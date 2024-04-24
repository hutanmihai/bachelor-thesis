import boto3
from botocore.client import BaseClient
from src.settings import settings


def s3_auth() -> BaseClient:
    s3 = boto3.client(
        service_name="s3", aws_access_key_id=settings.aws_access_key, aws_secret_access_key=settings.aws_secret_access_key, region_name="eu-central-1"
    )
    return s3
