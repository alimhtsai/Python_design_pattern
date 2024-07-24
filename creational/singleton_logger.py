from abc import ABCMeta, abstractmethod
import threading
import logging


'''a metaclass for creating singleton classes'''
class SingletonMeta(type):
    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # acquire the lock to make sure that only one thread can enter this block at a time
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


'''this metaclass combines the features of ABCMeta and SingletonMeta'''
class SingletonABCMeta(ABCMeta, SingletonMeta):
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)


'''an abstract class with the SingletonABCMeta metaclass'''
class BaseLogger(metaclass=SingletonABCMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


'''cconcrete implementation of BaseLogger'''
class MyLogger(BaseLogger):
    def __init__(self):
        print('<Logger init> initializing logger...')

        # create a logger object with the specified name
        self._logger = logging.getLogger('my_logger')
        # set the logging level to DEBUG
        self._logger.setLevel(logging.DEBUG)

        # create a file handler to log messages to a file
        file_handler = logging.FileHandler('my_log_file.log')
        # set the file handler logging level to DEBUG
        file_handler.setLevel(logging.DEBUG)

        # create a console handler to log messages to the console
        console_handler = logging.StreamHandler()
        # set the console handler logging level to INFO
        console_handler.setLevel(logging.INFO)

        # define the log message format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # set the formatter for both the file and console handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # add the file and console handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)


############################################################################
# Usage
############################################################################


# create an instance of MyLogger
logger = MyLogger()

# log different types of messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
