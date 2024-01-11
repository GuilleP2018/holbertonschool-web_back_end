#!/usr/bin/env python3
"""all"""
import pymongo


def list_all(mongo_collection):
    """list all"""
    if mongo_collection is not None:
        document = mongo_collection.find()
        return list(document) if document else []
    return []
