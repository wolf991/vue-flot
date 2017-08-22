from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta
from random import randint
from time import sleep

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('time_from')
parser.add_argument('time_to')

class ChartData(Resource):
    def post(self):
        args = parser.parse_args()
        data = {'data': []}
        for i in range(20):
            series = {
                'avg': [],
                'min': [],
                'max': [],
            }
            for timestamp in range(int(args['time_from']), int(args['time_to']), 60 * 60):
                series['avg'].append([timestamp * 1000, randint(0, 10)])
                series['min'].append([timestamp * 1000, randint(0, 10)])
                series['max'].append([timestamp * 1000, randint(0, 10)])
            series['label'] = str(i)
            data['data'].append(series)
        sleep(1)
        return data

api.add_resource(ChartData, '/chartdata')

if __name__ == '__main__':
    app.run()
