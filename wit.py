import os

import click

from file_handler import FileHandler
from pathlib import PurePosixPath, Path
import shutil


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        path = os.getcwd()
        path = Path(path).resolve()
        root = Path("\\").resolve()
        print(str(path).split("\\")[-1])
        FileHandler.working_directory = str(path).split("\\")[-1]
        while path != root:
            if FileHandler.is_wit_exist_in_path(path):
                FileHandler.base_path = path
                return True
            path = path.parent
        return False

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            click.secho('Wit already exist', fg="red", bold=True)
        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, ".wit\\staging_area")
        for root, dirs, files in os.walk(".", topdown=True):

            for name in files:
                if name == full_path.split("\\")[-1]:

                    print("file: ", os.path.join(root, name))
            for name in dirs:
                print("folder", os.path.join(root, name))
        FileHandler.copy_items(full_path, target_path)

    @staticmethod
    def add(arg):
        if Wit.validate_is_wit_repo():
            print("base path", FileHandler.base_path)
            full_path = FileHandler.get_source_path(arg)
            Wit.move_to_staging(full_path)
            # try:
            #     full_path = FileHandler.get_source_path(arg)
            #     Wit.move_to_staging(full_path)
            # except:
            #     click.secho('file is not exist', fg="red", bold=True)
        else:
            click.secho('Wit is not exist', fg="red", bold=True)

    @staticmethod
    def commit():
        pass
