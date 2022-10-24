import os


def print_tab(path, tab_depth):
    print("\t" * tab_depth + path)


def is_directory(file):
    return os.path.isdir(file)


def directory_structure(path=os.path.abspath(os.getcwd()), tab_depth=0):
    """path - specify path giving double (\\ for windows), if not current path will be taken in arg"""
    working_folder = path.split("\\")[-1]
    print_tab(working_folder, tab_depth)
    for element in os.listdir(path):
        if not is_directory(os.path.join(path, element)):
            print_tab(element, tab_depth+1)
        else:
            directory_structure(os.path.join(path, element), tab_depth + 1)


if __name__ == '__main__':
    directory_structure()
