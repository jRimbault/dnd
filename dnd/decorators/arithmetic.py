from enum import Enum


def arithmetic(cls=None, /, *, field: str = "value"):
    """Allows using a class as thin wrapper around a numeric value.

    Addition and subtraction will downgrade to the wrapped type.

    Examples :
    ```
    @dataclass
    @arithmetic
    class T:
        value: int

    assert isinstance(T(1) + T(1), int)
    assert T(1) + T(1) == 2
    ```
    """

    class Operation(tuple, Enum):
        equality = ("__eq__", "+", lambda a, b: a == b)
        greater_or_equal = ("__ge__", ">=", lambda a, b: a >= b)
        greater_than = ("__gt__", ">", lambda a, b: a > b)
        lesser_or_equal = ("__le__", "<=", lambda a, b: a <= b)
        lesser_than = ("__lt__", "<", lambda a, b: a < b)
        addition = ("__add__", "+", lambda a, b: a + b)
        subtraction = ("__sub__", "-", lambda a, b: a - b)

    def add_aritmetic_overloads(cls, field: str):
        def operation_decorator(cls, field: str, operand: str, func):
            def inner(self, other):
                if not isinstance(other, cls):
                    raise TypeError(
                        "unsupported operand type(s) "
                        + f"for {operand}: "
                        + f"'{type(self).__name__}' and '{type(other).__name__}'"
                    )
                return func(self.__dict__[field], other.__dict__[field])

            return inner

        def add_operation(operation: Operation):
            dunder, operand, func = operation
            if dunder not in cls.__dict__:
                setattr(cls, dunder, operation_decorator(cls, field, operand, func))

        for operation in Operation:
            add_operation(operation)

        return cls

    def wrap(cls):
        return add_aritmetic_overloads(cls, field)

    if cls is None:
        return wrap

    return wrap(cls)
