#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Fifo cache """

    def __init__(self):
        """ constructor func """
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item

    def get(self, key):
        """ get item func"""
        return self.cache_data.get(key, None)
