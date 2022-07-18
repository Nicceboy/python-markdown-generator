from setuptools import setup

setup(name='markdowngenerator',
      version='0.1',
      description='Python library for dynamically generating HTML sanitized Markdown syntax.',
      long_description=open('README.md').read(),
      url='https://github.com/Nicceboy/python-markdown-generator',
      author='Niklas Saari',
      author_email='niklas.saari@oulu.fi',
      license='Apache-2.0',
      packages=['markdowngenerator', 'markdowngenerator.config'],
      zip_safe=False)
