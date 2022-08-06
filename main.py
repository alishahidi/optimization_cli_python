#!/usr/bin/env python3

import fire
from termcolor import colored

import modules.compress, modules.directory

def banner():
    banner_text = """╔═╗┌─┐┌┬┐┬┌┬┐┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌  ┌─┐┬  ┬
║ ║├─┘ │ │││││┌─┘├─┤ │ ││ ││││  │  │  │
╚═╝┴   ┴ ┴┴ ┴┴└─┘┴ ┴ ┴ ┴└─┘┘└┘  └─┘┴─┘┴"""
    print(colored(f"\n{banner_text}\n", "magenta", attrs=["bold", "blink"]))

banner()


def optimization(directory, out_directory, quality, start_point = None, min_size = None, include_all = '0'):
    files = modules.directory.get_files(directory)
    include_all = bool(int(str(include_all).replace('y', '1').replace('Y', '1').replace('n', '0').replace('N', '0')))
    if(start_point):
        start_point = int(start_point)
        for file_name in files:
            modules.compress.compress_jpg(out_directory, modules.directory.get_absolute_path(file_name, directory), int(quality), start_point, min_size, include_all)
            start_point += 1
    else:
        for file_name in files:
            modules.compress.compress_jpg(out_directory, modules.directory.get_absolute_path(file_name, directory), int(quality), file_name.split(".")[0], min_size, include_all)

if __name__ == '__main__':
  fire.Fire({
      'opt': optimization,
  })
