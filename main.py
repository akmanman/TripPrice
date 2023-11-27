from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from schema import Schema, Use, SchemaError, Optional
from handler import handle

app = Flask(__name__)
api = Api(app)


class RequestHandler(Resource):
    def post(self):
        schema = Schema(
            {
                "method": Use(str),
                Optional("params"): dict
            },
            ignore_extra_keys=True
        )
        try:
            data = schema.validate(request.json)
        except SchemaError as e:
            raise e

        method = data["method"]
        params = data["params"]
        res = handle(method, params)
        return jsonify(res)


api.add_resource(RequestHandler, "/api/v1/get_info")
