import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from toolkit.validator import validate_file, validate_dir, REQUIRED_SECTIONS


def test_valid_lesson_plan():
    content = "\n".join(REQUIRED_SECTIONS) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        path = f.name
    try:
        result = validate_file(path)
        assert result["valid"] is True
        assert result["missing"] == []
    finally:
        os.unlink(path)


def test_missing_section():
    content = "## Objectives\n## Materials\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        path = f.name
    try:
        result = validate_file(path)
        assert result["valid"] is False
        assert "## Steps" in result["missing"]
        assert "## Assessment" in result["missing"]
    finally:
        os.unlink(path)


def test_validate_dir():
    with tempfile.TemporaryDirectory() as d:
        for i in range(3):
            with open(os.path.join(d, f"plan_{i}.md"), "w") as f:
                f.write("\n".join(REQUIRED_SECTIONS))
        results = validate_dir(d)
        assert len(results) == 3
        assert all(r["valid"] for r in results)


def test_templates_valid():
    d = os.path.join(os.path.dirname(__file__), "..", "templates")
    results = validate_dir(d)
    assert len(results) == 3
    assert all(r["valid"] for r in results)


def test_activity_guide_skipped():
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "activity_guide.md"), "w") as f:
            f.write("# Guide")
        with open(os.path.join(d, "plan.md"), "w") as f:
            f.write("\n".join(REQUIRED_SECTIONS))
        results = validate_dir(d)
        assert len(results) == 1


def test_empty_missing_all():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("# Title only")
        path = f.name
    try:
        result = validate_file(path)
        assert len(result["missing"]) == 4
    finally:
        os.unlink(path)
