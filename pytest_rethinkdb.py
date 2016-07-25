# -*- coding: utf-8 -*-

from os import environ

import pytest

import rethinkdb


def pytest_addoption(parser):
    group = parser.getgroup('rethinkdb')
    group.addoption(
        '--rethinkdb-host',
        action='store',
        dest='rethinkdb_host',
        default='localhost',
        help='Host of the RethinkDB test instance.',
    )
    group.addoption(
        '--rethinkdb-port',
        action='store',
        dest='rethinkdb_port',
        default=28015,
        help='Port of the RethinkDB test instance.',
    )

    parser.addini('RETHINKDB_HOST',
                  'Host of the RethinkDB test instance',
                  default='localhost')

    parser.addini('RETHINKDB_PORT', 'The driver port', default=28015)
    parser.addini('RETHINKDB_DB',
                  'The database used if not explicitly specified in a query',
                  default='test')
    parser.addini('RETHINKDB_USER',
                  'The user account to connect as',
                  default='admin')
    parser.addini('RETHINKDB_PASSWORD',
                  'The password for the user account to connect as',
                  default='')
    parser.addini('RETHINKDB_TIMEOUT',
                  'Timeout period in seconds for the connection to be opened',
                  default=20)
    parser.addini('RETHINKDB_SSL',
                  'A hash of options to support SSL connections',
                  default=None)


@pytest.fixture
def conn(request):
    return rethinkdb.connect(
        host=request.config.option.rethinkdb_host,
        port=request.config.option.rethinkdb_port
    )
