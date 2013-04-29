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

from __future__ import absolute_import
import subprocess
import sys


class PreconditionTask(object):
    def __init__(self, precondition_callback, description):
        self.precondition_callback = precondition_callback
        self.description = description

    def execute(self):
        if self.precondition_callback() is False:
            raise PreconditionNotFulfilledException('Precondition "{0}" not met.'.format(self.description))

    def __eq__(self, other_precondition_task):
        return self.description == other_precondition_task.description


class ShellCommandTask(object):

    def __init__(self, shell_command, ignore_failures=False):
        self.shell_command = shell_command
        self.ignore_failures = ignore_failures

    def __eq__(self, other_shell_command_task):
        return self.shell_command == other_shell_command_task.shell_command

    def __str__(self):
        return self.shell_command

    def execute(self):
        call_result = subprocess.call(self.shell_command,
                                      stderr=sys.stderr,
                                      stdout=sys.stdout,
                                      shell=True,
                                      executable='/bin/bash')
        if call_result != 0 and not self.ignore_failures:
            raise ShellCommandTaskException('Call "{0}" exited with nonzero value {1}.'.format(self.shell_command,
                                                                                               call_result))
        return call_result


class ShellCommandTaskException(RuntimeError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class PreconditionNotFulfilledException(ValueError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
