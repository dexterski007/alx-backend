#!/usr/bin/env python3
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
            discarded = next(reversed(self.cache_data))
            self.cache_data.pop(discarded)
            print("DISCARD: {}".format(discarded))
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get item"""
        return self.cache_data.get(key, None)
