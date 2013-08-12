# coding=utf-8
#
# pyb_init - pybuilder project initialization
#
# Copyright (C) 2013 Maximilien Riehl <maximilien.riehl@gmail.com>
#
#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

from pybuilder.core import use_plugin, init, Author

use_plugin('python.core')
use_plugin('python.install_dependencies')

use_plugin('filter_resources')
use_plugin('copy_resources')

use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.pydev')

authors = [Author('Maximilien Riehl', 'maximilien.riehl@gmail.com')]
license = 'WTFPL'
name = 'pyb_init'
url = 'https://github.com/mriehl/pyb_init'
summary = 'pybuilder project initialization'
version = '0.2.2'

default_task = ['analyze', 'publish']


@init
def set_properties(project):
    project.depends_on('docopt')

    project.build_depends_on('mockito')
    project.build_depends_on('mock')

    project.get_property('filter_resources_glob').append(
        '**/pyb_init/__init__.py')
    project.set_property('copy_resources_target', '$dir_dist')
    project.get_property('copy_resources_glob').append('README')

    project.set_property('coverage_break_build', True)
    project.set_property('distutils_classifiers', [
                         'Development Status :: 4 - Beta',
                         'Intended Audience :: Developers',
                         'License :: Freely Distributable',
                         'Programming Language :: Python',
                         'Natural Language :: English',
                         'Operating System :: Unix',
                         'Topic :: Software Development :: Build Tools'])
