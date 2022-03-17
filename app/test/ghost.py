from .. import init_app
from ..options import *
from flask import request as rq
# from inspect import signature
import pytest

# from app.api.data import get_data

# PYTEST functions and boilerplate, so not adding docstrings.

@pytest.fixture
def appload():
    app = init_app()
    app.config.update({
        "TESTING": True,
    })
    # app.run(host=host, debug=False,port=port)
    with app.app_context():
        yield

@pytest.fixture
def apprun():
    app = init_app()
    app.config.update({
        "TESTING": True,
    })
    app.run(host=host, debug=False,port=port)
    with app.app_context():
        yield
    shutdown_server()

def shutdown_server():
    func = rq.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()