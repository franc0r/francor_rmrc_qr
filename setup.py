from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'francor_rmrc_qr'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='martin',
    maintainer_email='martin.bauernschmitt@francor.de',
    description='Package to log QR codes to file from zbar',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'qr_log = francor_rmrc_qr.qr_log:main'
        ],
    },
)
