from flask import Blueprint, jsonify, render_template
from flask import current_app as app
from flask import request as rq

from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema
from webargs import fields

import logging
logger = logging.getLogger('root')

import requests as rqs
import json as js
from xmltodict import parse as xmp
import numpy as np

# class DataSchema(Schema):
#     degrees = fields.List(fields.Dict())
class SSchema(Schema):
    string = fields.Str()

def get_data():
    """Get ISS Data from the Public Distribution and XMLsightingData_citiesUSA05 files.
    Returns:
        list: a list of dictionaries containing Public Distribution data
        list: a list of dictionaries containing XMLsighting data   
    """
    loc = ["https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml",
    "https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA05.xml"]
    return [xmp(rqs.get(loc[i]).content) for i in range(2)]

class data(MethodResource):

  _loaded = False
  public = {}
  sight = {}

  @app.route("/data", methods=['POST'])
  def data():
      """ ISS position data
      ---
      post:
        description: Updates the list of data dictionaries.
        security:
          - ApiKeyAuth: []
        responses:
          201:
            description: Updated data dictionary list.
            content:
              application/json:
                schema: SSchema
      """
      route="/data"
      try: data.public,data.sight = get_data()
      except Exception as e: 
        msg = f"Exception: {e}"
        logger.error(f'{route}:{msg}')
      else:
        data._loaded = True
        msg = "Data updated."
        logger.info(f'{route}:{msg}')
      return msg
      
def public():
    """Get Public Distribution ISS Data.
    Returns:
        list: a list of dictionaries containing Public Distribution data 
    """
    if not data._loaded:
      data.data()
    return np.array(data.public['ndm']['oem']['body']['segment']['data']["stateVector"])

def sight():
    """Get XMLSighting ISS Data.
    Returns:
        list: a list of dictionaries containing sighting data 
    """
    if not data._loaded:
      data.data()
    return np.array(data.sight['visible_passes']['visible_pass'])
    
  # @app.route("/data", methods=['GET'])
  # # @use_kwargs({'id': fields.Str(), 'year': fields.Str(), 'degrees': fields.Str()})
  # # @marshal_with(DataSchema(many=True))
  # def data():
  #     """ ISS position data
  #     ---
  #     get:
  #       description: Get list of data dictionaries
  #       security:
  #         - ApiKeyAuth: []
  #     #   parameters:
  #     #     start: starting data dictionary list index
  #       responses:
  #         200:
  #           description: Return list of data dictionaries
  #           content:
  #             application/json:
  #                 schema: DataSchema
  #     """
  #     a0 = rq.args.get('start', 0)
  #     route = '/data'
  #     try: st = int(a0)
  #     except ValueError: 
  #         msg = "Invalid start parameter. Please input an integer."
  #         logger.error(f'{route}:{msg}')
  #         return msg
  #         # return [{'error':msg}]
  #     # logger.info(f"GET : {route}")
  #     return jsonify(get_data()[st:])
      