import os
import click
from file_handler import FileHandler
from pathlib import Path
from logging_handler import logger
from wit_exception import WitException


class Wit:
    base_path = None
    working_directory = None
    @staticmethod
    def validate_is_wit_repo():
        path = os.getcwd()
        path = Path(path).resolve()
        root = Path("\\").resolve()
        FileHandler.working_directory = str(path).split("\\")[-1]
        while path != root:
            if FileHandler.is_wit_exist_in_path(path):
                Wit.base_path = path
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
            logger.info(f"init wit in {os.getcwd()}")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(Wit.base_path, ".wit\\staging_area")
        # A list containing the folder names in the path of the item to be added
        dirs = full_path[len(str(Wit.base_path))::]
        dirs = dirs.split("\\")
        for item in dirs[:-1]:
            target_path = os.path.join(target_path, item)
            # if the folder (item) not exists we will create the dir
            if not os.path.exists(target_path):
                os.mkdir(target_path)
        # When we have reached the lowest layer,
        # only then will we copy the requested files to the path we chained
        FileHandler.copy_items(full_path, target_path)

    @staticmethod
    def add(arg):
        if Wit.validate_is_wit_repo():
            try:
                full_path = FileHandler.get_source_path(arg)
                Wit.move_to_staging(full_path)
                logger.info(f"{arg} was successfully added to staging_area")
            except WitException:
                click.secho('file is not exist', fg="red", bold=True)
                logger.error("Attempt to add a file that does not exist")
        else:
            click.secho('Wit is not exist', fg="red", bold=True)
            logger.error("Try to do Wit command without init wit")

    @staticmethod
    def commit(msg):
        if Wit.validate_is_wit_repo():
            pass
