# -*- coding: utf-8 -*-
# Author: Nam Nguyen Hoai
from flask import Flask
import monitor

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return monitor.get_content_from_server()


def run_server(port='3007'):
    app.run(host='0.0.0.0', port=port)
