from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MyManJeeves',
    version='0.1',
    description='A discord bot',
    long_description=readme,
    author='Pontus Johansson, Jonatan Davidsson',
    install_requires=requirements,
    author_email='pontus.johansson@falun.ntig.se, jonatan.davidsson@falun.ntig.se',
    url='https://github.com/havokoc/MyManJeeves',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
