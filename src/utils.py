from airtest.core.api import *
import subprocess
import sys

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

def multiplayer_pass_stage(accountList: list):
    """
    This function is used to pass the stage in multiplayer mode. 
    It starts a new process for each account in the provided list, 
    passing the stage for each account concurrently. 
    If any of the processes exit with a non-zero status code, 
    indicating an error, the function will print an error message 
    and exit the main program with the same status code.

    Args:
        accountList (list): A list of Account objects representing 
                             the accounts that will pass the stage.
    """
    # pass the level
    # All accounts pass the stage
    processes = []
    for acc in accountList:
        p = subprocess.Popen(["python", "src/main.py", "--pass-stage", str(acc.idx)])
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        exit_code = p.wait()
        if exit_code != 0:
            print(f"Process {p.pid} exited with code {exit_code}, exiting...")
            sys.exit(exit_code)
