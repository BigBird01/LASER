import subprocess
import datetime
import sys

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('setuptools')
install('gitpython')

import setuptools
import git

repo = git.Repo(search_parent_directories=True)
date=datetime.datetime.utcnow()

with open("README.md", "r") as fh:
  long_description = fh.read() + f'\n git version: {repo.head.object.hexsha}' + \
  f'\n date: {date}'

with open('VERSION') as fs:
    version = fs.readline().strip()
#    version += f".dev{date.strftime('%y%m%d%H%M%S')}"

with open('requirements.txt') as fs:
    requirements = [l.strip() for l in fs if not l.strip().startswith('#')]

extras = {}
extras["docs"] = ["recommonmark", "sphinx", "sphinx-markdown-tables", "sphinx-rtd-theme"]

setuptools.setup(
    name="LASER",
    version=version,
    author="Pengcheng He",
    author_email="penhe@microsoft.com",
    description="A toolkit for large scale distributed training",
    keywords="Distributed deep learning",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BigBird01/LASER",
    packages=setuptools.find_packages(where='src', exclude=['__pycache__']),
    package_dir = {'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require=extras,
    install_requires=requirements)
