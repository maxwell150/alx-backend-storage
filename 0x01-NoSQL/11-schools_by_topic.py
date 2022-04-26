#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """retruns a list"""
    school_list = [i for i in mongo_collection.find({ "topics" : topic })]
    return school_list
