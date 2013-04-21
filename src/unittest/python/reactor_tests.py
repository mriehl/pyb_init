from __future__ import absolute_import
import unittest
from mockito import when, verify, any as any_value, unstub

import pyb_init
from pyb_init.tasks import ShellCommandTask, PreconditionTask
from pyb_init.reactor import _add_common_tasks, TaskReactor, _add_preconditions

class ReactorTests(unittest.TestCase):

    def test_should_return_reactor_for_local_initialization(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = pyb_init.reactor.for_local_initialization()
        actual_tasks = reactor.get_tasks()
        self.assertEqual(actual_tasks, [ShellCommandTask('virtualenv virtualenv --clear'),
                                        ShellCommandTask('source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('source virtualenv/bin/activate && pyb -v')
                                        ])

    def test_should_return_reactor_for_github_clone(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = pyb_init.reactor.for_github_clone(user='user', project='project')
        actual_tasks = reactor.get_tasks()

        self.assertEqual(actual_tasks, [ShellCommandTask('git clone https://github.com/user/project'),
                                        ShellCommandTask('cd project && virtualenv virtualenv --clear'),
                                        ShellCommandTask('cd project && source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('cd project && source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('cd project && source virtualenv/bin/activate && pyb -v')
                                        ])
    def test_should_add_common_tasks_should_add_commands_when_no_prefix_is_given(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = TaskReactor()
        _add_common_tasks(virtualenv_name='venv', reactor=reactor, command_prefix=None)

        self.assertEqual(reactor.get_tasks(), [ShellCommandTask('virtualenv venv --clear'),
                                               ShellCommandTask('source venv/bin/activate && pip install pybuilder'),
                                               ShellCommandTask('source venv/bin/activate && pyb install_dependencies'),
                                               ShellCommandTask('source venv/bin/activate && pyb -v')])

    def test_should_add_common_tasks_should_add_prefixed_commands_when_prefix_is_given(self):
        reactor = TaskReactor()
        _add_common_tasks(virtualenv_name='venv', reactor=reactor, command_prefix='wtf ')

        self.assertEqual(reactor.get_tasks(), [ShellCommandTask('wtf virtualenv venv --clear'),
                                               ShellCommandTask('wtf source venv/bin/activate && pip install pybuilder'),
                                               ShellCommandTask('wtf source venv/bin/activate && pyb install_dependencies'),
                                               ShellCommandTask('wtf source venv/bin/activate && pyb -v')])

    def test_should_add_preconditions_on_local_project(self):
        reactor = TaskReactor()
        _add_preconditions(reactor, None)

        self.assertEqual(reactor.get_tasks(), [PreconditionTask(lambda: os.path.exists('build.py'), 'Build descriptor (build.py) should exist')])

    def test_should_add_preconditions_on_foreign_project(self):
        reactor = TaskReactor()
        _add_preconditions(reactor, 'project')

        self.assertEqual(reactor.get_tasks(), [PreconditionTask(lambda: os.path.exists('project/build.py'), 'Build descriptor (project/build.py) should exist')])
