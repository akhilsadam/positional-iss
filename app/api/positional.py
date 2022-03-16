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

from app.api.data import JSON #schema

class positional(MethodResource):
    @app.route("/epoch", methods=['GET'])
    def epochs():
        """ISS epoch data - all.
        ---
        get:
          description: Get all possible epochs.
          security:
            - ApiKeyAuth: []
          responses:
            200:
              description: Return a list of epochs.
              content:
                application/json:
                  schema: JSON
        """
        route="/epoch"
        try: 
            public = data.public()
            epochs = [public[i]["EPOCH"] for i in range(len(public))]
        except Exception as e: 
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = "GET epoch list"
            logger.info(f'{route}: {msg}')
            return jsonify(epochs)

    @app.route("/epoch/<string:name>", methods=['GET'])
    def epoch(name: str):
        """ISS epoch data - single.
        ---
        get:
          description: Get data for a single epoch.
          security:
            - ApiKeyAuth: []
          parameters:
          - name: name
            in: path
            description: Value of epoch to be queried.
            required: true
            example: 2022-042T12:04:00.000Z
            schema:
              type: string
          responses:
			200:
			  description: Return epoch information for first matching epoch as json.
			  content:
				application/json:
				  schema: JSON
        """
        route=f"/epoch/{name}"
        try: 
            public = data.public()
            index = [public[i]["EPOCH"] for i in range(len(public))].index(name)
            epoch = public[index]
        except ValueError as v:
            msg = "Invalid input: no epoch exists as queried. Please try again with a valid epoch."
            logger.error(f'{route}: {msg}')
            return msg
        except Exception as e:
            msg = f"Exception: {e}"
            logger.error(f'{route}: {msg}')
            return msg
        else:
            msg = f"GET epoch {name}"
            logger.info(f'{route}: {msg}')
            return jsonify(epoch)