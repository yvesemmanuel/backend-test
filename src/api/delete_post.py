import boto3
import json
import logging
from response import buildResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

tableName = "blog-post"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    requestBody = json.loads(event["body"])
    post_id = requestBody["_id"]

    try:
        response = table.delete_item(
            Key={
                "_id": post_id
            },
            ReturnValues="ALL_OLD"
        )
        body = {
            "Operation": "Delete post",
            "Message": "Success",
            "deletedPost": response
        }

        return buildResponse(200, body)

    except:
        logger.exception("Error handling here.")