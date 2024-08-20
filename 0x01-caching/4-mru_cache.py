#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Mru cache fix """
    def __init__(self):
        """ constructor func """
        super().__init__()
        self.align = []

    def put(self, key, item):
        """ put function fix """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.align.pop()
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.align.append(key)

    def get(self, key):
        """ get item fixed """
        if key and key in self.cache_data:
            self.align.remove(key)
            self.align.append(key)
            item = self.cache_data.get(key)
            return item
