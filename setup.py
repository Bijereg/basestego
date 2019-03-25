from setuptools import setup, find_packages
import basestego

setup(name='basestego',
      version=basestego.__version__,
      description='Steganography with base64',
      author=basestego.__author__,
      author_email='bijereg@gmail.com',
      packages=find_packages(),
      python_requires='>=3.6',
      test_suite='tests')
