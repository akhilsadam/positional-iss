import collections

from marshmallow import ValidationError
import flask
from re import error
import numpy as np

import pytest
# from hypothesis.extra import ghostwriter
# from hypothesis import given
# from hypothesis.strategies import text
from .ghost import appload
from ..api.schema import * #schema

# Disclaimer: note I am actually not using Schemas properly... that requires a bit more effort...

def test_get_data(appload):
    from ..api.data import get_data
    d=get_data()
    assert type(d) == list
    assert len(d) == 2
    assert type(d[0]) == collections.OrderedDict
    assert type(d[1]) == collections.OrderedDict
    JSON().load({'json':d}) # no exception
    d[0]['ndm']['oem']['body']['segment']['data']["stateVector"] # no exception
    d[1]['visible_passes']['visible_pass'] # no exception
    with pytest.raises(KeyError):
        d[0]['oem']
    with pytest.raises(KeyError):
        d[1]['visible_pass']

    # print(get_data())
    # ghostwriter.fuzz(get_data, except_=error)

def test_data(appload):
    from ..api.data import data
    d=data.data()
    assert type(d) == flask.wrappers.Response

    SSchema().load({'string':d.get_data()}) # no exception (can be replaced by a simple string check)
    assert isinstance(d.get_json(),str)

def test_public(appload):
    from ..api.data import public
    d=public()
    assert type(d) == np.ndarray
    assert len(d.shape) == 1


def test_sight(appload):
    from ..api.data import sight
    d=sight()
    assert type(d) == np.ndarray
    assert len(d.shape) == 1


