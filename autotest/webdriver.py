import cv2
import time
import aircv
import logging
import numpy as np
from typing import Optional, Union
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

    def save_screenshot(self,
                        filename,
                        rect: Optional["tuple"] = None) -> "bool":
        if not rect:
            return super().save_screenshot(filename)
        x1, y1, x2, y2 = rect
        image = cv2.imdecode(
            np.frombuffer(self.get_screenshot_as_png(), np.uint8),
            cv2.IMREAD_COLOR)
        return cv2.imwrite(filename, image[y1:y2, x1:x2])

    def find_element_by_image(self,
                              img_path: str,
                              cvt: "bool" = False) -> 'WebElement':
        try:
            return super().find_element_by_image(img_path)
        except:
            target = cv2.imread(img_path)
            template = cv2.imdecode(
                np.frombuffer(self.get_screenshot_as_png(), np.uint8),
                cv2.IMREAD_COLOR)
            if cvt:
                target = cv2.cvtColor(target)
                template = cv2.cvtColor(template)
            coor = aircv.find(target, template)
            print(coor)