import os

__CURR_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(__CURR_DIR, '../..')


def get_path(path: str)->str: 
    return os.path.join(ROOT_DIR + path)


def ensure_path_exists(path: str)->None:
    abs_path = get_path(path=path)
    head, tail = os.path.split(abs_path)
    os.makedirs(head, exist_ok=True)


def get_path_safe(path: str)->str:
    '''
    Wrapper method to get filepath.
    If any of the folders in the path is missing, it creates the directory
    The filepath arg should end with / if it is a folder path, and should not end with / if a filepath
    ''' 
    ensure_path_exists(path=path)
    return get_path(path=path)

