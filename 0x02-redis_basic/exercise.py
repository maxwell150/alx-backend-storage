#!/usr/bin/env python3
"""redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper func"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapeper func"""
        input = str(args)
        self._redis.rpush(key + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", output)
        return output
    return wrapper

def replay(method: Callable):
    """display the history of calls of a particular function"""
    key = method.__qualname__
    redis = method.__self__.redis
    count = redis.get(key).decode('utf-8')
    print(f"{key} was called {count} times:")
    inputs = redis.lrange(key + ":inputs", 0, -1)
    outputs = redis.lrange(key + ":outputs", 0, -1)
    data = list(zip(inputs, outputs))
    for k, v in data:
        attr, v = k.decode('utf-8'), v.decode('utf-8')
        print(f"{key}(*{attr}) -> {v}")

class Cache:
    """declares a Cache redis class"""
    def __init__(self):
        """instance of the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

