import time
import logging
from typing import Union
from selenium import webdriver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from appium import webdriver

class Common(webdriver.Remote):
    def sleep(self, secs: Union[int, float]):
        logging.info(f"等待 {secs} 秒...")
        time.sleep(secs)