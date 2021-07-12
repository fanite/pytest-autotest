from appium import webdriver

class Custom(webdriver.Remote):
    def say_byebye(self):
        print("bye bye")