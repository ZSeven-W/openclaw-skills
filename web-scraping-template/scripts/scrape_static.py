#!/usr/bin/env python3
import argparse
import json
import re
import urllib.request
from datetime import datetime, timezone

TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(html):
    return TAG_RE.sub("", html).strip()


def extract_titles(html):
    matches = re.findall(r"<h1[^>]*>(.*?)</h1>|<h2[^>]*>(.*?)</h2>", html, flags=re.I | re.S)
    titles = []
    for h1, h2 in matches:
        text = strip_tags(h1 or h2)
        if text:
            titles.append(text)
    return titles


def main():
    parser = argparse.ArgumentParser(description="Fetch a static page and extract H1/H2 titles.")
    parser.add_argument("url")
    parser.add_argument("--user-agent", default="OpenClawSkillTemplateBot/1.0")
    args = parser.parse_args()

    req = urllib.request.Request(args.url, headers={"User-Agent": args.user_agent})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="replace")

    output = {
        "source_url": args.url,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "titles": extract_titles(html),
    }
    print(json.dumps(output, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
