#!/usr/bin/env python3
import argparse
from pathlib import Path

TEMPLATE = '''#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="{description}")
    parser.add_argument("input", help="Input path")
    parser.add_argument("--output", default="", help="Output path")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    args = parser.parse_args()

    if args.dry_run:
        print(f"[dry-run] would process: {args.input}")
        return

    print(f"processing: {args.input}")


if __name__ == "__main__":
    main()
'''


def main():
    parser = argparse.ArgumentParser(description="Generate a starter argparse CLI script.")
    parser.add_argument("--name", required=True, help="Script filename, e.g. my_tool.py")
    parser.add_argument("--description", default="Generated CLI command")
    parser.add_argument("--out-dir", default=".")
    args = parser.parse_args()

    out = Path(args.out_dir) / args.name
    out.write_text(TEMPLATE.format(description=args.description), encoding="utf-8")
    out.chmod(0o755)
    print(out)


if __name__ == "__main__":
    main()
