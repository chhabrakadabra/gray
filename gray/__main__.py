import subprocess
import sys

import click

from worker import init
from constants import DEFAULT_PLASMA_STORE_SIZE, PLASMA_SOCKET_LOCATION

def start_plasma_proc(store_size=DEFAULT_PLASMA_STORE_SIZE):
    print('Starting plasma store process')
    return subprocess.Popen(['plasma_store', '-m', str(store_size), '-s', PLASMA_SOCKET_LOCATION])

def start_worker_proc():
    print('Starting worker process')
    return subprocess.Popen([sys.executable, 'gray', 'worker'])

@click.group()
def cli():
    ...

@cli.command()
def node():
    subprocs = [start_plasma_proc(), start_worker_proc(), start_worker_proc()]
    for subproc in subprocs:
        subproc.wait()

@cli.command()
def worker():
    init()

if __name__ == '__main__':
    cli()
