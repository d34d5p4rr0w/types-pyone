from setuptools import setup

setup(
    name='types-pyone',
    version='0.1.3',
    description='Type stubs for pyone library',
    url='https://github.com/d34d5p4rr0w/types-pyone',

    packages=['pyone'],
    package_data={'pyone': ['*.pyi'], 'pyone': ['py.typed']},
    install_requires=[
        'pyone',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Typing :: Stubs Only'
    ],
)

