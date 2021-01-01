from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as ver:
    version_info = ver.read().strip()

setup(name='python-markdown-generator',
      version=version_info,
      description='Python library for dynamically generating HTML sanitized Markdown syntax.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Nicceboy/python-markdown-generator',
      author='Niklas Saari',
      author_email='niklas.saari@oulu.fi',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
