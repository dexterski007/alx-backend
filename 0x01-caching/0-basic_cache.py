#!/usr/bin/python3
""" Basic caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic cache """

    def put(self, key, item):
        """ put new items in cache """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """ get item value from cache """
        return self.cache_data.get(key, None)
