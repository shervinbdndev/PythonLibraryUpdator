try:
    import os
    import sys
    import subprocess
    from typing import Any

except:
    raise ModuleNotFoundError.__doc__

finally:
    ...
    
    
    
class PythonLibraryUpdator:
    def __init__(self) -> Any:
        self.currentPythonVersion : int = int(sys.version[0])
        
        if (self.currentPythonVersion < 3):
            print(f'Your Current Python Version is {sys.version} , Update Your Python to Version 3')
        else:
            for package in os.popen(cmd='pip freeze').readlines():
                subprocess.call(args=['pip3' , 'install' , '--upgrade' , package.strip().split(sep='==')[0]])
            
            
            
            

if (__name__ == '__main__' and __package__ is None):
    PythonLibraryUpdator()