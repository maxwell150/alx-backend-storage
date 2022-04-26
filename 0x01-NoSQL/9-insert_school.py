#!/usr/bin/env python3
"""insert a doc in py"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """returns the new _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
