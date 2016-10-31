import datetime

import bottle
import core.mtwsgi


class MTServer(bottle.ServerAdapter):

    def __init__(self,scheduler):
        app = bottle.Bottle()

        @app.route('/sigSchedule')
        def foo():
            scheduler.start_process();
            #asd.set_asd(1);
            return 'Verificação\n'
            #return str(datetime.datetime.now())

        @app.route('/sigSensor')
        def foo():
            #scheduler.start_process();
            #asd.set_asd(0);
            return 'Verificação\n'
            #return str(datetime.datetime.now())

        @app.route('/time')
        def time():
            #return 'hello, world 2!\n'
            return str(datetime.datetime.now())

        app.run(host='0.0.0.0', port=8081, thread_count=3)

    def run(self, handler):
        thread_count = self.options.pop('thread_count', None)
        server = mtwsgi.make_server(self.host, self.port, handler, thread_count, **self.options)
        server.serve_forever()
