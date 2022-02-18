from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup
(
    name='DataScience-x-Logistic-Regression',
    version='1.0',
    description=readme,
    author='dgiannop',
    author_email='dgiannop@student.codam.nl',
    url='https://github.com/danali262/DataScience-x-Logistic-Regression',
    license='MIT',
    packages=find_packages()
)
