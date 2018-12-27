from django.conf import settings
from settings import base
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = base.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = base.MEDIAFILES_LOCATION
