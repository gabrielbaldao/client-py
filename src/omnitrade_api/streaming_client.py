import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
from client import Client

class StreamingClient(Client):
    def __init__(self, options = {}):
        #   super
        self.endpoint = options['endpoint'] if 'endpoint' in options.keys() else 'wss://omnitrade.com:8080' 
        self.logger   = options['logger'] if 'logger' in options.keys() else 'Logger' #Logger(STDOUT)
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.endpoint,
                                on_message  =   self.on_message,
                                on_error    =   self.on_error,
                                on_close    =   self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, message):
        print(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                self.ws.send("Hello %d" % i)
            time.sleep(1)
        # self.ws.close()
        print("thread terminating...")
        thread.start_new_thread(run, ())


