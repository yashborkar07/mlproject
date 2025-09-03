from setuptools import find_packages,setup

setup(
    name="mlproject",
    version="0.01",
    author="yash",
    author_email="yashborkar07@gmail.com",
    packages=find_packages(),
    install_requires=["pandas","numpy","seaborn"]
)