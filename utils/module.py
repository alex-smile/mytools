import logging
from importlib import import_module
from typing import Any, Dict

logger = logging.getLogger(__name__)


class ModuleShortcut:
    """管理自动加载的模块"""

    __module_pool: Dict[str, Any] = {}

    def __new__(cls, module_name):
        if module_name not in cls.__module_pool:
            try:
                cls.__module_pool[module_name] = import_module(module_name)
            except Exception:
                logger.exception("import module error, module_name=%s", module_name)
                cls.__module_pool[module_name] = None
        return cls.__module_pool[module_name]

    def get(self, attr_name):
        return getattr(self, attr_name)

    def __getattr__(self, attr_name):
        return self.get(attr_name)