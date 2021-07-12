import pytest
import logging as log
from appium import webdriver
from autotest.by import By
from autotest import webdriver
from .custom import Custom
from typing import TypeVar, Union

T = TypeVar("T", bound=Union[webdriver.Remote,Custom])

def test_one(caplog):
    raise Exception("sssssssssssssss")

def test_two(device: "T"):
    device.activate_app("com.android.settings")

def test_three(device: "T"):
    searchbar = device.find_element(By.ID, "com.android.settings:id/search_action_bar")
    searchbar.click()
    device.sleep(2)
    device.tap([(93, 146)])


if __name__ == "__main__":
    pytest.main(["-s","-v"])
