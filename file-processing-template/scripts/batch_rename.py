#!/usr/bin/env python3
import argparse
from pathlib import Path


def planned_name(path, prefix):
    return path.with_name(f"{prefix}{path.name}")


def main():
    parser = argparse.ArgumentParser(description="Prefix-rename files by extension.")
    parser.add_argument("directory")
    parser.add_argument("--ext", default=".txt", help="File extension filter")
    parser.add_argument("--prefix", default="processed_")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.directory)
    files = sorted([p for p in root.iterdir() if p.is_file() and p.suffix == args.ext])

    collisions = []
    plan = []
    for f in files:
        target = planned_name(f, args.prefix)
        if target.exists() and target != f:
            collisions.append((f, target))
        plan.append((f, target))

    if collisions:
        for src, dst in collisions:
            print(f"collision: {src} -> {dst}")
        raise SystemExit("Aborting due to collisions")

    for src, dst in plan:
        print(f"{src.name} -> {dst.name}")
        if not args.dry_run and src != dst:
            src.rename(dst)


if __name__ == "__main__":
    main()
