from pip.req import parse_requirements
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirement
requires = [str(ir.req) for ir in install_reqs]


setup(
    name='ssmais',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL 3.0',
    description='SSMais is a Django application that aims to perform reservation management of a service over the Web.',
    long_description=README.md,
    url='https://github.com/Software-Design-2017/SSMais',
    author='Mais Software Inc.',
    author_email=' maissoftwareinc@gmail.com',
    install_requires=requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL 3.0',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
