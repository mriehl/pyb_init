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

    def test_should_invoke_docopt_with_version_and_docstring(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True})

        entry_point()

        verify(pyb_init).docopt(doc=pyb_init.__doc__, version='${version}')

    def test_should_run_local_initialization_when_argument_is_given(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True})

        entry_point()

        verify(pyb_init.reactor).for_local_initialization()

    def test_should_run_all_tasks_until_finished(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({'local': True})
        mock_reactor = mock()
        mock_task_1 = mock()
        mock_task_2 = mock()
        when(pyb_init.reactor).for_local_initialization().thenReturn(mock_reactor)
        when(mock_reactor).get_tasks().thenReturn([mock_task_1, mock_task_2])

        entry_point()

        verify(mock_task_1).execute()
        verify(mock_task_2).execute()
