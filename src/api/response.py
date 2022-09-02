import json
from custom_encoder import CustomEncoder

def buildResponse(statusCode, body=None):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }

    if body:
        response["body"] = json.dumps(body, cls=CustomEncoder)

    return response