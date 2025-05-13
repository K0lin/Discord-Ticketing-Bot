# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import os.path
from pathlib import Path

class PathsManager:

    @staticmethod
    def get_root_absolute_path():
        return Path(os.path.dirname(__file__)).parent

    @staticmethod
    def get_subdirectory_path(dir_name):
        return os.path.join(PathsManager.get_root_absolute_path(), dir_name)

    @staticmethod
    def get_filename(parent_dir_name, filename, extension):
        return os.path.join(PathsManager.get_root_absolute_path(), parent_dir_name, filename + "." + extension)