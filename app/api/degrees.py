from flask import Blueprint, jsonify, render_template
from flask import current_app as app
from flask import request as rq

from flask_apispec import use_kwargs, marshal_with
from marshmallow import Schema
from webargs import fields

import logging
logger = logging.getLogger('root')

class DegreeSchema(Schema):
    id = fields.Int()
    year = fields.Int()
    degrees = fields.Int()

class DegreesSchema(Schema):
    degrees = fields.List(fields.Dict(fields.Str(), fields.Int()))

def get_data():
    """Get degrees over the years.
    Returns:
        list: a list of dictionaries containing the id, year, and degrees.    
    """
    return [ {'id': 0, 'year': 1990, 'degrees': 5818},
    {'id': 1, 'year': 1991, 'degrees': 5725},
    {'id': 2, 'year': 1992, 'degrees': 6005},
    {'id': 3, 'year': 1993, 'degrees': 6123},
    {'id': 4, 'year': 1994, 'degrees': 6096} ]


@app.route("/degrees", methods=['GET'])
# @use_kwargs({'id': fields.Str(), 'year': fields.Str(), 'degrees': fields.Str()})
# @marshal_with(DegreeSchema(many=True))
def degrees():
    """ Degree observations
    ---
    get:
      description: Get list of degree dictionaries
      security:
        - ApiKeyAuth: []
    #   parameters:
    #     start: starting degree dictionary list index
      responses:
        200:
          description: Return list of degree dictionaries
          content:
            application/json:
                schema: DegreesSchema
    """
    a0 = rq.args.get('start', 0)
    route = '/degrees'
    try: st = int(a0)
    except ValueError: 
        msg = "Invalid start parameter. Please input an integer"
        logger.error(f'{route}:{msg}')
        return msg
    # logger.info(f"GET : {route}")
    return jsonify(get_data()[st:])
    