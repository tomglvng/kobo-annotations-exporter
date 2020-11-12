import os.path


def check_file_exists(file_name) -> str:
    if os.path.isfile(file_name):
        return file_name
    else:
        raise FileNotFoundError(file_name)


def check_folder_exists(directory_name) -> str:
    if os.path.isdir(directory_name):
        return directory_name
    else:
        raise NotADirectoryError(directory_name)
