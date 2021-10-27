import os

from setuptools import find_packages, setup

# reading requirements from requirements.txt
INSTALL_REQUIRES = []
dpath = os.path.dirname(os.path.realpath(__file__))
fpath = os.path.join(dpath, 'requirements.txt')
with open(fpath, 'r') as f:
    for line in f:
        INSTALL_REQUIRES.append(line.replace('\n', ''))


setup(
    name='titanic',
    packages=find_packages(),
    version='0.1.0',
    description='Dev repo example',
    author='LidiyaNorman',
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': INSTALL_REQUIRES,
    },
)