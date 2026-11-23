"""Validator for lesson plan templates."""
import os
import sys
import glob

REQUIRED_SECTIONS = ["## Objectives", "## Materials", "## Steps", "## Assessment"]


def validate_file(path: str) -> dict:
    with open(path) as f:
        content = f.read()
    missing = [s for s in REQUIRED_SECTIONS if s not in content]
    return {"file": path, "valid": len(missing) == 0, "missing": missing}


def validate_dir(directory: str) -> list:
    results = []
    for path in sorted(glob.glob(os.path.join(directory, "*.md"))):
        if "activity_guide" in os.path.basename(path):
            continue
        results.append(validate_file(path))
    return results


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description="Lesson Plan Validator")
    parser.add_argument("directory", help="Directory containing lesson plans")
    args = parser.parse_args(argv)
    results = validate_dir(args.directory)
    all_valid = True
    for r in results:
        status = "OK" if r["valid"] else "FAIL"
        print(f"{status}: {os.path.basename(r['file'])}")
        if r["missing"]:
            print(f"  Missing: {', '.join(r['missing'])}")
            all_valid = False
    if not all_valid:
        sys.exit(1)
    print(f"\nAll {len(results)} lesson plans valid.")


if __name__ == "__main__":
    main()
