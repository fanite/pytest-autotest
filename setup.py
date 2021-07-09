from os.path import dirname, join
from setuptools import setup, find_packages


def read_file(fileName: str):
    """
    read document
    """
    with open(join(dirname(__file__), fileName), 'r', encoding='utf-8') as fh:
        if fh.readable:
            return fh.read()


setup(
    version='0.0.1',
    name='autotest',
    packages=find_packages(),
    author='fanite',
    author_email='fanite@qq.com',
    license='MIT',
    url='https://github.com/fanite/pytest-autotest',
    description='This fixture provides a configured "driver" for Android Automated Testing, using uiautomator2.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    python_requires='~=3.7',
    install_requires=read_file('requirements.txt').splitlines(),
    entry_points={
        'pytest11': [
            'pytest-autotest = autotest.plugin',
        ],
    },
)
