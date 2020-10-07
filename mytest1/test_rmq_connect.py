# -*- coding: utf-8 -*-

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


def test_rmq_connect(rmq_root):
    """RabbitMQ test example"""
    exchange_name = 'todelete_exchangename_Oohebae2sesh'
    queue_name = 'todelete_queuename_Oohebae2sesh'
    routing_key = 'todelete_routingkey_Oohebae2sesh'
    channel = rmq.channel()

    _declare_pipe(channel, exchange_name, queue_name, routing_key)

    # !!! body must be byte string, because of raw data
    test_body = b'test'
    amqp.put(channel, exchange_name, routing_key, test_body)
    return_body, return_properties = amqp.get(channel, queue_name)

    _delete_pipe(channel, exchange_name, queue_name)

    assert return_body == test_body
