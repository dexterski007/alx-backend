#!/usr/bin/env python3
""" Basic caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Lfu cache """
    def __init__(self):
        """ constructor func fix """
        super().__init__()
        self.freq = {}
        self.usage = {}

    def put(self, key, item):
        """ put function fix """
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if key in self.freq.keys():
                self.freq[key] += 1
            else:
                self.freq[key] = 0
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ get item fix """
        if key and key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
