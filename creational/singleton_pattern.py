import threading
from datetime import datetime
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
class SimpleSingleton:
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
        print('initializing <super>...')

    # return the singleton instance
    def __call__(cls: Any, *args: Any, **kwargs: Any) -> Any:
        return cls._instances[cls]


'''the implementation of MetaSingletonEager'''
class ConcreteMetaSingletonEager(metaclass=MetaSingletonEager):
    def __init__(self) -> None:
        print('initializing <child>...')
        pass


'''thread-safe implementation'''
class ThreadSafeSingleton:
    # class-level variable to store single class instance
    _instance = None

    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    def __new__(cls: Any) -> Any:

        # acquire the lock to ensure thread safety
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)

        return cls._instance


'''thread-safe metaclass implementation'''
class MetaThreadSafeSingleton(type):
    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):

        # acquire the lock to ensure thread safety
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


'''the implementation of MetaThreadSafeSingleton'''
class ConcreteMetaThreadSafeSingleton(metaclass=MetaThreadSafeSingleton):
    def time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


############################################################################
# Usage
############################################################################


# classic GoF implementation
s1_1 = ClassicSingleton.get_instance()
s1_2 = ClassicSingleton.get_instance()
print(s1_1 is s1_2) # expected True

# simple python way
s2_1 = SimpleSingleton()
s2_2 = SimpleSingleton()
print(s2_1 is s2_2) # expected True

# best singleton implementation with lazy initialization
s3_1 = ConcreteMetaSingletonLazy()
s3_2 = ConcreteMetaSingletonLazy()
print(s3_1 is s3_2) # expected True

# best singleton implementation with eager loading
s4_1 = ConcreteMetaSingletonEager()
s4_2 = ConcreteMetaSingletonEager()
print(s4_1 is s4_2) # expected True

# thread-safe implementation
s5 = ThreadSafeSingleton()

# thread-safe metaclass implementation
def get_singleton_instance():
    s = ConcreteMetaThreadSafeSingleton()
    print(s.time())

# create a list to store threads
threads = []

# create 10 thread objects, appending each to the threads list
for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

# start each thread in the threads list
for t in threads:
    t.start()

# wait for each thread to finish
for t in threads:
    t.join()
