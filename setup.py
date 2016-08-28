# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'django-slack-invitation'
VERSION = '0.1.0'


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


def requirements():
    return readlist('requirements.txt')


def requirements_test():
    if sys.version_info < (3, 0):
        return ['mock']
    return []

setup(
    name=NAME,
    version=VERSION,
    description='API client for Beddit sleep tracker',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework:: Django',
        'Framework:: Django:: 1.10',
        'Framework:: Django:: 1.7',
        'Framework:: Django:: 1.8',
        'Framework:: Django:: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django slack invitation plugin',
    author='giginet',
    author_email='giginet.net@gmail.com',
    url='https://github.com/giginet/%s' % NAME,
    download_url='https://github.com/giginet/%s/tarball/master' % NAME,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['README.rst',
             'LICENSE.rst',
             'requirements.txt'],
    },
    zip_safe=True,
    install_requires=requirements(),
    test_suite='runtests.run_tests',
    tests_require=requirements_test(),
)
