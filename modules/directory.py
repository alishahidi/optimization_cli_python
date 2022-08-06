import os

def get_files(path):
    valid_extensions = ['jpg','jpeg']
    file_names = [fn for fn in os.listdir(path)
                if any(fn.endswith(ext) for ext in valid_extensions)]
    return file_names

def get_absolute_path(file_name, directory):
    return os.path.abspath(os.path.join(directory, file_name))
