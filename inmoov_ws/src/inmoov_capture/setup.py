from setuptools import find_packages, setup

package_name = 'inmoov_capture'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andrew',
    maintainer_email='andrew@rekabuk.co.uk',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    }, 
    entry_points={
        'console_scripts': [
            'inmoov_capture = inmoov_capture.inmoov_capture:main',
            'inmoov_capture_multi = inmoov_capture.inmoov_capture_multi:main',
            'inmoov_capture_replay = inmoov_capture.inmoov_capture_replay:main',
        ],
    },
)
