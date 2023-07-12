import os
import shutil
from logging_handler import logger
from wit_exception import WitException


class FileHandler:


    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @staticmethod
    def is_wit_exist_in_path(path):
        return ".wit" in os.listdir(path)

    @staticmethod
    def get_source_path(path):
        full_path = os.path.join(os.getcwd(), path)
        if not os.path.exists(full_path):
            raise WitException
        return full_path

    @classmethod
    def copy_items(cls, origin, target):
        if not os.path.isfile(origin):
            shutil.copytree(origin, os.path.join(target, origin.split("\\")[-1]), dirs_exist_ok=True)
        else:
            shutil.copy2(origin, target)
