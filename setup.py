import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-shorturls",
    version = "2.0.1",
    url = 'https://github.com/bfirsh/django-shorturls',
    license = 'BSD',
    description = "A URL shortening app for Django.",
    long_description = read('README.rst'),

    author = 'Simon Willison, Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools', 'six'],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
