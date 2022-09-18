'''
Author       : Thyssen Wen
Date         : 2022-09-18 09:06:20
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-18 09:12:58
Description  : file content
FilePath     : /DLAN/setup.py
'''
from setuptools import setup

package_name = 'DLAN'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thyssen',
    maintainer_email='Thinksky5124@outlook.com',
    description='A rich, leading and practical library of deep learning automatic navigation ROS package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
