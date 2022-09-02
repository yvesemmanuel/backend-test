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
    updateKey, updateValue = requestBody["updateKey"], requestBody["updateValue"]

    try:
        response = table.update_item(
            Key={
                "_id": post_id
            },
            UpdateExpression="set %s = :value" % updateKey,
            ExpressionAttributeValues={
                ":value": updateValue
            },
            ReturnValues="UPDATED_NEW"
        )

        body = {
            "Operation": "Update post",
            "Message": "Sucess",
            "UpdateAttributes": response
        }

        return buildResponse(200, body)
    except:
        logger.exception("Error handling here.")
