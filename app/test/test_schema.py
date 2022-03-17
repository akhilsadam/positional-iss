from re import error

from marshmallow import ValidationError

import pytest
import json as js
# from hypothesis.extra import ghostwriter
# from hypothesis import given
# from hypothesis.strategies import text
from .conftest import app,appload
from ..api.schema import * #schema

# Disclaimer: note I am actually not using Schemas properly... that requires a bit more effort... (so we have a very minimal test case set here)

validJSON={"json":js.loads(""" [{
 		"city": "Olathe",
 		"country": "United_States",
 		"duration_minutes": "6",
 		"enters": "10 above SSW",
 		"exits": "10 above ENE",
 		"max_elevation": "28",
 		"region": "Kansas",
 		"sighting_date": "Thu Feb 17/06:13 AM",
 		"spacecraft": "ISS",
 		"utc_date": "Feb 17, 2022",
 		"utc_offset": "-6.0",
 		"utc_time": "12:13"
 	},
 	{
 		"city": "Nantucket",
 		"country": "United_States",
 		"duration_minutes": "3",
 		"enters": "19 above NNW",
 		"exits": "10 above NNE",
 		"max_elevation": "19",
 		"region": "Massachusetts",
 		"sighting_date": "Sat Feb 26/04:56 AM",
 		"spacecraft": "ISS",
 		"utc_date": "Feb 26, 2022",
 		"utc_offset": "-5.0",
 		"utc_time": "09:56"
 	}
 ]""")}
invalidJSON={"json":[dict([(3,5)]),"abc","errrpr"]}
validHTML={"html":str(["abc","errrpr"])}
invalidHTML={"html":["abc","errrpr"]}
validS={"string":str(["abce"])}
invalidS={"string":["abce"]}

def test_JSON():
    JSON().load(validJSON)
    with pytest.raises(ValidationError):
        JSON().load(invalidJSON)

def test_HTML():
    HTML().load(validHTML)
    with pytest.raises(ValidationError):
        HTML().load(invalidHTML)

def test_SSchema():
    SSchema().load(validS)
    with pytest.raises(ValidationError):
        SSchema().load(invalidS)