from ..options import *
from marshmallow import ValidationError
from .. import log
logger = log.init_logger('root')
from .ghost import appload, apprun

# Disclaimer: note most of the code is in register.py, along with the api save functions, since it is the same workflow.

def test_expectedAPI(appload):
    from app.api.register import capture, generateAPI
    # s = signature(func)
    # param = s.parameters.keys()
    # ann = [s.parameters[p] for p in param]
    from flask import current_app as app
    app.run(host=host, debug=False,port=port)
    url = f"{baseurl}/api/api.json"
    capture(f"{baseurl}/country", type=0, appcontext=True)
    capture(f"{baseurl}/country/United_States", type=0, appcontext=True)
    api = capture(url,appcontext=True)
    eva = generateAPI(api,True,False,appcontext=True)
    for test in eva:
        if test[1] != 0:
            logger.critical(f"Assertion Error : ENDPOINT {test[0]} fails example")
            raise(AssertionError)


# def test_unexpectedAPI(apprun):
#     from app.api.register import capture, generateAPI
#     # s = signature(func)
#     # param = s.parameters.keys()
#     # ann = [s.parameters[p] for p in param]
#     url = f"{baseurl}/api/api.json"
#     api = capture(url)
#     eva = generateAPI(api,True,True)
#     for test in eva:
#         if test[1] != 0:
#             logger.critical(f"Assertion Error : ENDPOINT {test[0]} does not fail every 'improper-input' test")
#             raise(AssertionError)

