# -*- coding: utf-8 -*-

from pika import URLParameters, BlockingConnection


def create_connection(url):
    parameters = URLParameters(url)
    connection = BlockingConnection(parameters)

    return connection


def get(channel, queue_name):
    method_frame, properties, body = channel.basic_get(queue_name)
    channel.basic_ack(method_frame.delivery_tag)
    return (body, properties)


def put(channel, exchange_name, routing_key, body, properties=None):
    channel.basic_publish(exchange_name, routing_key, body, properties)

