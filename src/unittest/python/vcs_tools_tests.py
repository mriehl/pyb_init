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

import unittest

from pyb_init.vcs_tools import determine_project_name_from_git_url,\
                               determine_project_name_from_svn_url

class GitUrlToolsTests(unittest.TestCase):

    def test_should_return_project_name_for_git_url_with_git_ending(self):
        actual_project_name = determine_project_name_from_git_url('https://git/test.git')
        self.assertEqual(actual_project_name, 'test')

    def test_should_return_project_name_for_long_git_url_with_git_ending(self):
        actual_project_name = determine_project_name_from_git_url('https://git/foo/bar/test.git')
        self.assertEqual(actual_project_name, 'test')

    def test_should_return_project_name_for_git_url_without_git_ending(self):
        actual_project_name = determine_project_name_from_git_url('https://git/test')
        self.assertEqual(actual_project_name, 'test')

    def test_should_return_project_name_for_git_ssh_url(self):
        actual_project_name = determine_project_name_from_git_url('git@github.com:mriehl/pyb_init.git')
        self.assertEqual(actual_project_name, 'pyb_init')

    def test_should_return_project_name_for_git_read_only_url(self):
        actual_project_name = determine_project_name_from_git_url('git://github.com/mriehl/pyb_init.git')
        self.assertEqual(actual_project_name, 'pyb_init')


class SvnUrlToolsTests(unittest.TestCase):

    def test_should_return_project_name_for_svn_url(self):
        actual_project_name = determine_project_name_from_svn_url('https://svn/test')
        self.assertEqual(actual_project_name, 'test')

    def test_should_return_project_name_for_svn_url_ending_in_trunk(self):
        actual_project_name = determine_project_name_from_svn_url('https://svn/test/trunk')
        self.assertEqual(actual_project_name, 'test')
