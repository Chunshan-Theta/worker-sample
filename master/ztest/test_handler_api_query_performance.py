import unittest, os, os.path, sys, urllib
import tornado.options
from tornado.options import options
from tornado.testing import AsyncHTTPTestCase
from tornado.options import define
import datetime
import configparser
import json
# add application root to sys.path
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, APP_ROOT)
sys.path.append(os.path.join(APP_ROOT, '..'))

# import your app module
from app_url import app
from util.config import UserConfig, update_config
from util.status import PreviousRequest, PreviousRequest_100
# Create your Application for testing
# In this example, the tornado config file is located in: APP_ROOT/config/test.py
# get config about serever
config = configparser.ConfigParser()
config.read(os.path.join(APP_ROOT, 'server.config'))
server_port = config["server.address"]["Port"]
server_ip = config["server.address"]["Server"]
running_mode = "dev" if config["server.log"]["running_mode"] == "DEV" else config["server.log"]["running_mode"]
server_log_dir = config["server.log"]["server_log_dir"]

# get config about valid users.
dir_path = "{}/LocalStorage/config".format(APP_ROOT)
service_config = update_config()
with open("{}/LocalStorage/intent/intent.json".format(APP_ROOT)) as file:
    temp_content = "".join(file.readlines())
    temp_obj = json.loads(temp_content)
    intent_dict = temp_obj
# update global variable
define("port", group='Webserver', type=int, default=server_port, help="Run on the given port")
define("server_ip", group='Webserver', type=int, default=server_ip, help="IP")
define("subpath", group='Webserver', type=str, default="", help="Url subpath (such as /nebula)")
define("running_mode", group='Webserver', type=str, default=running_mode, help="for logger level amendment")
define("turnon_time", group='Webserver', type=str, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), help="turnon_time")
define("server_log_dir", group='Webserver', type=str, default=server_log_dir, help="for logger level amendment")
define("application_log", group='Webserver', type=dict, default={}, help="application_log")
define("service_config", group='Webserver', type=object, default=service_config, help="users config")
define("status_PreviousRequest", group='Webserver',
       type=object,
       default=PreviousRequest(),
       help="status_PreviousRequest")

define("status_PreviousRequest_100", group='Webserver',
       type=object,
       default=PreviousRequest_100(),
       help="status_PreviousRequest_100")
define("intent_dict", group='Webserver', type=dict, default=intent_dict, help="init intent dict")
# Create your base Test class.
# Put all of your testing methods here.

class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return app

    def test_(self):
        self.fetch(self.get_url('/api/query?q=我是誰'), method="GET", headers={"token":"gitlabci"})


