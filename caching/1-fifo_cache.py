#!/usr/bin/python3
"""This is a FIFO cache"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A fifo cache"""

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
