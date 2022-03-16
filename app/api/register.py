from flask import Blueprint, jsonify, render_template
from flask import current_app as app
from flask import request as rq

from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from app.api.schema import * #schema

import logging
logger = logging.getLogger('root')

import requests as rqs
import json as js
import numpy as np

from app.options import baseurl,mdfile

# Not pytesting the following functions as 1) testing the requests is unecessary, 2) this is not core functionality and is not required by the specifications,
# 3) this is an API test in and of itself, and part of other tests, 4) developer exhaustion...

def capture(url, type=0):
  """Parses JSON from an endpoint.
  Arguments:
    str: A string containing the endpoint URL.
    int: GET or POST endpoint?
  Returns:
    dict: the Python dictionary version of the input url JSON.
  """
  if type==0:
    return js.loads(rqs.get(url).content.decode('utf8').replace("'", '"'))
  else:
    return js.loads(rqs.post(url).content.decode('utf8').replace("'", '"'))

def generateAPI(api,test=False):
  """Structure API information (currenly assumes single endpoint: either GET or POST, not both).
  Arguments: 
    dict: The API dictionary parsed by FlaskApiSpec.
    bool: Save test outputs?
  Returns:
    array: a NumPy array structure containing endpoints, descriptions, parameter names&descriptions, response descriptions, example input calls, example outputs.
  """
  REST = ["get","post"]
  REST2 = ["GET","POST"]
  p = 'parameters'
  paths = api['paths'].keys()
  denylist = ['/','/pdf','/api/save','/api/doc']

  # make i/o array

  io = np.zeros(shape=(len(paths),6),dtype=object) # endpoint,description, parameter names&descriptions, response descriptions, example input call, example output

  if test:
    exa = np.zeros(shape=(len(paths)),dtype=tuple(list,bool,object)) #  endpoint, status, example output

  # loop over API

  for i, pinfo in enumerate(zip(paths,api['paths'].values())):
    # logger.info(info['options'])
    path, info = pinfo
    io [i,0] = path
    state = 0

    for k,key in enumerate(REST):
      if key in info.keys():
        endpoint = info[key]
        io [i,1] = endpoint['description']
        logger.info(f"DESC:{endpoint['description']}")

        if p in endpoint.keys():
          params = endpoint['parameters']
          values = dict([(pq['name'],pq['example']) for pq in params])
          namedesc = [f"`{pq['name']}`\t:\t{pq['description']}\tAn example would be : `{pq['example']}`" for pq in params]
          io[i,2] = namedesc
          # logger.info(values)
          logger.info(f"PARAM:{namedesc}")
        else:
          values = None
          io [i,2] = ["N/A"]

        resp = endpoint['responses']
        respdesc = [f"A `{ret}` response will : {resp[ret]['description']}" for ret in resp.keys()]
        io[i,3] = respdesc
        logger.info(f"RESP:{respdesc}")

        if values is not None:
          segmented = np.array(path.replace("{","}").split("}"))
          odd = (np.array(list(range(len(segmented)))) % 2 == 1)
          # logger.info(segmented[odd])
          exval = [values[c] for c in segmented[odd]]
          # logger.info(exval)
          call = "".join([exval[int(j/2)] if odd[j] else segmented[j] for j in range(len(segmented))])
        else:
          call = path
        url = f"{baseurl}{call}"
        io[i,4] = f"`curl -X {REST2[k]} {url} -H \"accept: application/json\"`"
        logger.info(f"CALL:{url}")

        if call not in denylist:
          try:
            rawstringjs = js.dumps(capture(url,k), indent=4, sort_keys=True)
          except Exception as e:
            rawstringjs = "API CALL FAILED"
            state = 1
          # logger.info(stringjs)
          segmented = rawstringjs.split("\n")
          lox = len(segmented)
          if lox > 30:
            stringjsA = segmented[:15]
            stringjsA.extend(["...."])
            stringjsA.extend(segmented[lox-15:lox])
            rawstringjs = "\n".join(stringjsA)
          exresp = f"\n{rawstringjs}"
        else:
          exresp = None
        io[i,5] = exresp
        logger.info(f"OUT:{exresp}")

        break # remember, single endpoints!

    if test:
      exa[i] = (path,state,js.loads(rawstringjs))

  if test:
    return exa    
  return io


def formatAPI(io):
  """Structure API information.
  Arguments: 
    array: a NumPy array structure containing descriptions, parameter names&descriptions, response descriptions, example input calls, example outputs.
  Returns:
    string: a formatted Markdown output
  """
  # io = np.zeros(shape=(len(paths),6),dtype=object) # path,description, parameter names&descriptions, response descriptions, example input call, example output
  out = []
  for i in range(len(io)):
    f = io[i,:]
    path = f"### ENDPOINT: `{f[0]}`"
    desc = f" - Description: {f[1]}"
    param = " - Parameters: \n   -  {}".format("\n   -  ".join(f[2]))
    resp = " - Responses: \n   -  {}".format("\n   -  ".join(f[3]))
    if f[5] is not None:
      opt = " yields: "
      eoc = "```"+"  \n ".join(f[5].split("\n"))+"\n```"
    else:
      opt = ''
      eoc = ''
    eic = f"\n - Example: {f[4]}{opt}"
    st = "\n".join([path,desc,param,resp,eic,eoc])
    out.append(st)
  return "# REST API:\n" + "\n\n".join(out)


class register(MethodResource):

    @app.route("/api/save", methods=['GET'])
    def register():
        """Application API (generate API examples). UNSUPPORTED, so use at your own risk.
        ---
        get:
          description: Get API as rendered string
          security:
            - ApiKeyAuth: []
          responses:
            200:
              description: Return rendered API as string
              content:
                application/json:
                  schema: SSchema
        """
        route="/api/save"
        try:
            # get api
            url = f"{baseurl}/api/api.json"
            api = capture(url)
            io = generateAPI(api)
            markdown = formatAPI(io)
            # with open(mdfile,'r') as file:
            #   file.write(markdown)
        except Exception as e: 
            msg = f"Exception: {e}"
            logger.error(f'{route}:{msg}')
            return msg
        else:
            msg = "Generated Examples."
            logger.info(f'{route}:{msg}')
        return markdown