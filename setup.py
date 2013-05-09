from setuptools import setup, find_packages
from os import path


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='jython-sikuli-server',
    include_package_data = True,
    package_data = {'':['*.md']},
    author='Alistair Broomhead',
    version='0.1.8',
    author_email='alistair.broomhead@gmail.com',
    description='Jython script to run a robot remote library exposing the Sikuli API (and popen).',
    license='MIT',
    url='https://github.com/alistair-broomhead/jython-sikuli-server',
    download_url='https://github.com/alistair-broomhead/jython-sikuli-server/zipball/master',
    long_description=read('README.md'),
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    install_requires=[]
)
