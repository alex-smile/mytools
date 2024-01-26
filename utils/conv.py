from typing import Any, Optional


def str_bool(value: Any, allow_null: bool = True) -> Optional[bool]:
    """Convert string/int/bool to bool

    >>> str_bool("true")
    True
    >>> str_bool("false")
    False
    >>> str_bool("1")
    True
    >>> str_bool("0")
    False
    """
    if value in ["true", "True", "TRUE", "1", 1, True]:
        return True

    elif value in ["false", "False", "FALSE", "0", 0, False]:
        return False

    elif value in ["null", "Null", "NULL", "", None] and allow_null:
        return None

    raise ValueError("Must be a valid boolean")

    
def smart_str(s, encoding="utf-8"):
    if issubclass(type(s), str):
        return s

    try:
        if isinstance(s, bytes):
            s = str(s, encoding)
        else:
            s = str(s)
    except UnicodeDecodeError as e:
        raise e

    return s

    
def smart_bytes(s, encoding="utf-8"):
    if isinstance(s, bytes):
        if encoding == "utf-8":
            return s
        else:
            return s.decode("utf-8").encode(encoding)
    return s.encode(encoding)