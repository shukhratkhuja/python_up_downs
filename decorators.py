import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# say_hello = my_decorator(say_hello)

# FUNCTION RUNTIME DECORATOR (AOP - aspect oriented programming) # logging runtime of the function
def runtime(*args, **kwargs):
    def decorator_function(func):
        def wrapper(): 
            st = time.time()
            func_result = func()
            ed = time.time()
            print(kwargs['name_of_task'], ' run: ', ed-st, '\nThe function result is: ', func_result)
        return wrapper
    return decorator_function


@runtime(name_of_task='My celery task')
def sleep_func():
    print('started sleeping at: ', time.time())   
    
    time.sleep(2)

    print('finished sleeping at: ', time.time())
    return 2 + 2
# sleep_func()

#memoization

def memoize(func):
    cache = {}
    def wrapper(*args):
        
        if args in cache:
            
            return cache[args]
        result = func(*args)
        print(result)
        time.sleep(1)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))