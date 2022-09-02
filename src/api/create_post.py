import boto3
import json
import logging
import uuid
from insert_media import insert_media
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

        if "Medias" in new_item:
            medias = new_item["Medias"]
            del new_item["Medias"]

        ## here we should handle files submission to the S3 bucket after presigned it and save it's url to the Medias array field
        
        # for every media file encrypted to a string (as a base64 I suggest), send it to the the S3 bucket as a file from the post identified by new_item["_id"]
        for idx, media in enumerate(medias):
            insert_media(idx, new_item["_id"], media)


        table.put_item(Item=new_item)
        body = {
            "Operation": "Save new post",
            "Message": "Success",
            "Item": requestBody
        }

        return buildResponse(200, body)
    except:
        logger.exception("Error handling here.")