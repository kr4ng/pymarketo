import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pymarketo'))
from version import VERSION

long_description = '''
pymarketo is a python query client that wraps the Marketo SOAP API.
For sending data to Marketo, check out developers.marketo.com for more
information.
'''

setup(
    name='marketo',
    version=VERSION,
    url='https://github.com/kr4ng/pymarketo',
    author='Steven Simoni',
    author_email='steven@rightstack.io',
    maintainer='rightstack.io',
    maintainer_email='steven@rightstack.io',
    packages=['pymarketo'],
    license='MIT License',
    install_requires=[
        'requests',
        'iso8601'
    ],
    description='pymarketo is a python query client that wraps the Marketo SOAP API.',
    long_description=long_description
)