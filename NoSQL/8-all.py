#!/usr/bin/env python3
"""all"""
import pymongo


def list_all(mongo_collection):
    """list all"""
    doc =[]
    for i in mongo_collection.find():
        doc.append(i)
    return doc
