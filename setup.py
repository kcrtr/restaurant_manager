from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in restaurant_manager/__init__.py
from restaurant_manager import __version__ as version

setup(
	name="restaurant_manager",
	version=version,
	description="Restaurant Manager App for ERPNext",
	author="ByteBot Tech",
	author_email="opensource@bytebottech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
