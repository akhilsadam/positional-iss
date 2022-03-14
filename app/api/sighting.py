from flask import Blueprint, jsonify, render_template
from flask import current_app as app
from flask import request as rq

from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema
from webargs import fields

import logging
logger = logging.getLogger('root')

import app.api.data as data
from app.api.positional import JSON #schema

import numpy as np

# Note the following functions are simple enough that I did not separate out the processing!

class sighting(MethodResource):
    @app.route("/country", methods=['GET'])
    def countries():
        """ISS Country data - all.
        ---
        get:
          description: Get all possible countries.
          security:
            - ApiKeyAuth: []
          responses:
            200:
              description: Returns a list of countries.
              content:
                application/json:
                  schema: JSON
        """
        route="/country"
        try: 
            sight = data.sight()
            country = np.unique([sight[i]["country"] for i in range(len(sight))]).tolist()
        except Exception as e: 
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = "GET country list"
            logger.info(f'{route}: {msg}')
            return jsonify(country)

    @app.route("/country/<string:country>", methods=['GET'])
    def country(country: str):
        """ISS Country data - single.
        ---
        get:
          description: Get data for a single country.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: country
            in: path
            description: Value (name) of country to be queried. Ex: United_States
            required: true
            schema:
              type: string
          responses:
			200:
			  description: Returns all matching (queried country) sightings as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/country/{country}"
        try: 
            sight = data.sight()
            indx = np.where(np.array([sight[i]["country"] for i in range(len(sight))]) == country)[0]
            logger.debug(indx)
            country = sight[indx].tolist()
        except ValueError as v:
            msg = "Invalid input: no country exists as queried. Please try again with a valid country."
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET country {country}"
            logger.info(f'{route}: {msg}')
            return jsonify(country)
    
    @app.route("/country/<string:country>/region", methods=['GET'])
    def regions(country: str):
        """ISS Region data - all for a specific country.
        ---
        get:
          description: Get data for all regions of a certain country.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: country
            in: path
            description: Value (name) of country to be queried. Ex: United_States
            required: true
            schema:
              type: string
          responses:
			200:
			  description: Returns all matching regions for the queried country as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/country/{country}/region"
        try: 
            sight = data.sight()
            indx = np.where(np.array([sight[i]["country"] for i in range(len(sight))]) == country)[0]
            logger.debug(indx)
            region = np.unique([x["region"] for x in sight[indx]]).tolist()
        except ValueError as v:
            msg = "Invalid input: no country exists as queried. Please try again with a valid country."
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET regions for country {country}"
            logger.info(f'{route}: {msg}')
            return jsonify(region)
    
    @app.route("/country/<string:country>/region/<string:region>", methods=['GET'])
    def region(country: str,region: str):
        """ISS Region data - single.
        ---
        get:
          description: Get all data for a specific region of a certain country.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: country
            in: path
            description: Value (name) of country to be queried. Ex: United_States
            required: true
            schema:
              type: string
          - name: region
            in: path
            description: Value (name) of region to be queried. Ex: Kansas
            required: true
            schema:
              type: string
          responses:
			200:
			  description: Returns all matching results for the queried region as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/country/{country}/region/{region}"
        try: 
            sight = data.sight()
            indx = np.where(np.array([sight[i]["country"] for i in range(len(sight))]) == country)[0]
            indx2 = np.where(np.array([x["region"] for x in sight[indx]]) == region)[0]
            city = sight[indx][indx2].tolist()
            # logger.debug(city)
        except ValueError as v:
            msg = "Invalid input: either no country or region exists as queried. Please try again with valid input."
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET region {region} from country {country}"
            logger.info(f'{route}: {msg}')
            return jsonify(city)

    @app.route("/country/<string:country>/region/<string:region>/city", methods=['GET'])
    def cities(country: str,region: str):
        """ISS Cities data - all.
        ---
        get:
          description: Get all cities for a specific region of a certain country.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: country
            in: path
            description: Value (name) of country to be queried. Ex: United_States
            required: true
            schema:
              type: string
          - name: region
            in: path
            description: Value (name) of region to be queried. Ex: Kansas
            required: true
            schema:
              type: string
          responses:
			200:
			  description: Returns all matching cities for the queried region and country as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/country/{country}/region/{region}/city"
        try: 
            sight = data.sight()
            indx = np.where(np.array([sight[i]["country"] for i in range(len(sight))]) == country)[0]
            indx2 = np.where(np.array([x["region"] for x in sight[indx]]) == region)[0]
            city = np.unique([x['city'] for x in sight[indx][indx2]]).tolist()
            # logger.debug(city)
        except ValueError as v:
            msg = "Invalid input: either no country or region exists as queried. Please try again with valid input."
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET all cities in {region}, {country}"
            logger.info(f'{route}: {msg}')
            return jsonify(city)
    
    @app.route("/country/<string:country>/region/<string:region>/city/<string:city>", methods=['GET'])
    def city(country: str,region: str,city: str):
        """ISS Cities data - single.
        ---
        get:
          description: Get all information for a specific city of a region of a certain country.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: country
            in: path
            description: Value (name) of country to be queried. Ex: United_States
            required: true
            schema:
              type: string
          - name: region
            in: path
            description: Value (name) of region to be queried. Ex: Kansas
            required: true
            schema:
              type: string
          - name: city
            in: path
            description: Value (name) of city to be queried. Ex: Wichita
            required: true
            schema:
              type: string
          responses:
			200:
			  description: Returns all information for the queried city as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/country/{country}/region/{region}/city/{city}"
        try: 
            sight = data.sight()
            indx = np.where(np.array([sight[i]["country"] for i in range(len(sight))]) == country)[0]
            indx2 = np.where(np.array([x["region"] for x in sight[indx]]) == region)[0]
            indx3 = np.where(np.array([x["city"] for x in sight[indx][indx2]]) == city)[0]
            city = sight[indx][indx2][indx3].tolist()
            # logger.debug(city)
        except ValueError as v:
            msg = "Invalid input: either no country nor region nor city exists as queried. Please try again with valid input. \
              (if this message seems grammatically incorrect to you, replace the 'nor' with 'or no'.)"
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET all cities in {region}, {country}"
            logger.info(f'{route}: {msg}')
            return jsonify(city)