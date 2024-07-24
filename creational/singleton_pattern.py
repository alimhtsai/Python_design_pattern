from typing import Any


'''classic GoF implementation'''
class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        # raise an error to prevent constructor utilization
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls: Any) -> Any:
        # lazy initialization
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        # return the single instance of the class
        return cls._instance


'''simple python way'''
class Singleton:
    # class-level variable to store single class instance
    _instance = None

    # override the __new__ method to control how new objects are created
    def __new__(cls: Any) -> Any:
        # lazy initialization
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


'''
metaclass: a class that defines the behavior and rule for creating other classes
best singleton implementation with lazy initialization
'''
class MetaSingletonLazy(type):
    # a dictionary that stores single instance of the class for each subclass
    # of the MetaSingleton metaclass
    _instances: dict = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any) -> Any:
        # lazy initialization
        if cls not in cls._instances:
            # create the instance by calling the __call__ method
            # of the parent's (super().__call__())
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


'''the implementation of MetaSingletonLazy'''
class ConcreteMetaSingletonLazy(metaclass=MetaSingletonLazy):
    def some_business_logic(self):
        pass


'''
metaclass: a class that defines the behavior and rule for creating other classes
best singleton implementation with eager loading
'''
class MetaSingletonEager(type):
    # a dictionary that stores single instance of the class for each subclass
    # of the MetaSingletonEager metaclass
    _instances: dict = {}

    # override: called during creation of sub-types
    def __init__(cls: Any, name: Any, bases: Any, dct: dict):
        # eager loading
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    # return the singleton instance
    def __call__(cls: Any, *args: Any, **kwargs: Any) -> Any:
        return cls._instances[cls]


'''the implementation of MetaSingletonEager'''
class ConcreteMetaSingletonEager(metaclass=MetaSingletonEager):
    def __init__(self) -> None:
        pass


# classic GoF implementation
s1 = ClassicSingleton.get_instance()

# simple python way
s2 = Singleton()

# best singleton implementation with lazy initialization
s3 = ConcreteMetaSingletonLazy()

# best singleton implementation with eager loading
s4 = ConcreteMetaSingletonEager()
