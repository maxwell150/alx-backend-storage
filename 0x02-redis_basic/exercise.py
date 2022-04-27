#!/usr/bin/env python3
"""redis class and methods"""
import redis
from uuid import uuid4
from typing import Union


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

