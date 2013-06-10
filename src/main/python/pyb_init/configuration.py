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

configuration = {}


def set_configuration(virtualenv_name,
                      virtualenv_use_system_site_packages=False,
                      python_interpreter=None):
    configuration['virtualenv_name'] = virtualenv_name
    configuration['virtualenv_use_system_site_packages'] = virtualenv_use_system_site_packages
    configuration['virtualenv_path_to_python_interpreter'] = python_interpreter
