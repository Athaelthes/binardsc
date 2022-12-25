import re

from flask import Flask, jsonify

app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
info = {
    'title':LazyString(lambda: 'API Documentation for Data Proessing and Modeling'),
    'version': LazyString(lambda: '1.0.0'),
    'description' : LazyString (lambda: 'Dokumentasi API untuk Data Processing dan Modeling'),
    },
  host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint":'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)