'''
Author       : Thyssen Wen
Date         : 2022-09-18 09:06:20
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-19 07:23:23
Description  : file content
FilePath     : /DLAN/setup.py
'''
from setuptools import setup, find_packages
import sys
import platform
python_min_version = (3, 7, 0)
python_min_version_str = '.'.join(map(str, python_min_version))
if sys.version_info < python_min_version:
    print("You are using Python {}. Python >={} is required.".format(platform.python_version(),
                                                                     python_min_version_str))
    sys.exit(-1)
package_name = 'dlan'

setup(
    name=package_name,
    version='0.0.0',
    packages = find_packages(exclude=('configs', 'tools', 'demo')),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resources/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thyssen',
    maintainer_email='Thinksky5124@outlook.com',
    description='A rich, leading and practical library of deep learning automatic navigation ROS package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=[
        "pytorch >= 1.12.0",
        "pyyaml",
    ],
    package_data={
        'scripts': [".sh"],
    },
    python_requires='>={}'.format(python_min_version_str),
    entry_points={
        'console_scripts': [
            'launch = launch:main',
        ],
    },
)
