"""Contains functions which are useful for collecting safe inputs"""


def int_safe_input(
    text: str,
    lowest: int | None = None,
    highest: int | None = None,
) -> int:
    """Function which is used to safely get an integer input"""
    while True:
        try:
            integer: int = int(input(text))
            if lowest is not None and highest is not None:
                if lowest > integer or highest < integer:
                    print(f"Input must be between {lowest} and {highest}")
                    continue
            elif lowest is not None:
                if lowest > integer:
                    print(f"Input minimum is {lowest}")
                    continue
            elif highest is not None:
                if highest < integer:
                    print(f"Input maximum is {highest}")
                    continue
            return integer
        except ValueError:
            print("Integer input expected\n")


def str_safe_input(text: str = "", min_length: int = 0, max_length: int = 100) -> str:
    """Function which is used to safely get a boolean input"""
    while True:
        string = input(text)
        if min_length <= len(string) <= max_length:
            return string
        print(f"At least {min_length} and maximum {max_length} characters needed\n")


def bool_safe_input(text: str = "") -> bool:
    """Function which is used to safely get a boolean input"""
    while True:
        try:
            boolean: bool = bool(input(text))
            return boolean
        except ValueError:
            print("Boolean input expected (1 for true, 0 for false)\n")
