import subprocess
import sys


class ShellCommandTask(object):

    def __init__(self, shell_command):
        self.shell_command = shell_command

    def __eq__(self, other_shell_command_task):
        return self.shell_command == other_shell_command_task.shell_command

    def execute(self):
        call_result = subprocess.call(self.shell_command, stderr=sys.stderr, stdout=sys.stdout, shell=True)
        if call_result != 0:
            raise ShellCommandTaskException('Call "{0}" exited with nonzero value {1}.'.format(self.shell_command,
                                                                                               call_result))


class ShellCommandTaskException(RuntimeError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
