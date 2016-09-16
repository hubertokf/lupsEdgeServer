import datetime

import bottle
import mtwsgi


class MTServer(bottle.ServerAdapter):
    def run(self, handler):
        thread_count = self.options.pop('thread_count', None)
        server = mtwsgi.make_server(self.host, self.port, handler, thread_count, **self.options)
        server.serve_forever()


if __name__ == '__main__':
    app = bottle.Bottle()

    @app.route('/')
    def foo():
        return 'hello, world!\n'
        #return str(datetime.datetime.now())

    @app.route('/time')
    def time():
        #return 'hello, world 2!\n'
        return str(datetime.datetime.now())

    app.run(server=MTServer, host='0.0.0.0', port=8080, thread_count=3)
