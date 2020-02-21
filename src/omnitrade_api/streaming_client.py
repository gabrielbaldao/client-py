import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import logging
import json
import ast
from client import Client

logging.basicConfig(level=logging.INFO)

class StreamingClient(Client):
    def __init__(self, options = {}):
        super(StreamingClient, self).__init__(options)
        self.endpoint = options['endpoint'] if 'endpoint' in options.keys() else 'wss://omnitrade.com:8080' 
        self.logger   = options['logger'] if 'logger' in options.keys() else logging
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.endpoint,
                                on_message  =   self.on_message,
                                on_error    =   self.on_error,
                                on_close    =   self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, message):
        msg = ast.literal_eval(message.decode())

        key =  msg.keys()[0]
        data = msg[key]
        if data != None and key == 'challenge':
            self.ws.send(str(self.auth.signed_challenge(data)).encode())
        else:
            try:
            except Exception as e:
                self.logger.error("Failed to process message: {error}".format(error=e))

    def on_error(self, error):
        self.logger.info(error)

    def on_close(self):
        self.ws.close()
        self.logger.info("### closed ###")

    def on_open(self):
        self.logger.info("Connected")
