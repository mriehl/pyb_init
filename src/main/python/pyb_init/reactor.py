from __future__ import absolute_import
import os

from pyb_init.tasks import ShellCommandTask, PreconditionTask
from pyb_init.vcs_tools import determine_project_name_from_git_url

VIRTUALENV_NAME = 'virtualenv'


def for_local_initialization():
    reactor = TaskReactor()
    _add_common_tasks(virtualenv_name=VIRTUALENV_NAME, reactor=reactor, command_prefix=None)
    return reactor


def for_github_clone(user, project):
    reactor = TaskReactor()
    reactor.add_task(ShellCommandTask('git clone https://github.com/{0}/{1}'.format(user, project)))
    _add_common_tasks(virtualenv_name=VIRTUALENV_NAME,
                      reactor=reactor,
                      command_prefix='cd {0} && '.format(project),
                      project=project)
    return reactor


def for_git_clone(git_url):
    reactor = TaskReactor()
    reactor.add_task(ShellCommandTask('git clone {0}'.format(git_url)))
    project = determine_project_name_from_git_url(git_url)
    _add_common_tasks(virtualenv_name=VIRTUALENV_NAME,
                      reactor=reactor,
                      command_prefix='cd {0} && '.format(project),
                      project=project)
    return reactor


def _add_common_tasks(virtualenv_name, reactor, command_prefix, project=None):
    _add_preconditions(reactor, project)
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


def _add_preconditions(reactor, project):
    if project:
        reactor.add_task(PreconditionTask(lambda: os.path.exists('{0}/build.py'.format(project)),
                                          'Build descriptor ({0}/build.py) should exist'.format(project)))
    else:
        reactor.add_task(PreconditionTask(lambda: os.path.exists('build.py'),
                                          'Build descriptor (build.py) should exist'))


class TaskReactor(object):

    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)
