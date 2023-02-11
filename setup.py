import os
from setuptools import setup, find_packages
from distutils.core import setup, Extension
from distutils import sysconfig
from Cython.Distutils import build_ext

with open('README.rst', 'r') as fh:
    long_description = fh.read()

quiclib = Extension(
    'quiclib', sources=['./graphem/QUIC.cpp'],
    extra_link_args=['-llapack', '-lblas', '-lstdc++', '-fPIC'],
)

class NoSuffixBuilder(build_ext):
    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        suffix = sysconfig.get_config_var('EXT_SUFFIX')
        ext = os.path.splitext(filename)[1]
        return os.path.join('./graphem', filename.replace(suffix, "")+ext)

setup(
    name='cfr-graphem',
    version='0.2.1',
    description='The GraphEM component for CFR',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Feng Zhu, Julien Emile-Geay',
    author_email='fengzhu@usc.edu, julieneg@usc.edu',
    url='https://github.com/fzhu2e/cfr-graphem',
    packages=find_packages(),
    include_package_data=True,
    license='BSD 3-Clause',
    zip_safe=False,
    cmdclass={'build_ext': NoSuffixBuilder},
    ext_modules=[quiclib],
    keywords='climate field reconstruction',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'cfr',
    ],
)
