#!/usr/bin/env python3
"""Python function that returns all students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """return sorted avg"""
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ])
