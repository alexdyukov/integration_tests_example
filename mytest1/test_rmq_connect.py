# -*- coding: utf-8 -*-

import random
import string
from lib import rmq


def _declare_pipe(channel, exchange, queue, routing_key):
    channel.exchange_declare(exchange=exchange,
                             exchange_type='direct',
                             passive=False,
                             durable=False,
                             auto_delete=False)
    channel.queue_declare(queue=queue,
                          passive=False,
                          durable=False,
                          auto_delete=False,
                          exclusive=False)
    channel.queue_bind(queue=queue,
                       exchange=exchange,
                       routing_key=routing_key)


def _delete_pipe(channel, exchange, queue):
    channel.queue_delete(queue=queue)
    channel.exchange_delete(exchange=exchange)


def _generate_key(length):
    assert length > 0
    symbols = string.ascii_letters + string.digits
    return ''.join([random.choice(symbols) for n in range(length)])


def test_rmq_connect(rmq_root):
    """RabbitMQ test example"""

    key = _generate_key(length=10)
    exchange_name = 'todelete_exchangename_' + key
    queue_name = 'todelete_queuename_' + key
    routing_key = 'todelete_routingkey_' + key
    channel = rmq_root.channel()

    _declare_pipe(channel, exchange_name, queue_name, routing_key)

    # !!! body must be byte string, because of raw data
    test_body = b'test'
    rmq.put(channel, exchange_name, routing_key, test_body)
    return_body, return_properties = rmq.get(channel, queue_name)

    _delete_pipe(channel, exchange_name, queue_name)

    assert return_body == test_body
