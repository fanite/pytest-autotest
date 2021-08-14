import cv2
import time
import aircv
import logging
import numpy as np
from appium import webdriver
from os.path import basename
from collections import ChainMap
from typing import Optional, Union
from appium.webdriver.common.mobileby import MobileBy


def find_all(im_source, im_search, **kwargs):
    '''
    优先Template，之后Sift
    @ return [(x,y), ...]
    '''
    kwargs = ChainMap(kwargs, {"threshold": 0.8, "maxcnt": 0})
    result = aircv.find_all_template(im_source, im_search, **kwargs)
    if not result:
        result = aircv.find_all_sift(im_source,
                                     im_search,
                                     maxcnt=kwargs["maxcnt"])
    if not result:
        return []
    return [match["result"] for match in result]


def find(im_source, im_search, **kwargs):
    '''
    Only find maximum one object
    '''
    kwargs = ChainMap(kwargs, {"maxcnt": 1})
    r = find_all(im_source, im_search, **kwargs)
    return r[0] if r else None


class By(MobileBy):
    """By Operator"""


class WebElement(webdriver.WebElement):
    pass


class CoordElement(object):
    def __init__(self, driver: "Remote", coord: "tuple") -> None:
        super().__init__()
        self.driver = driver
        self.coord = coord

    def click(self):
        self.driver.tap([self.coord])


class Remote(webdriver.Remote):
    def sleep(self, secs: Union["int", "float"]):
        logging.info(f"waiting {secs} seconds...")
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

    def find_element_by_image(
            self,
            img_path: str,
            rgb: "bool" = False) -> Union["WebElement", "CoordElement"]:
        logging.info(f"find picture {basename(img_path)} in screen.")
        try:
            return super().find_element_by_image(img_path)
        except:
            im_search = cv2.imread(img_path)
            im_source = cv2.imdecode(
                np.frombuffer(self.get_screenshot_as_png(), np.uint8),
                cv2.IMREAD_COLOR)
            coord = find(im_source, im_search, rgb=rgb)
            if not coord:
                raise RuntimeError(
                    f"the picture {basename(img_path)} is not found in screen."
                )
            return CoordElement(self, coord)
