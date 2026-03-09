#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Basic CSV cleaner with required-column checks.")
    parser.add_argument("input_csv")
    parser.add_argument("output_csv")
    parser.add_argument("--required", nargs="*", default=[])
    parser.add_argument("--trim", nargs="*", default=[])
    parser.add_argument("--summary", default="")
    args = parser.parse_args()

    src = Path(args.input_csv)
    dst = Path(args.output_csv)

    with src.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing = [c for c in args.required if c not in fieldnames]
        if missing:
            raise SystemExit(f"Missing required columns: {', '.join(missing)}")

        rows = list(reader)

    for row in rows:
        for col in args.trim:
            if col in row and row[col] is not None:
                row[col] = row[col].strip()

    with dst.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "input": str(src),
        "output": str(dst),
        "rows": len(rows),
        "columns": len(fieldnames),
        "required_columns": args.required,
        "trimmed_columns": args.trim,
    }
    if args.summary:
        with open(args.summary, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=True)
    else:
        print(json.dumps(summary, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
