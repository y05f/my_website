from setuptools import find_packages, setup

setup(
    name='my_website',
    version='1.0.0',
    description='my personal website built using flask',
    author='Youssef Safi',
    author_email='ysf.safi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)