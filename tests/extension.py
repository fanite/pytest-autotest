from selenium import webdriver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from appium import webdriver

class Extension(webdriver.Remote):
    def say_byebye(self):
        print("bye bye")