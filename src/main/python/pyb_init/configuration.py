# coding=utf-8
configuration = {}


def set_configuration(virtualenv_name, virtualenv_use_system_site_packages=False):
    configuration['virtualenv_name'] = virtualenv_name
    configuration['virtualenv_use_system_site_packages'] = virtualenv_use_system_site_packages
