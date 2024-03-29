from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='simplestack',
   version='1.0',
   description='Simple stack for data science operations',
   license="MIT",
   long_description=long_description,
   author='Caleb Kennedy',
   author_email='caleb@stonearchscientific.com',
   url="https://github.com/stonearchscientific/simplestack",
   packages=find_packages(),  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   py_modules=['event', 'java'] 
)
