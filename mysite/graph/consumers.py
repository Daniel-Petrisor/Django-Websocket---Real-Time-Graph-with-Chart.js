import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(100):
            # value >>> main.js file
            self.send(json.dumps({'value': randint(100, 120)}))
            sleep(1)