"""Routes for Flask app."""
import os
from flask import Blueprint, current_app as app
from flask import render_template

from app.options import *

import app.log as log
logger = log.init_logger('root')

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec

from app.api.schema import * #schema

appname = "positional-iss"
apiversion='v0.0.1'

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
        readmelink = "https://github.com/akhilsadam/positional-iss",
    )

@app.route("/api/doc", methods=['GET'])
def api():
    """Application API, styled.
    ---
    get:
      description: Get API HTML
      security:
        - ApiKeyAuth: []
      responses:
        200:
          description: Return API HTML
          content:
            application/json:
              schema: HTML
    """
    # with open("app/static/dist/css/styleapi.css",'r') as f:
    #     css = f.read().replace("\n"," ")
    return render_template(
        "api.jinja2",
        title=appname,
        description="",
        template="home-template",
        readmelink = "https://github.com/akhilsadam/positional-iss",
        apilink = "/api",
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
        general="",
        template="home-template",
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
    'APISPEC_SWAGGER_URL': '/api/api.json',
    'APISPEC_SWAGGER_UI_URL': '/api',
})
docs = FlaskApiSpec(app)

docs.register(home)
docs.register(pdf)
docs.register(api)

### EVENT REGISTRATION | PLEASE LINE UP BY CLASS ###

denylist = ['__pyc','__init','test','schema']
denymethodlist = ['as_view','dispatch_request']

methods = []
for file in os.listdir('app/api/'):
    if all(item not in file for item in denylist):
        page = file[:len(file)-3]
        exec(f'from app.api.{page} import {page}')
        exec(f"methods = [attribute for attribute in dir({page}) if callable(getattr({page}, attribute)) and not attribute.startswith('__') and attribute not in denymethodlist]")
        for method in methods:
            logger.debug(f'{method}')
            # print(method)
            exec(f'docs.register({page}.{method})')
    # exec(f'app.register_blueprint({page})')