import os
from PIL import Image
from termcolor import colored
import shutil

import modules.directory

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def compress_jpg(directory, file_name, quality, new_file_name, min_size = None, include_all = False):
    image_size = os.path.getsize(file_name)
    new_file_name = modules.directory.get_absolute_path(str(new_file_name) + ".jpg", directory)
    if min_size and image_size <= (int(min_size) * 1024):
        if include_all:
            shutil.copyfile(file_name, new_file_name)
        return
    image = Image.open(file_name)
    print(f"[{colored('*', 'blue', attrs=['bold'])}] Openning:", file_name)
    print(f"[{colored('*', 'blue', attrs=['bold'])}] Image shape:", image.size)
    print(f"[{colored('*', 'blue', attrs=['bold'])}] Size:", get_size_format(image_size))
    try:
        image.save(new_file_name, quality=quality, optimize=True)
    except OSError:
        image = image.convert("RGB")
        image.save(new_file_name, quality=quality, optimize=True)
    print(f"\t[{colored('+', 'green', attrs=['bold'])}] New file saved:", new_file_name)
    new_image_size = os.path.getsize(new_file_name)
    # print the new size in a good format
    print(f"\t[{colored('+', 'green', attrs=['bold'])}] New size:", get_size_format(new_image_size))
    # calculate the saving bytes
    saving_diff = new_image_size - image_size
    # print the saving percentage
    print(f"\t[{colored('+', 'green', attrs=['bold'])}] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")
    print(f"\n[{colored('>', 'yellow', attrs=['bold'])}] ################################################################\n")
