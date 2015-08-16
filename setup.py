import os
from setuptools import setup
from setuptools import find_packages

VERSION = '1.0dev'

requires = [
    'docopt',
    'ndg-httpsclient',
    'pyasn1',
    'pyopenssl',
    'requests',
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

setup(name='acidfs',
      version=VERSION,
      description='Library for building Ansible dynamic inventories for '
                  'Digital Ocean.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: Repoze Public License",
        ],
      author="Chris Rossi",
      author_email="chris@armchimedeanco.com",
      url="http://github.com/chrisrossi/droplets",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires)
