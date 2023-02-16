def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MySingletonClass:
    pass



singleton1 = MySingletonClass()
singleton2 = MySingletonClass()

print(singleton1 is singleton2) # True
