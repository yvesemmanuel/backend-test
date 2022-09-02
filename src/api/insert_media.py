import boto3
import logging
from response import buildResponse
from create_presigned_media_post import create_presigned_post

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_resource = boto3.resource("s3")
bucketName = "nina-crud-bucket"

def insert_media(id, post_id, data):
    key = str(id) + post_id

    pass