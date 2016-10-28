# !/usr/bin/env python
# -*- coding: UTF-8 -*-
#TODO:get the attrs form conf
import pika
import uuid
import time


class RpcClient(object):
    def __init__(self , queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost', heartbeat_interval=0))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.exchange_declare(exchange='test',type='direct')
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='test',
                                   routing_key=self.queue_name,
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        timeout = int(5)
        start = time.time()
        while self.response is None:
            if time.time()-start > timeout: #if timeout raise error
                self.response = {'timeout':time.clock()}
            self.connection.process_data_events()
        return self.response

