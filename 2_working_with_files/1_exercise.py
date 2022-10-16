import os.path


def count_files(path: str = "dev") -> int:
    """first arg - specify path, if not /dev will be taken"""
    directory_structure = os.listdir(path)
    return len([file for file in directory_structure if os.path.isfile(f"{path}/{file}")])


print(f"There are {count_files()} files")

