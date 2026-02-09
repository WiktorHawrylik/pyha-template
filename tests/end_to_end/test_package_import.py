import python_library_template


def test_package_exports_greet() -> None:
    assert python_library_template.greet("Template") == "Hello, Template!"
