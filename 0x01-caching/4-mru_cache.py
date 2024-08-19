#!/usr/bin/python3
""" Basic caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Mru cache """
    def __init__(self):
        """ constructor func """
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = next(reversed(self.cache_data))
            self.cache_data.pop(discarded)
            print("DISCARD: {}".format(discarded))
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item"""
        if key is None or key not in self.cache_data.keys():
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
