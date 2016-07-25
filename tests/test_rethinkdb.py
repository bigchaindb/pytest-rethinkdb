# -*- coding: utf-8 -*-

from os import environ


def test_conn_fixture(testdir):
    """Test the conn fixture."""

    rethinkdb_host = environ.get('TEST_RETHINKDB_HOST', 'rdb')
    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_conn(conn):
            assert conn.host == '{}'
            assert conn.port == 28015
    """.format(rethinkdb_host))

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--rethinkdb-host={}'.format(rethinkdb_host),
        '--rethinkdb-port=28015',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_conn PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'rethinkdb:',
        '*--rethinkdb-host=RETHINKDB_HOST',
        '*Host of the RethinkDB test instance.',
        '*--rethinkdb-port=RETHINKDB_PORT',
        '*Port of the RethinkDB test instance.',
    ])


def test_rethinkdb_host_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        RETHINKDB_HOST = planetearth
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def rethinkdb_host(request):
            return request.config.getini('RETHINKDB_HOST')

        def test_rethinkdb_host_planetearth(rethinkdb_host):
            assert rethinkdb_host == 'planetearth'
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_rethinkdb_host_planetearth PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
