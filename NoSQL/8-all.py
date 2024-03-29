#!/usr/bin/env python3
""" list all documents in a collection in PyMongo"""
import pymongo


def list_all(mongo_collection):
    """list all"""
    if mongo_collection is not None:
        document = mongo_collection.find()
        return list(document) if document else []
    return []
