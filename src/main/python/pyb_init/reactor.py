from __future__ import absolute_import
from pyb_init.tasks import ShellCommandTask

VIRTUALENV_NAME = 'virtualenv'


def for_local_initialization():
    reactor = TaskReactor()
    _add_common_tasks(virtualenv_name=VIRTUALENV_NAME, reactor=reactor, command_prefix=None)
    return reactor


def for_github_clone(user, project):
    reactor = TaskReactor()
    reactor.add_task(ShellCommandTask('git clone https://github.com/{0}/{1}'.format(user, project)))
    _add_common_tasks(virtualenv_name=VIRTUALENV_NAME, reactor=reactor, command_prefix='cd {0} && '.format(project))
    return reactor


def _add_common_tasks(virtualenv_name, reactor, command_prefix):
    commands = ['virtualenv {0} --clear'.format(virtualenv_name),
                'source {0}/bin/activate && pip install pybuilder'.format(virtualenv_name),
                'source {0}/bin/activate && pyb install_dependencies'.format(virtualenv_name),
                'source {0}/bin/activate && pyb -v'.format(virtualenv_name)]

    if command_prefix:
        expanded_commands = [command_prefix + command for command in commands]
    else:
        expanded_commands = commands
    for command in expanded_commands:
        reactor.add_task(ShellCommandTask(command))


class TaskReactor(object):

    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)
