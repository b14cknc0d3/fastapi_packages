try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='packages',
    version='1.0.1',
    author='Ye Lin Aung',
    author_email='b14cknc0d3@gmail.com',
    packages=[
        'auth',
        'database',
    ],
    requires=[
        'SQLAlchemy~=2.0.28',
        'passlib~=1.7.4',
        'python-jose~=3.3.0',
        'setuptools~=69.0.3'
    ],
)
