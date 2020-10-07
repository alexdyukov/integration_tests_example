# -*- coding: utf-8 -*-

import pytest
from lib import psql
from lib import rmq


@pytest.fixture(scope='session')
def mydb1():
    p = psql.create_pool(
            url = _get_psql_url(),
            conn_limit = _get_psql_conn_limit()
    )
    yield p
    p.close()


@pytest.fixture(scope='session')
def rmq_root():
    c = rmq.create_connection(
            url = _get_rmq_root_url()
    )
    yield c
    c.close()


def _get_psql_url():
    # TODO parsing env
    return 'postgresql://postgres:postgres@localhost:5432/postgres'


def _get_psql_conn_limit():
    # TODO parsing env
    return 5


def _get_rmq_root_url():
    # TODO parsing env
    return 'amqp://guest:guest@localhost:5672/%2F'
