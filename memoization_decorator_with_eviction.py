def memoize_with_eviction(max_cache_size=100):
    def memoize(func):
        cache = {}
        cache_keys = []

        def wrapper(*args):
            if args in cache:
                return cache[args]

            result = func(*args)
            cache[args] = result
            cache_keys.append(args)

            if len(cache_keys) > max_cache_size:
                del cache[cache_keys[0]]
                cache_keys.pop(0)

            return result
        return wrapper
    return memoize

# @memoize_with_eviction(max_cache_size=100)
# def expensive_function(arg1, arg2, ... , argn):
#     # Function implementation
#     ...
