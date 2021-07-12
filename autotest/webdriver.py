import time
import logging
from typing import Union
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class By(MobileBy):
    """By Operator"""

class WebElement(webdriver.WebElement):
    pass

class Remote(webdriver.Remote):
    def sleep(self, secs: Union["int", "float"]):
        logging.info(f"等待 {secs} 秒...")
        time.sleep(secs)
