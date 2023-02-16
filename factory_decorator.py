"""def factory(base_class):
    def class_factory(class_name, class_parents, class_attrs):
        class_attrs["factory_class"] = base_class
        return type(class_name, (class_parents,), (class_attrs,))
    return class_factory

@factory
class BaseClass:
    def __init__(self, name) -> None:
        self.name = name

class ConcreteClass1(BaseClass):
    def __init__(self, age) -> None:
        super().__init__()
        self.age = age


class ConcreteClass2(BaseClass):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def print_name(self):
        print("The name is: ")


class_map = {
    "ConcreteClass1": ConcreteClass1,
    "ConcreteClass2": ConcreteClass2,
}

def create_object(class_name, *args, **kwargs):
    obj_class = class_map[class_name]
    return obj_class(*args, **kwargs)

obj1 = create_object("ConcreteClass1")
obj2 = create_object("ConcreteClass2")"""
