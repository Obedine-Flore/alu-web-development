#!/usr/bin/python3
"""This is an LRU cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ An LRU cache """

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            if self.cache_data:
                discard = next(iter(self.cache_data))
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item in the cache"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data[key]
