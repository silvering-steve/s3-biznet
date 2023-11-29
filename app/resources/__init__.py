from .s3_resources import S3Client

from app.settings.config import ACCESS_KEY, SECRET_KEY, ENDPOINT_URL

s3client = S3Client(ACCESS_KEY, SECRET_KEY, ENDPOINT_URL)
