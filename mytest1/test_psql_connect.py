# -*- coding: utf-8 -*-

from lib import psql


def test_psql_connect(mydb1):
    """Test example with PostgreSQL connection"""
    output = psql.execute(mydb1, 'SELECT 1 FROM dual', ())
    assert output[0] == (1,)
