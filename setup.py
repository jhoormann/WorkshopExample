from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/jhoormann/WorkshopExample',
      author='Janie Hoormann',
      author_email='janie@hoormann.org',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
