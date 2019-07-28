from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="nmutils",
    version="0.0.1",
    author="Neil Marshall",
    author_email="neil.marshall@dunelm.org.uk",
    description=("A collection of mathematical utilities, primarily to help with"
        "repetitive elements of solving problems hosted at Project Euler"),
    url="https://github.com/neilmarshall/nmutils.git",
    packages=find_packages(),
    install_requires="Cython",
    ext_modules=cythonize("nmutils/*.pyx"),
    exclude=["tests", "venv"]
)

