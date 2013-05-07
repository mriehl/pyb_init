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
#

from __future__ import absolute_import
import unittest
import os
from mockito import when, any as any_value, unstub

import pyb_init
from pyb_init.tasks import ShellCommandTask, PreconditionTask
from pyb_init.reactor import _add_common_tasks, TaskReactor, _add_preconditions
from pyb_init.configuration import set_configuration

class ReactorTests(unittest.TestCase):

    def tearDown(self):
        unstub()

    def setUp(self):
        set_configuration(virtualenv_name='virtualenv')

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
        reactor = pyb_init.reactor.for_github_clone(user='user1', project='project1')
        actual_tasks = reactor.get_tasks()

        self.assertEqual(actual_tasks, [ShellCommandTask('git clone https://github.com/user1/project1'),
                                        ShellCommandTask('cd project1 && virtualenv virtualenv --clear'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pyb -v')
                                        ])

    def test_should_respect_system_site_packages_configuration(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        set_configuration(virtualenv_name='virtualenv', virtualenv_use_system_site_packages=True)
        reactor = pyb_init.reactor.for_github_clone(user='user1', project='project1')
        actual_tasks = reactor.get_tasks()

        self.assertEqual(actual_tasks, [ShellCommandTask('git clone https://github.com/user1/project1'),
                                        ShellCommandTask('cd project1 && virtualenv virtualenv --clear --system-site-packages'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('cd project1 && source virtualenv/bin/activate && pyb -v')
                                        ])

    def test_should_return_reactor_for_git_clone(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        when(pyb_init.reactor).determine_project_name_from_git_url(any_value()).thenReturn('test')
        reactor = pyb_init.reactor.for_git_clone(git_url='https://git/test.git')
        actual_tasks = reactor.get_tasks()

        self.assertEqual(actual_tasks, [ShellCommandTask('git clone https://git/test.git'),
                                        ShellCommandTask('cd test && virtualenv virtualenv --clear'),
                                        ShellCommandTask('cd test && source virtualenv/bin/activate && pip install pybuilder'),
                                        ShellCommandTask('cd test && source virtualenv/bin/activate && pyb install_dependencies'),
                                        ShellCommandTask('cd test && source virtualenv/bin/activate && pyb -v')
                                        ])

    def test_add_common_tasks_should_add_only_commands_when_no_prefix_is_given(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = TaskReactor()
        _add_common_tasks(reactor=reactor, command_prefix=None)

        self.assertEqual(reactor.get_tasks(), [ShellCommandTask('virtualenv virtualenv --clear'),
                                               ShellCommandTask('source virtualenv/bin/activate && pip install pybuilder'),
                                               ShellCommandTask('source virtualenv/bin/activate && pyb install_dependencies'),
                                               ShellCommandTask('source virtualenv/bin/activate && pyb -v')])


    def test_add_common_tasks_should_respect_configured_virtualenv_name(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = TaskReactor()

        set_configuration(virtualenv_name='foobar')
        _add_common_tasks(reactor=reactor, command_prefix=None)

        self.assertEqual(reactor.get_tasks(), [ShellCommandTask('virtualenv foobar --clear'),
                                               ShellCommandTask('source foobar/bin/activate && pip install pybuilder'),
                                               ShellCommandTask('source foobar/bin/activate && pyb install_dependencies'),
                                               ShellCommandTask('source foobar/bin/activate && pyb -v')])

    def test_add_common_tasks_should_add_prefixed_commands_when_prefix_is_given(self):
        when(pyb_init.reactor)._add_preconditions(any_value(), any_value()).thenReturn(None)
        reactor = TaskReactor()
        _add_common_tasks(reactor=reactor, command_prefix='wtf ')

        self.assertEqual(reactor.get_tasks(), [ShellCommandTask('wtf virtualenv virtualenv --clear'),
                                               ShellCommandTask('wtf source virtualenv/bin/activate && pip install pybuilder'),
                                               ShellCommandTask('wtf source virtualenv/bin/activate && pyb install_dependencies'),
                                               ShellCommandTask('wtf source virtualenv/bin/activate && pyb -v')])

    def test_should_add_preconditions_on_local_project(self):
        reactor = TaskReactor()
        _add_preconditions(reactor, None)

        self.assertEqual(reactor.get_tasks(), [PreconditionTask(lambda: os.path.exists('build.py'), 'Build descriptor (build.py) should exist'),
                                               PreconditionTask(lambda: None, 'Virtualenv should be installed and callable')])

    def test_should_add_preconditions_on_foreign_project(self):
        reactor = TaskReactor()
        _add_preconditions(reactor, 'project')

        self.assertEqual(reactor.get_tasks(), [
                                                PreconditionTask(lambda: os.path.exists('project/build.py'), 'Build descriptor (project/build.py) should exist'),
                                                PreconditionTask(lambda: None, 'Virtualenv should be installed and callable')])
