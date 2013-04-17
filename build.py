# coding=utf-8
from pybuilder.core import use_plugin, init, Author

use_plugin('python.core')
use_plugin('python.install_dependencies')

use_plugin('filter_resources')

use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.pydev')

authors = [Author('Maximilien Riehl', 'maximilien.riehl@gmail.com')]
license = 'WTFPL'
name = 'pyb_init'
url = 'https://github.com/mriehl/pyb_init'
version = '0.0.1'

default_task = ['analyze', 'publish']


@init
def set_properties(project):
    project.depends_on('docopt')

    project.get_property('filter_resources_glob').append('**/pyb_init/__init__.py')
    project.set_property('copy_resources_target', '$dir_dist')
    project.set_property('coverage_break_build', False)

