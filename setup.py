try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='packages',
    version='1.0.0',
    packages=[
        'auth',
        'database',
    ],
)
