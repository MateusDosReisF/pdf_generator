from setuptools import setup, find_packages

setup(
    name='pdf_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'reportlab',
    ],
    description='A simple PDF generation library',
    author='Mateus Reis',
    author_email='mateussgp12@gmail.com',
    url='https://github.com/mateusdosreisf/pdf_generator',
)
