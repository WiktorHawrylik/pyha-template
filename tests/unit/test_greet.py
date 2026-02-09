from python_library_template.core import greet


def test_greet_returns_message() -> None:
    assert greet("World") == "Hello, World!"
