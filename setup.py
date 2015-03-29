from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import os
import website


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'README.rst')) as readme:
    README = readme.read()


def readlines(filename):
    with file(os.path.join(BASE_DIR, filename), 'r') as f:
        return f.readlines()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='website',
    version=website.__version__,
    tests_require=['pytest', 'django', 'pytest-django'],
    cmdclass={'test': PyTest},
    packages=['website'],
    url='https://github.com/brady-vitrano/website',
    install_requires=readlines('requirements.txt'),
    platforms=['any'],
    license='MIT',
    author='brady-vitrano',
    author_email='bjvitrano@gmail.com',
    description='Django website for testing purposes',
    long_description=README,
    include_package_data=True,
    extras_require={
        'testing': ['pytest'],
    },
    zip_safe=False
)