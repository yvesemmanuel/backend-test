import boto3
import json
import logging
import uuid
from response import buildResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

tableName = "blog-post"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    requestBody = json.loads(event["body"])

    try:
        new_item = requestBody
        new_item["_id"] = str(uuid.uuid1())

        table.put_item(Item=new_item)
        body = {
            "Operation": "Save new post",
            "Message": "Success",
            "Item": requestBody
        }

        return buildResponse(200, body)
    except:
        logger.exception("Error handling here.")