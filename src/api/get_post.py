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
        response = table.get_item(
            Key={
                "_id": post_id
            }
        )

        item = response.get("Item", None)

        if item is not None:
            return buildResponse(200, item)
        else:
            return buildResponse(404, {"Message": "Post {} not found.".format(post_id)})
    except:
        logger.exception("Error handling here.")
