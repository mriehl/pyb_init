import unittest
from mockito import when, verify, any as any_value, unstub, mock

import pyb_init
from pyb_init.tasks import ShellCommandTask, ShellCommandTaskException

class ShellCommandTaskTests(unittest.TestCase):

    def tearDown(self):
        unstub()

    def test_should_initialize_with_shell_command(self):
        task = ShellCommandTask('echo true')
        self.assertEqual(task.shell_command, 'echo true')

    def test_should_run_task_as_shell_command(self):
        when(pyb_init.tasks.subprocess).call(any_value(), stderr=any_value(), stdout=any_value(), shell=any_value()).thenReturn(0)

        task = ShellCommandTask('ls -l')
        task.execute()

        verify(pyb_init.tasks.subprocess).call('ls -l', stderr=any_value(), stdout=any_value(), shell=any_value())

    def test_should_raise_exception_when_shell_call_fails(self):
        when(pyb_init.tasks.subprocess).call(any_value(), stderr=any_value(), stdout=any_value(), shell=any_value()).thenReturn(5)

        task = ShellCommandTask('ls -l')
        self.assertRaises(ShellCommandTaskException, task.execute)

class ShellCommandTaskExceptionTests(unittest.TestCase):
    def test_should_represent_task_as_string(self):
        task = ShellCommandTaskException('Error message')

        self.assertEqual(str(task), 'Error message')