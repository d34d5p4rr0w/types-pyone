from setuptools import setup

setup(
    name='types-pyone',
    version='0.1.2',
    description='Type stubs for pyone library',
    packages=['pyone'],
    package_data={'pyone': ['*.pyi'], 'pyone/bindings': ['*.pyi'], 'pyone': ['py.typed']},
    install_requires=[
        'pyone',
        'typing-extensions',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Typing :: Stubs Only'
    ],
)

