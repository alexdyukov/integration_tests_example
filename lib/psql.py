# -*- coding: utf-8 -*-

import psycopg2
from psycopg2 import pool


def create_pool(url, conn_limit):
    pool = psycopg2.pool.SimpleConnectionPool(
            minconn = 1,
            maxconn = conn_limit,
            dsn = url
    )
    return pool


def execute_sql(pool, sql, params):
    connection = pool.getconn()

    if not connection:
        raise Exception('[psql] Cannot acquare connection from pool')

    cursor = connection.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    cursor.close()
    pool.putconn(connection)
    return rows

