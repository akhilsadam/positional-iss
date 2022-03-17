from ..options import *
from flask import request as rq
from .. import init_app, log
logger = log.init_logger('root')
# from inspect import signature
import pytest

# from app.api.data import get_data

# PYTEST functions and boilerplate, so not adding docstrings.

@pytest.fixture
def app():
    app = init_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def appload(app):
    with app.app_context():
        yield

@pytest.fixture
def client(app):
    return app.test_client()

# def instance_app():
#     from flask import current_app as app
#     app.config.from_object('config.Config')
#     with app.app_context():
#         from .. import routes

#     for rule in app.url_map.iter_rules():
#         logger.info(rule)
#     return app



# @pytest.fixture
# def apprun():
#     app = genapp()
#     app.config.update({
#         "TESTING": True,
#     })
#     app.run(host=host, debug=False,port=port)
#     with app.app_context():
#         yield
#     shutdown_server()

# def shutdown_server():
#     func = rq.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()