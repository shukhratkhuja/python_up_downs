"""
Thread Pool: 
A thread pool is a class that manages a pool of worker threads. 
This thread pool can be implemented as a singleton to ensure that
only one instance of the thread pool is used by the application.
"""

import concurrent.futures

class ThreadPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

thread_pool = ThreadPool()
future = thread_pool.executor.submit(lambda x: x**2, 5)
result = future.result()
another_thread_pool = ThreadPool()
print(another_thread_pool.executor == thread_pool.executor) # Output: True
