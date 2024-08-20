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
                self.cache_data[key] = item
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least = min(self.freq.values())
                    least_keys = [k for k, v in self.freq.items()
                                  if v == least]
                    discarded = min(least_keys, key=self.freq.get)
                    self.cache_data.pop(discarded)
                    self.freq.pop(discarded)
                    print("DISCARD: {}".format(discarded))
                self.cache_data[key] = item
                self.freq[key] = 1

    def get(self, key):
        """ get item fix """
        if key and key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
