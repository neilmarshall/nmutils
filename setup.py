import os
from setuptools import setup, find_packages
from Cython.Build import cythonize

with open('README.md') as f:
    long_description = f.read()

def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

init = os.path.join(os.path.dirname(__file__), 'nmutils', '__init__.py')

version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]

VERSION = get_version(eval(version_line.split('=')[-1]))

setup(
    name="nmutils",
    version=VERSION,
    author="Neil Marshall",
    author_email="neil.marshall@dunelm.org.uk",
    description=("A collection of mathematical utilities, primarily to help with "
        "repetitive elements of solving problems hosted at Project Euler"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/neilmarshall/nmutils.git",
    packages=find_packages(),
    install_requires="Cython>=0.29",
    ext_modules=cythonize("nmutils/*.pyx")
)
