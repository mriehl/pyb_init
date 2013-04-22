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


def determine_project_name_from_git_url(git_url):
    start_index = git_url.rfind('/') + len('/')

    if git_url.endswith('.git'):
        end_index = len(git_url) - len('.git')
    else:
        end_index = len(git_url)

    return git_url[start_index:end_index]
