import tornado.httpserver
import tornado.netutil
import tornado.options
from tornado import ioloop
from tornado.options import define, options, parse_command_line
import configparser
import datetime
import os
import json
import tornado.log
import socket

# Start application
from app_url import app

http_server = tornado.httpserver.HTTPServer(app)
port = 10050
host = '0.0.0.0'
http_server.listen(port, host)
print(f'Server is running at http://{host}:{port}')
print('Quit the server with Control-C')
io_loop = ioloop.IOLoop.instance()
io_loop.start()
