from batch_geocoder import __version__
from setuptools import setup

long_description = ''
with open('./README.md') as f:
    long_description = f.read()

setup(name='batch_geocoder',
    version=__version__,
    description='Python package of helpers, wrappers, and custom modules for geocoding location data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/christopherpryer/python-geocoder',
    author='Chris Pryer',
    author_email='christophpryer@gmail.com',
    license='PUBLIC',
    packages=['batch_geocoder'],
    zip_safe=False)
