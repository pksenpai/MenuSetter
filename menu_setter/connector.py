from core import Core
from time import sleep


def message_back(msg, core): # message back from outer codes
    
    """\__________________________ERRORS__________________________/"""
    
    ERROR_missed_message_argument = (
        "ERROR: missing {} required positional argument --> ('{}', <!MISSED HERE!>={})"
        )
    
    """\__________________________MESSAGES__________________________/"""
    
    if msg == 'menu_setter.core.back':
        connect(core)
    elif msg == 'menu_setter.core.stopMove':
        input()
    elif 'menu_setter.core.setTimer' in msg:
        ERROR = ERROR_missed_message_argument.format(1, msg, "delay_time")
        raise TypeError(ERROR) if len(msg) != 2 else msg
        sleep(msg[1])

def connect(core):
    """ Call Action from Main Menu """
    for methodName, args in core.method_caller():
        try:
            if methodName == 'back': # its back to first of menu page %%%BUG%%%
                connect(core)
            
            """ Create an object from class """
            obj = core.obj_caller()
            method = getattr(obj, methodName)
            
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



        
""" TEST CALL"""
# 1-attribute, 2-argument, 3-module, 4-className
core_obj = Core(('Parsa', 'Ahmadian', 'PKPY', 'pk', '123'), (':D', 21), 'test001', 'test')
connect(core_obj)
