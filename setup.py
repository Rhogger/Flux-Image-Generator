from setuptools import setup

setup(
    name='Flux-Image-Generator',
    version='1.0',
    description='A Langflow component that generates images from text using Flux.dev.',
    author='Rhogger',
    author_email='rhoggerrv@gmail.com',
    packages=['Generators'],
    install_requires=[
        'requests',
        'langflow',
    ],
)
