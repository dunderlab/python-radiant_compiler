import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='radiant-compiler',
    version='0.1a1',
    packages=['radiant.compiler'],
    author='Yeison Cardona',
    author_email='yencardonaal@unal.edu.co',
    maintainer='Yeison Cardona',
    maintainer_email='yencardonaal@unal.edu.co',
    download_url='https://github.com/dunderlab/python-radiant.compiler',
    install_requires=[
        'python-for-android',
        'cython',
    ],
    scripts=[
       "cmd/radiant_p4a",
    ],
    include_package_data=True,
    license='BSD-2-Clause',
    description="Brython Framework",
    long_description=README,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
    ],
)

