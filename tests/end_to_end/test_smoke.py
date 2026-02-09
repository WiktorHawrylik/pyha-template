from python_library_template import greet


def test_library_smoke() -> None:
    message = greet("Template")
    assert "Template" in message
