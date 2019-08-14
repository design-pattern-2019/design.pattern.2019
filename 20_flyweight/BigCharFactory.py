from threading import Lock
from BigChar import BigChar


class BigCharFactory:
    _unique_instance = None
    _lock = Lock()  # クラスロック
    pool = {}

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def getInstance(cls):
        if not cls._unique_instance:
            with cls._lock:
                if not cls._unique_instance:
                    cls._unique_instance = cls.__internal_new__()

        return cls._unique_instance

    def getBigChar(self, charname):
        with self._lock:
            bc = self.pool.get(charname, 'empty')
            if bc == 'empty':
                bc = BigChar(charname)
                self.pool[charname] = bc
            return bc
