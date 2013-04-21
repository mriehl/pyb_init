'''
Usage:
pyb-init local

-h --help    show this
'''
__version__ = '${version}'

from docopt import docopt
from pyb_init import reactor


def entry_point():
    parsed_command_line = docopt(doc=__doc__, version=__version__)
    task_reactor = None
    if parsed_command_line['local']:
        task_reactor = reactor.for_local_initialization()

    for task in task_reactor.get_tasks():
        task.execute()
