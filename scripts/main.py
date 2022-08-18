try:
    import os
    import sys
    import asyncio
    import platform
    import subprocess
    from typing_extensions import Self
    from typing import (Coroutine , Type , Any)

except ModuleNotFoundError as mnfe:
    raise mnfe.__doc__

finally:
    ...
    
    

class PythonVersionUpdator:
    def __init__(self : Self) -> Any:
        super(PythonVersionUpdator , self).__init__()
        if (platform.system()[0].upper() in ['W' , 'L']):
            try:
                subprocess.call(args=['py' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])
            except:
                subprocess.call(args=['python3' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])

    
    
    
class PythonLibraryUpdator:
    
    @classmethod
    async def update(cls : Type[Self]) -> Coroutine:
        cls.currentPythonVersion : int = int(sys.version[0])
        
        if (cls.currentPythonVersion < 3):
            print(await f'Your Current Python Version is {sys.version} , Update Your Python to Version 3')
        else:
            for package in os.popen(cmd='pip freeze').readlines():
                subprocess.call(args=['pip3' , 'install' , '--upgrade' , package.strip().split(sep='==')[0]])
            
            
            
            

if (__name__ == '__main__' and __package__ is None):
    PythonVersionUpdator()
    asyncio.run(main=PythonLibraryUpdator().update())