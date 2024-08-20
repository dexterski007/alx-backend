#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Lru cache func """
    def __init__(self):
        """ constructor func ok """
        super().__init__()

    def put(self, key, item):
        """ put function func """
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data.keys()))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item

    def get(self, key):
        """ get item func """
        if key is None or key not in self.cache_data.keys():
            return
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return self.cache_data.get(key, None)
