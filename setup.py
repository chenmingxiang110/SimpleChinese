#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas>=1.0.0',
                'jieba>=0.42.1',
                'numpy>=1.18.1',
                'scikit-learn>=0.22.1',
                'matplotlib>=3.1.2',
                'wordcloud>=1.7.0']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Mingxiang Chen",
    author_email='chenmingxiang110@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Chinese text processing, representation, and visualization.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='simplechinese',
    name='simplechinese',
    packages=find_packages(include=['simplechinese', 'simplechinese.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chenmingxiang110/simplechinese',
    version='0.1.0',
    zip_safe=False,
)
