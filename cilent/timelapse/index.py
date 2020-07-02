#!/usr/bin/env python3

import os

from bottle import route, static_file, run

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='0.0.0.0', port='8080')
