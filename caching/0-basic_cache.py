#!/usr/bin/python3
"""This is a basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic cache"""

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
