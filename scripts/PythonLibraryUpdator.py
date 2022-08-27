if (__debug__):
    try:
        import os
        import sys
        import asyncio
        import requests
        import colorama
        import subprocess
        from typing_extensions import Self
        from typing import (Coroutine , Type , Union , Literal , Any , final)

    except ModuleNotFoundError.__doc__ as MNFE:
        raise MNFE from None

    finally:
        ...
else:
    raise
    
    

@final
class PythonVersionUpdator:
    def __init__(self: Self) -> Union[Literal[None] , Self]:
        super(PythonVersionUpdator , self).__init__()
        try:
            subprocess.call(args=['py' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])
        except:
            subprocess.call(args=['python3' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])

    
    

@final    
class PythonLibraryUpdator:
    
    @staticmethod
    async def update() -> Coroutine:
        for package in os.popen(cmd='pip freeze').readlines():
            try:
                subprocess.call(args=['pip3' , 'install' , '--upgrade' , package.strip().split(sep='==')[0]])
            except ConnectionError.__doc__ as CE:
                print('%s %s Occurred' % colorama.ansi.Fore.RED , CE)
                break
            except requests.RequestException.__doc__ as RE:
                print('%s %s Occurred' % colorama.ansi.Fore.RED , RE)
                break
            except KeyboardInterrupt.__doc__ as KI:
                print('%s %s Occurred' % colorama.ansi.Fore.RED , KI)
                break
        else:
            print('%s All Libraries Updated Successfully' % colorama.ansi.Fore.GREEN)
            
    def __new__(cls: Type[Self] , *args: Any , **kwargs: Any) -> Union[Literal[None] , Self]:
        if (sys.version_info[0:2] in [(3,7) , (3,8) , (3,9) , (3,10)]):
            return super().__new__(cls , *args , **kwargs)
        return None
            
      
      
def main() -> Literal[None]:
    PythonVersionUpdator()
    asyncio.run(main=PythonLibraryUpdator().update())
      
            

if (__name__ == '__main__' and __package__ is None):
    main()