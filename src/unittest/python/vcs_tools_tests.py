import unittest

from pyb_init.vcs_tools import determine_project_name_from_git_url

class VcsToolsTests(unittest.TestCase):

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
