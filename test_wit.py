from wit import Wit
import pytest
from wit_exception import WitException
from file_handler import FileHandler


def test_validate_is_wit_repo():
    assert not Wit.validate_is_wit_repo()


@pytest.mark.parametrize("path", [
    r"C:\Users\WIN-10\Desktop\מסלול הנדסאים\elevation\project\jo\.wit\staging_area\son\grateson\file_not_exist"])
def test_get_source_path(path):
    with pytest.raises(WitException):
        FileHandler.get_source_path(path)
