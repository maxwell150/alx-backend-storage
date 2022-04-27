#!/usr/bin/env python3
"""redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    """declares a Cache redis class"""
    def __init__(self):
        """instance of the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a sttring"""
        key = str(uuid4())
        self._redis.mset({ key : data })
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data to the desired format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: str) -> str:
        """return decoded byte in string"""
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """return decoded byte in int"""
        return int(self._redis.get(data))

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
