# -*- coding: utf-8 -*-

from os import environ

import pytest

import rethinkdb


def pytest_addoption(parser):
    group = parser.getgroup('rethinkdb')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2016',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo


@pytest.fixture
def conn():
    return rethinkdb.connect(
        host=environ.get('RETHINKDB_DATABASE_HOST', 'localhost'),
        port=environ.get('RETHINKDB_DATABASE_PORT', 28015))
