"""
Cache: 
A cache is a class that stores data in memory to speed up access to frequently accessed data. 
This cache can be implemented as a singleton to ensure that 
only one instance of the cache is used by the application.
"""

class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cache = {}

cache = Cache()
cache.cache['key'] = 'value'
another_cache = Cache()
print(another_cache.cache['key']) # Output: 'value'
