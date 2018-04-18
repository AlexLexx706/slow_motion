
from setuptools import setup, find_packages

setup(
    name='slow_motion',
    version='0.1',
    author='alexlexx',
    author_email='alexlexx1@gmail.com',
    packages=find_packages(),
    license='GPL',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'slow_motion = slow_motion:main'],
    },
    package_data={
        'slow_motion': [
            'images/*.*']
    },
)
