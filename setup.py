from setuptools import setup

setup(
    name='keggutil',
    version='0.1.0',
    description='Utility package for KEGG pathway database',
    author='Kozo Nishida',
    author_email='knishida@riken.jp',
    url='http://github.com/kozo2/keggutil',
    keywords=['KEGG', 'bioinformatics'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['keggutil'],
    extras_requires=[
        'requests',
        'pandas',
    ],
)
