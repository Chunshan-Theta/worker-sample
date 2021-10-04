import os

import tornado.web
from tornado_swagger.setup import setup_swagger
from handler.api.query.testHandler import testHandler

# jaeger
# from jaeger_client import Config
# import tornado_opentracing

# def init_jaeger_tracer(service_name):
#     config = Config(
#         config={  # usually read from some yaml config
#             'sampler': {
#                 'type': 'probabilistic',
#                 'param': 1,
#             },
#             'local_agent': {
#                 'reporting_host': '10.205.48.66',
#             },
#         },
#         service_name=service_name,
#         validate=True,
#     )
#     # Create your opentracing tracer using TornadoScopeManager for active Span handling.
#     return config.initialize_tracer()



# urls initial
urls = [


]


class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r"/status/Test", testHandler)
    ]

    def __init__(self, **settings):

        setup_swagger(
            self._routes,
            swagger_url="/docs",
            api_base_url="/",
            description="",
            api_version="1.0.0",
            title="Journal API",
            contact="name@domain",
            schemes=["http"],
            security_definitions={
                "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"}
            },
        )
        super(Application, self).__init__(self._routes, **settings)


# tornado_opentracing.init_tracing()
app = Application()

