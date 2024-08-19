#!/usr/bin/python3
""" Basic caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Lifo cache """
    def __init__(self):
        """ constructor func """
        super().__init__()

    def put(self, key, item):
        """ put function """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = list(self.cache_data.keys())[-1]
            self.cache_data.pop(discarded)
            print("DISCARD: {}".format(discarded))
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """ get item"""
        return self.cache_data.get(key, None)
