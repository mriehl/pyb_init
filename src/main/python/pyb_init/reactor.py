from tasks import ShellCommandTask


def for_local_initialization():
    reactor = TaskReactor()
    virtualenv_name = 'virtualenv'
    reactor.add_task(ShellCommandTask('virtualenv {0}'.format(virtualenv_name)))
    reactor.add_task(ShellCommandTask('source {0}/bin/activate && pip install pybuilder'.format(virtualenv_name)))
    reactor.add_task(ShellCommandTask('source {0}/bin/activate && pyb install_dependencies'.format(virtualenv_name)))
    reactor.add_task(ShellCommandTask('source {0}/bin/activate && pyb -v'.format(virtualenv_name)))
    return reactor


class TaskReactor(object):

    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)
