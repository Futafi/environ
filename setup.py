from setuptools import setup


ENVIRON_VERSION = "0.0.0"
with open("README.md", "r") as f:
    README = f.read()

setup(
    name="environ",
    packages=["environ"],
    version=ENVIRON_VERSION,
    install_requires=[],
    dependency_links=[],
    description="easy but incompetent .env loader",
    long_description=README,
    license="Apache",
    author="Daiki Futagi",
    author_email="D.Futagi@vivaldi.net",
)
