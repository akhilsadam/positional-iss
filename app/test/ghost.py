from functools import lru_cache
from app.api.register import capture, generateAPI
from .. import init_app
from ..options import *
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

@lru_cache(maxsize=20) # only should ever have 1 call.
def sign():
    # s = signature(func)
    # param = s.parameters.keys()
    # ann = [s.parameters[p] for p in param]
    url = f"{baseurl}/api/api.json"
    api = capture(url)
    return generateAPI(api,True)