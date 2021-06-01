#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
  name='androidlib',
  version='0.1.0',
  scripts=['bin/androidctl'],
  description='manages android sdk installation and its packages',
  long_description='manages android sdk installation and its packages',
  author='AeroGear',
  author_email='aerogear-dev@lists.jboss.org',
  url='https://github.com/aerogear/androidctl',
  license='',
  classifiers=[
    'License :: OSI Approved :: Apache Software License',
    'Environment :: Console',
    'Topic :: Software Development :: Build Tools'
  ],
  data_files=[('androidlib/config', ['config/default.cfg'])],
  packages=find_packages(),
  install_requires=[
    'requests==2.18.3',
    'urllib3==1.26.5',
    'pyOpenSSL==17.2.0',
    'cryptography==2.0.3',
    'idna==2.5',
    'certifi==2017.7.27.1'
  ],
  setup_requires=['pytest-runner'],
  tests_require=['pytest', 'pytest-sugar']
)
