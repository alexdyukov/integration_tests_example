# -*- coding: utf-8 -*-

from lib import psql


def test_psql_connect(mydb1):
    """Test example with PostgreSQL connection"""
    output = psql.execute_sql(mydb1, 'SELECT 1', ())
    assert output[0] == (1,)
