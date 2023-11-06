from json import load
from os import path
from .extra_opt import menu_config_path as PATH
from .extra_opt import menu_config_fileName as fileName
from .extra_opt import menu_config_fileExtension as fileExtension


def menu_ext(_path_=PATH, _fileName_=fileName, _fileExtension_=fileExtension):
    
    file_path = path.join(_path_, _fileName_)
    file_path = "{}.{}".format(file_path, _fileExtension_)
    
    with open(file_path) as data_menu_json:
        menu_data = load(data_menu_json)
    
    return menu_data

if __name__ == '__main__':
    menu_ext()
    print()
    print("> Data extracted successfully!!!:D <")
    print()