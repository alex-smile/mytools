import threading


class SingletonMeta(type):
    """
    examples:
        class Spam(metaclass=SingletonMeta):
            pass
    """
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class StrictSingletonMeta(type):
    """
    examples:
        class Spam(metaclass=StrictSingletonMeta):
            pass
    """
    def __init__(self, *args, **kwargs):
        self.__instance = None
        self.__lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is not None:
            return self.__instance

        with self.__lock:
            if self.__instance is not None:
                return self.__instance

            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance