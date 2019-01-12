from django.conf import settings
from settings import staging
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = staging.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = staging.MEDIAFILES_LOCATION
