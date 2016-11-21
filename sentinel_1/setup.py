from distutils.core import setup

setup(
    name='Doris_5.0',
    version='1.2.0',
    packages=['sentinel_1', 'sentinel_1.functions', 'sentinel_1.main_code'],
    url='',
    license='',
    author='Gert Mulder',
    author_email='g.mulder-1@tudelft.nl',
    description='Doris 5.0',

    install_requires=['numpy, datetime, requests, os, sys, numpy, shapely, fiona', 'gdal', 'osr', 'xml']
)
