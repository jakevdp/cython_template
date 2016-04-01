import os

PACKAGE_NAME = 'cython_template'


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(PACKAGE_NAME, parent_package, top_path)

    config.add_subpackage('__check_build')
    config.add_subpackage('tests')
    config.add_extension('example_code',
                         sources=['example_code.c'])

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
