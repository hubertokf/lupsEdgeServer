import datetime
import requests
import bottle
import json
import core.mtwsgi

from bottle import get, post, request


class MTServer(bottle.ServerAdapter):

    def __init__(self, scheduler, subscriber):
        app = bottle.Bottle()

        @app.route('/sigSensor_add', method='POST')
        def index():

            postdata = request.body.read()
            str_data = json.loads(postdata.decode('utf-8'))

        @app.route('/sigSensor_delete', method='POST')
        def index():

            postdata = request.body.read()
            str_data = json.loads(postdata.decode('utf-8'))

        @app.route('/sigSchedule_add', method='POST')
        def index():


            postdata = request.body.read()
            str_data = json.loads(postdata.decode('utf-8'))

            str_data['modo'] = 'cron'

            scheduler.add_job(str_data);

        @app.route('/sigSchedule_delete', method='POST')
        def index():

            postdata = request.body.read()
            str_data = json.loads(postdata.decode('utf-8'))

            scheduler.remove_job(str_data);

        @app.route('/sigTopico_add', method='POST')
        def index():

            postdata = request.body.read()
            str_data = json.loads(postdata.decode('utf-8'))

            subscriber.add_subscribe(str_data);

        app.run(host='0.0.0.0', port=8081, thread_count=3)

    def run(self, handler):
        thread_count = self.options.pop('thread_count', None)
        server = mtwsgi.make_server(self.host, self.port, handler, thread_count, **self.options)
        server.serve_forever()
