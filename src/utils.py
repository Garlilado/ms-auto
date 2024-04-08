from airtest.core.api import *

def set_device(func):
    """
    A decorator that sets the current device before calling the decorated function.

    Args:
        func (callable): The function to be decorated. This function should be a method of a class that has a 'dev' attribute.

    Returns:
        callable: The decorated function, which will call 'set_current(self.dev)' before calling the original function.
    """
    def wrapper(self, *args, **kwargs):
        set_current(self.serialNo)
        return func(self, *args, **kwargs)
    return wrapper