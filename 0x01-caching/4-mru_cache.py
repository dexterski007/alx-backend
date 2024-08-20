#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Mru cache fix """
    def __init__(self):
        """ constructor func """
        super().__init__()

    def put(self, key, item):
        """ put function fix """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = next(reversed(self.cache_data))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get item fixed """
        if key and key in self.cache_data.keys():
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
