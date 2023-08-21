from setuptools import setup, find_packages

setup(
    name='iot_sb',
    version='0.0.1',
    url='https://github.com/extinctCoder/iot_smartbuilding.git',
    author='extinctCoder',
    author_email='write2shourov@gmail.com',
    description='IOT based smart build control system...:)',
    packages=find_packages(include=['src']),
    install_requires=['dynaconf >= 3.1.11'],
)
