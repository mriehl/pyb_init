from __future__ import absolute_import
import unittest
from mockito import when, verify, any as any_value, unstub, mock

import pyb_init
from pyb_init import entry_point

class PybInitTests(unittest.TestCase):

    def tearDown(self):
        unstub()

    def setUp(self):
        self.set_up_no_op_reactor()

    def set_up_no_op_reactor(self):
        mock_reactor = mock()
        when(mock_reactor).get_tasks().thenReturn([])
        when(pyb_init.reactor).for_local_initialization().thenReturn(mock_reactor)
        when(pyb_init.reactor).for_github_clone(user=any_value(), project=any_value()).thenReturn(mock_reactor)
        when(pyb_init.reactor).for_git_clone(git_url=any_value()).thenReturn(mock_reactor)

    def test_should_invoke_docopt_with_version_and_docstring(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True, 'github': False, 'git': False})

        entry_point()

        verify(pyb_init).docopt(doc=pyb_init.__doc__, version='${version}')

    def test_should_run_local_initialization_when_argument_is_given(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True, 'github': False, 'git': False})

        entry_point()

        verify(pyb_init.reactor).for_local_initialization()

    def test_should_run_github_initialization_when_argument_is_given(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': False,
                                                                                'git': False,
                                                                                'github': True,
                                                                                '<user>': 'coder1234',
                                                                                '<project>': 'committer'})

        entry_point()

        verify(pyb_init.reactor).for_github_clone(user='coder1234', project='committer')

    def test_should_run_git_initialization_when_argument_is_given(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': False,
                                                                                'github': False,
                                                                                'git': True,
                                                                                '<git_url>': 'foo'})

        entry_point()

        verify(pyb_init.reactor).for_git_clone(git_url='foo')

    def test_should_run_all_tasks_until_finished(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True, 'github': False, 'git': False})
        mock_reactor = mock()
        mock_task_1 = mock()
        mock_task_2 = mock()
        when(pyb_init.reactor).for_local_initialization().thenReturn(mock_reactor)
        when(mock_reactor).get_tasks().thenReturn([mock_task_1, mock_task_2])

        entry_point()

        verify(mock_task_1).execute()
        verify(mock_task_2).execute()
