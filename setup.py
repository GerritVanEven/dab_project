from setuptools import find_packages, setup

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains the code in the src directory of the project",
    author="Gerrit Van Even",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
)
