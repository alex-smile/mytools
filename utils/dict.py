from functools import reduce
from operator import getitem

_NOT_SET = object()


def get_exist_items(obj: dict, keys: list) -> dict:
    return {key: obj[key] for key in keys if key in obj}


def deep_item_getter(keys, default=_NOT_SET):
    """Chaining value getter of dict"""

    def getter(obj):
        return get_deep_item(obj, keys, default=default)

    return getter


def get_deep_item(obj, keys, default=_NOT_SET):
    """递归获取深层数据

    :param keys: 键列表：["foo", "bar"]，或用 "." 连接的键路径："foo.bar"
    """
    if isinstance(keys, str):
        keys = keys.split(".")

    try:
        return reduce(getitem, keys, obj)
    except (KeyError, IndexError):
        if default is _NOT_SET:
            raise

        return default