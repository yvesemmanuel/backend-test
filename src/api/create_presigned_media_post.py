import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_presigned_media(bucket_name, object_name, fields=None, conditions=None, expiration=3600):
    s3_client = boto3.client("s3")

    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except:
        logger.exception("Error handling here.")

    # presigned URL and required fields
    return response
