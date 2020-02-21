from setuptools import find_packages
from setuptools import setup

setup(
    name="omnitradeClient",
    version="0.2",
    license="MIT license",
    description="Python client for Omnitrade API",
    author="Omnitrade",
    author_email="@codeminer42.com",
    url="https://github.com/OmniTrade/client-py",
    packages=find_packages("src"),
    package_dir={"": "src/"},
    include_package_data=True,
    zip_safe=False,
    keywords=["omnitrade", "api"],
    install_requires=open("requirements.txt").readlines(),
    extras_require={}
)
