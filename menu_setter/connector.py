from .core import Core
from .exceptions import Message_except as exception
from time import sleep


"""\__________________________________MESSAGE__________________________________/"""
    # useful commands
    
def message_back(msg, core): # message back from outer codes
    
    if msg == 'menu_setter.core.back':
        connect()
    elif msg == 'menu_setter.core.stopMove':
        input()
    elif 'menu_setter.core.setTimer' in msg:
        
        if len(msg) == 2:
            sleep(msg[1])
        else:
            raise exception.missed_argument(1, msg, "delay_time")


"""\___________________________________BODY___________________________________/"""
    # connector connecting objects from core to your project methods
    # CORE --connector(obj)--> PROJECT
    
def connect(moduleName=None, func=None, args=None, className=None, attr=None):
    
    """ Create Object From Core Class """
    core = Core(
        moduleName,
        func,
        args,
        className,
        attr
    )
    
    """ Call Action from Main Menu """
    for methodName, args in core.method_caller():
        try:
            
            """ Create an object from class """
            obj, dtype = core.obj_caller()
            
            if obj and dtype == 'c': # if object exists & obj data type is class base
                method = getattr(obj, methodName)
                
            if obj and dtype == 'f': # if object exists & obj data type is function base
                method = obj
            
            """ The method may have no arguments """
            if not args:
                message = method()
            else:
                message = method(*args)

            if message: # if message back from outer code's response the defined request's
                message_back(message, core)
            
            print("\n>===============================================@")
                        
        except NameError as error:
            print(error)
        except ModuleNotFoundError as error:
            print(error)

