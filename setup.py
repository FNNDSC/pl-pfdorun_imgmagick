from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'pfdorun_imgmagick',
    version          = '1.0.1',
    description      = 'An app to recursively walk down a directory tree and run a CLI program from imagemagick',
    long_description = readme,
    author           = 'Arushi Vyas',
    author_email     = 'dev@babyMRI.org',
    url              = 'https://github.com/FNNDSC/pl-pfdorun_imgmagick',
    packages         = ['pfdorun_imgmagick'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'pfdorun_imgmagick = pfdorun_imgmagick.__main__:main'
            ]
        }
)
