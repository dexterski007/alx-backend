#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Lru cache func """
    def __init__(self):
        """ constructor func ok """
        super().__init__()
        self.align = []

    def put(self, key, item):
        """ put function func """

        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.align.pop(0)
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.align.append(key)

    def get(self, key):
        """ get item func """
        if key in self.cache_data:
            self.align.remove(key)
            self.align.append(key)
            return self.cache_data.get(key, None)
