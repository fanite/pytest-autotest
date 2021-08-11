import os
import pytest
import logging as log
from appium import webdriver
from autotest.by import By
from autotest import webdriver
from .custom import Custom
from typing import TypeVar, Union

T = TypeVar("T", bound=Union[webdriver.Remote,Custom])

img_path = os.path.join(os.getcwd(), "asserts/test.png")

def test_one(caplog):
    log.info("asdsaddd")

def test_two(device: "T"):
    device.activate_app("com.android.settings")

def test_three(device: "T"):
    device.save_screenshot(img_path, (0,886,1080,1086))


if __name__ == "__main__":
    pytest.main(["-s","-v"])
