#!/usr/bin/env python3
"""List all docs"""
import pymongo


def list_all(mongo_collection):
    """returns docs in a collection or empty list if none"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
