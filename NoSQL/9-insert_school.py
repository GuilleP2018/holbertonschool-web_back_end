#!/usr/bin/env python3
"""insert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert a document in Python"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
