"""Routes for Flask app."""
import os
from flask import current_app as app
from flask import render_template

import app.log as log
logger = log.init_logger('root')

from app.api.degrees import *

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec


from marshmallow import Schema, fields



appname = "positional-iss"
apiversion='v0.0.1'

class HTML(Schema):
    html = fields.Str()


@app.route("/", methods=['GET'])
def home():
    """Application homepage.
    ---
    get:
      description: Get homepage HTML
      security:
        - ApiKeyAuth: []
      responses:
        200:
          description: Return homepage HTML
          content:
            application/json:
              schema: HTML
    """
    return render_template(
        "index.jinja2",
        title=appname,
        description="",
        template="home-template",
        body="This is a homepage served with Flask.",
        readmelink = "https://github.com/akhilsadam/positional-iss",
    )

@app.route("/pdf", methods=['GET'])
def pdf():
    """Application writeup / research article.
    ---
    get:
      description: Get writeup HTML
      security:
        - ApiKeyAuth: []
      responses:
        200:
          description: Return writeup HTML
          content:
            application/json:
              schema: HTML
    """
    return render_template(
        "readme.jinja2",
        general=
"""Documentation""",
        template="home-template",
        body="This is a homepage served with Flask.",
    )

# @app.route("/api/doc", methods=['GET'])
# def pdf():
#     """Application API Reference.
#     ---
#     get:
#       description: Get API documentation
#       security:
#         - ApiKeyAuth: []
#       responses:
#         200:
#           description: Return API documentation
#           content:
#             application/json:
#               schema: HTML
#     """
#     return 

app.config.update({
    'APISPEC_SPEC': APISpec(
        title=appname,
        version=apiversion,
        openapi_version="3.0.2",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/api',
    'APISPEC_SWAGGER_UI_URL': '/api/doc',
})
docs = FlaskApiSpec(app)

docs.register(home)
docs.register(pdf)

denylist = ['__pyc','__init']

for file in os.listdir('app/api/'):
    if all(item not in file for item in denylist):
        page = file[:len(file)-3]
        exec(f'from app.api.{page} import {page}')
        exec(f'docs.register({page})')
    # exec(f'app.register_blueprint({page})')