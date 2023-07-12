import os
import secrets

from wit import Wit


class Commit:
    path = None
    commit_id = None
    @staticmethod
    def create_commit_dir():
        commit_id = secrets.token_hex(20)
        path = os.path.join(Wit.base_path, f'.wit/images/{commit_id}')
        os.mkdir(path)

    @staticmethod
    def create_commit_data_file():
        pass
