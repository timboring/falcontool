import os
import sys

import click


BASEDIRS = ['tests', 'src']
BASEFILES = ['requirements.txt', 'README.md', 'src/api.py', 'CODEOWNERS']


class Error(Exception):
    pass


class CreateResourceError(Error):
    pass


def touch(filename):
    with open(filename, 'w') as fd:
        initial_string = '# This file was autogenerated by falcon.'
        fd.write(initial_string)


def output_status(resource_type, resource_name, resource_status='created'):
    click.echo(f'{resource_status} {resource_type} {resource_name}')


@click.command()
@click.argument('name')
@click.option('--dockerfile', '-d', is_flag=True, help='Create empty Dockerfile')
@click.option('--models', '-m', is_flag=True, help='Create empty models.py file')
@click.option('--resources', '-r', is_flag=True, help='Create empty resources.py file')
@click.option('--tox', '-t', is_flag=True, help='Create empty tox.ini file')
@click.pass_context
def create(ctx, name, dockerfile, models, resources, tox):
    if os.path.exists(name):
        click.echo(f'Cowardly refusing to clobber existing directory {name}.')
        sys.exit(2)

    os.makedirs(name)
    os.chdir(name)
    output_status('directory', name)

    for dir in BASEDIRS:
        os.makedirs(dir)
        output_status('directory', dir)

    for file in BASEFILES:
        touch(file)
        output_status('file', file)

    if dockerfile:
        touch('Dockerfile')
        output_status('file', 'Dockerfile')

    if models:
        touch('src/models.py')
        output_status('file', 'src/models.py')

    if resources:
        touch('src/resources.py')
        output_status('file', 'src/resources.py')

    if tox:
        touch('tox.ini')
        output_status('file', 'tox.ini')