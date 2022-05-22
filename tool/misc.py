from typing import Union


class lispInternalNumberException(Exception):
    pass


def to_number(x) -> Union[int, float, complex]:
    try:
        return int(x)
    except (ValueError, TypeError):
        try:
            return float(x)
        except (ValueError, TypeError):
            try:
                return complex(x)
            except (ValueError, TypeError):
                raise lispInternalNumberException

def is_number(x) -> bool:
    try:
        _ = to_number(x)
        return True
    except lispInternalNumberException:
        return False
