import inspect
from os import path
from time import strftime
from _pytest.config import Config
from _pytest.fixtures import fixture
from _pytest.pathlib import import_path
from autotest import webdriver


def logging_settings(config):
    log_format = "%(asctime)s %(levelname)-8s %(filename)s::%(module)s::%(funcName)s <%(lineno)4d>: %(message)s"
    log_date_format = "%Y-%m-%d %H:%M:%S"
    if not config.getoption("log_format"):
        setattr(config.option, "log_format", log_format)
    if not config.getoption("log_date_format"):
        setattr(config.option, "log_date_format", log_date_format)
    if not config.getoption("log_file_format"):
        setattr(config.option, "log_file_format", log_format)
    if not config.getoption("log_file_date_format"):
        setattr(config.option, "log_file_date_format", log_date_format)
    log_file = config.getini("log_file")
    if log_file:
        log_file = path.normpath(log_file)
        root, ext = path.splitext(log_file)
        if ext == "":
            current_time = strftime("%Y-%m-%d-%H%M%S")
            logs_path = path.join(log_file, f"{current_time}.log")
        else:
            logs_path = log_file
        setattr(config.option, "log_file", logs_path)

def get_class(pypath):
    pyfile = path.join(pypath, "custom.py")
    if not path.isfile(pyfile):
        return webdriver.Remote
    pymodule = import_path(pyfile)
    pyclasses = [pyclass for name, pyclass in inspect.getmembers(
        pymodule, lambda x: inspect.isclass(x) and x.__base__ == webdriver.Remote.__base__)]
    pyclasses.insert(0, webdriver.Remote)
    return type("Remote", tuple(pyclasses), {})

def pytest_configure(config: Config):
    logging_settings(config)

@fixture(scope="session")
def device(pytestconfig, request):
    Remote = get_class(pytestconfig.rootpath)
    desired_caps = dict(
        platformName='Android',
        deviceName='Android Emulator'
    )
    device = Remote('http://localhost:4723/wd/hub', desired_caps)
    yield device
    request.addfinalizer(lambda: device.quit())
