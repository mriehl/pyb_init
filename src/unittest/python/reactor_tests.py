import unittest
from mockito import when, verify, any as any_value, unstub

import pyb_init
from pyb_init.tasks import ShellCommandTask

class ReactorTests(unittest.TestCase):

    def test_should_return_reactor_for_local_initialization(self):
        reactor = pyb_init.reactor.for_local_initialization()
        actual_tasks = reactor.get_tasks()
        self.assertEqual(actual_tasks, [ShellCommandTask('virtualenv virtualenv'),
                                        ShellCommandTask('source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('source virtualenv/bin/activate && pyb -v')
                                        ])