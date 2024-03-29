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
            os.system(command='cls')
        except:
            os.system(command='clear')
        print('\n%s Updating Interpreter . . .\n%s' % (colorama.ansi.Fore.GREEN , colorama.ansi.Fore.WHITE))
        try:
            subprocess.call(args=['py' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])
        except:
            subprocess.call(args=['python3' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])
        finally:
            print('\n%s Interpreter Updated\n%s' % (colorama.ansi.Fore.GREEN , colorama.ansi.Fore.WHITE))

    
    

@final    
class PythonLibraryUpdator:
    
    @staticmethod
    async def update() -> Union[Coroutine , str]:
        print('\n%s Updating Libraries . . .\n%s' % (colorama.ansi.Fore.GREEN , colorama.ansi.Fore.WHITE))
        for package in os.popen(cmd='pip freeze').readlines():
            try:
                subprocess.call(args=['pip3' , 'install' , '--upgrade' , package.strip().split(sep='==')[0]])
            except ConnectionError.__doc__ as CE:
                raise '%s %s Occurred' % (colorama.ansi.Fore.RED , CE)
            except requests.RequestException.__doc__ as RE:
                raise '%s %s Occurred' % (colorama.ansi.Fore.RED , RE)
            except KeyboardInterrupt.__doc__ as KI:
                raise '%s %s Occurred' % (colorama.ansi.Fore.RED , KI)
        else:
            print('\n%s All Libraries Updated Successfully \n%s' % (colorama.ansi.Fore.GREEN , colorama.ansi.Fore.WHITE))
            
    def __new__(cls: Type[Self] , *args: Any , **kwargs: Any) -> Union[Literal[None] , Self]:
        if (sys.version_info[0:2] in [(3,7) , (3,8) , (3,9) , (3,10)]):
            return super().__new__(cls , *args , **kwargs)
        return None
            
      
      
def main() -> Literal[None]:
    PythonVersionUpdator()
    asyncio.run(main=PythonLibraryUpdator().update())
      
            

if (__name__ == '__main__' and __package__ is None):
    main()