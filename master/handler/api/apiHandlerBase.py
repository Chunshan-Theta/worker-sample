# coding:utf-8

import json
import traceback
import datetime

from tornado.web import RequestHandler, HTTPError, Application
from tornado.options import options
from handler.api import errors
#
import uuid

import os



class APIHandlerBase(RequestHandler):


    def data_receive(self, chunk):
        pass

    def __init__(self, application, request, **kwargs):

        ##
        RequestHandler.__init__(self, application, request, **kwargs)
        Application.log_request = self._log_request

        ##
        self.set_header('Content-Type', 'text/json')
        self.handler_method_identify_label = None
        self.handler_log_info = {}
        self.request_id = str(uuid.uuid4())
        self.access_control_allow()

        try:
            self.request_body_json = json.loads(self.request.body)
        except Exception as e:
            self.request_body_json = None

    def access_control_allow(self):
        # allow JS cross
        self.set_header("Access-Content-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Depth, User-Agent, X-File-Size, "
                                                        "X-Requested-With, X-Requested-By, If-Modified-Since, "
                                                        "X-File-Name, Cache-Control, Token")
        self.set_header('Access-Control-Allow-Origin', '*')

    def get(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def post(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def put(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def delete(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def options(self, *args, **kwargs):
        self.write("")

    def write_json(self, data, status_code=200, msg='success.'):
        # init variable
        if str(status_code).startswith('2'):
            self.handler_log_info["reason"] = msg
        request_time = self.request.request_time()
        request_ip = self.request.remote_ip
        self.set_status(status_code=status_code, reason=msg)

        self.finish(json.dumps(data))

    @staticmethod
    def check_none(resource):
        if resource is None:
            raise HTTPError(**errors.status_22)

    def _log_request(self, handler):
        """Writes a completed HTTP request to the logs.

                By default writes to the python root logger.  To change
                this behavior either subclass Application and override this method,
                or pass a function in the application settings dictionary as
                ``log_function``.
                """
        """
        # init variable
        request_time = self.request.request_time()
        request_ip = self.request.remote_ip

        # logger
        logger = log_Object.getLogger("tornado.access")
        # if self.handler_method_identify_label is None: logger.warning("handler_method_identify_label is None")

        # get status
        log_method = logger.error if str(handler.get_status())[0] == '5' else logger.info if str(handler.get_status()) == '200' else logger.warning
        log_method("%d\t%s\t%.2fs\t%s" % (handler.get_status(),
                                               self.handler_method_identify_label,
                                               request_time,
                                               request_ip))
        """
        pass


class APINotFoundHandler(APIHandlerBase):

    def __init__(self, application, request):
        ##
        APIHandlerBase.__init__(self, application, request)
        Application.log_request = self._log_request
        self.handler_method_identify_label = "NOT FIND Handler"

    def data_receive(self, chunk):
        pass

    def get(self, *args, **kwargs):
        raise HTTPError(**errors.status_1)

    def post(self, *args, **kwargs):
        raise HTTPError(**errors.status_1)

    def put(self, *args, **kwargs):
        raise HTTPError(**errors.status_1)

    def delete(self, *args, **kwargs):
        raise HTTPError(**errors.status_1)

    def options(self, *args, **kwargs):
        if self.settings['allow_remote_access']:
            self.write("")




