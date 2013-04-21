from __future__ import absolute_import
import unittest
from mockito import when, verify, any as any_value, unstub, mock

import pyb_init
from pyb_init import tasks
from pyb_init.tasks import ShellCommandTask, ShellCommandTaskException, PreconditionTask, PreconditionNotFulfilledException


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

        verify(pyb_init.tasks.subprocess).call('ls -l', stderr=tasks.sys.stderr, stdout=tasks.sys.stdout, shell=True)

    def test_should_raise_exception_when_shell_call_fails(self):
        when(pyb_init.tasks.subprocess).call(any_value(), stderr=any_value(), stdout=any_value(), shell=any_value()).thenReturn(5)

        task = ShellCommandTask('ls -l')
        self.assertRaises(ShellCommandTaskException, task.execute)


class PreconditionTaskTests(unittest.TestCase):

    def test_should_succeed_when_precondition_is_true(self):
        precondition = PreconditionTask(lambda: True, 'Always succeeds')
        precondition.execute()

    def test_should_fail_when_precondition_is_false(self):
        precondition = PreconditionTask(lambda: False, 'Always fails')
        self.assertRaises(PreconditionNotFulfilledException, precondition.execute)


class PreconditionNotFulfilledExceptionTests(unittest.TestCase):
    def test_should_represent_precondition_as_string(self):
        precondition = PreconditionNotFulfilledException('Precondition failed')

        self.assertEqual(str(precondition), 'Precondition failed')


class ShellCommandTaskExceptionTests(unittest.TestCase):
    def test_should_represent_task_as_string(self):
        task = ShellCommandTaskException('Error message')

        self.assertEqual(str(task), 'Error message')
