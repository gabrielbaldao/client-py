from setuptools import find_packages
from setuptools import setup

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext


setup(
    name="omnitradeClient",
    version="0.1.0",
    license="MIT license",
    description="Python client for Omnitrade API",
    author="Omnitrade",
    author_email="@codeminer42.com",
    url="https://github.com/OmniTrade/client-py",
    packages=find_packages("src"),
    package_dir={"": "src/"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/omnitradeClient/*.py")],
    include_package_data=True,
    zip_safe=False,
    keywords=["omnitrade", "api"],
    install_requires=open("requirements.txt").readlines(),
    extras_require={}
)
