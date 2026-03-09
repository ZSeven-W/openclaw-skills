#!/usr/bin/env python3
import argparse
import json
import random
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RETRY_STATUS = {429, 500, 502, 503, 504}


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_url(base_url, endpoint, query):
    url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
    if query:
        url += "?" + urllib.parse.urlencode(query)
    return url


def request_once(config):
    import os

    url = build_url(config["base_url"], config["endpoint"], config.get("query", {}))
    headers = dict(config.get("headers", {}))

    auth = config.get("auth", {})
    if auth.get("type") == "bearer":
        token = os.environ.get(auth.get("token_env", ""), "")
        if not token:
            raise RuntimeError("Missing bearer token env var")
        headers["Authorization"] = f"Bearer {token}"

    body = config.get("body")
    data = None if body is None else json.dumps(body).encode("utf-8")
    if data and "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        url=url,
        data=data,
        headers=headers,
        method=config.get("method", "GET").upper(),
    )
    timeout = int(config.get("timeout", 20))

    start = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        duration_ms = int((time.time() - start) * 1000)
        return resp.getcode(), raw, duration_ms, url


def main():
    parser = argparse.ArgumentParser(description="Send one API request from JSON config.")
    parser.add_argument("config", help="Path to request-template style JSON")
    parser.add_argument("--retries", type=int, default=3, help="Retry attempts for transient errors")
    args = parser.parse_args()

    config = load_config(args.config)
    for attempt in range(1, args.retries + 2):
        try:
            status, raw, duration, url = request_once(config)
            payload = {
                "ok": 200 <= status < 300,
                "status": status,
                "duration_ms": duration,
                "url": url,
                "response": raw,
            }
            print(json.dumps(payload, indent=2, ensure_ascii=True))
            return 0
        except urllib.error.HTTPError as e:
            transient = e.code in RETRY_STATUS
            if attempt <= args.retries and transient:
                sleep_s = min(10, (2 ** (attempt - 1)) + random.random())
                time.sleep(sleep_s)
                continue
            print(json.dumps({"ok": False, "status": e.code, "error": str(e)}), file=sys.stderr)
            return 1
        except Exception as e:
            print(json.dumps({"ok": False, "error": str(e)}), file=sys.stderr)
            return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
