"""Thynnus - Override Annotation

Thynnus provides a new feature, annotation, to Python checking the
element is meant to override an element declared in a superclass.

"""


class NoSuperClassMethodFound(Exception):
    """No Super Class Method Found"""

    def __init__(self, method_name) -> None:
        super().__init__(
            f"No method named {method_name} found in superclass."
        )


def override(cls):
    """Override Decorator"""
    def decorator(method):
        if method.__name__ not in dir(cls):
            raise NoSuperClassMethodFound(method.__name__)
        return method
    return decorator
