import os.path
from pathlib import Path

class PathsManager:

    @staticmethod
    def get_root_absolute_path():
        return Path(os.path.dirname(__file__)).parent.parent

    @staticmethod
    def get_subdirectory_path(dir_name):
        return os.path.join(PathsManager.get_root_absolute_path(), dir_name)

    @staticmethod
    def get_filename(parent_dir_name, filename, extension):
        return os.path.join(parent_dir_name, filename + "." + extension)