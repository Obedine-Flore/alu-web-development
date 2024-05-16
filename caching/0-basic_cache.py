#!/usr/bin/env python3

class BaseCaching:
    def __init__(self):
        self.cache_data = {}
class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """Assign the item value for the key in the dictionary cache_data."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in cache_data."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
