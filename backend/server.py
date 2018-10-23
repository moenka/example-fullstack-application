#!/usr/bin/env python3

from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! My hostname is %s.' % gethostname()

app.run(host='0.0.0.0', port=80, debug=False)

