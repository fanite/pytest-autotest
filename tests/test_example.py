import os
import pytest
import logging as log
from custom import Custom
from autotest import webdriver
from typing import TypeVar, Union

T = TypeVar("T", bound=Union[webdriver.Remote,Custom])

img_path = os.path.join(os.getcwd(), "asserts/test.png")

# def test_one(caplog):
#     log.info("asdsaddd")

# def test_two(device: "T"):
#     pass

def test_three(device: "T"):
    device.activate_app("com.android.settings")
    device.sleep(3)
    # device.save_screenshot(img_path, (0,886,1080,1086))
    device.find_element_by_image(img_path, rgb=True).click()

if __name__ == "__main__":
    pytest.main(["-s","-v"])
