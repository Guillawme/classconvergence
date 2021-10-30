from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
    readme = f.read()

setup(
    name = 'classconvergence',
    version = '1.2',

    description = 'Plot the class distribution as a function of iteration from a Class2D or Class3D job from RELION',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Guillawme/classconvergence',

    author = 'Guillaume Gaullier',
    author_email = 'contact@gaullier.org',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Natural Language :: English'
    ],
    keywords = 'cryo-EM class distribution plot visualization',

    py_modules = ["classconvergence"],

    python_requires = '>=3.9.7',
    install_requires = [
        'click>=8.0.3',
        'matplotlib>=3.4.3',
        'starfile>=0.4.9'
    ],

    entry_points = {
        'console_scripts': [
            'classconvergence=classconvergence:cli'
        ]
    },

    project_urls = {
        'Bug Reports': 'https://github.com/Guillawme/classconvergence/issues',
        'Source': 'https://github.com/Guillawme/classconvergence'
    }
)
