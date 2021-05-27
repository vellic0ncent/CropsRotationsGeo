from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# long_description = (here / 'README.md').read_text(encoding='utf-8')

# with open("README",'r') as f:
#     long_description = f.read()

setup(
    name='Project',
    version='2.0',
    description='Crop Rotation Modelling',
    # long_description=detailed_description,
    author='3&Ps',
    package_dir={'': 'ClassifierCrops'},
    packages=find_packages(where='ClassifierCrops'),
    # python_requires '>=3.6, <4',
    install_requires=['', '', ''],
    entry_points={
        'console_scripts': [
            'src=src:main',
        ],
    },
)
