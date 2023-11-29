import io

import boto3

from ..error.exception import BucketNotFound, UploadFileFailed


class S3Client:
    def __init__(self, access_key: str, secret_key: str, endpoint: str) -> None:
        """
        Initialization for S3 Client
        """
        self.session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

        self.s3_resource = self.session.resource(
            "s3",
            endpoint_url=endpoint
        )

        self.s3_client = self.session.client(
            "s3",
            endpoint_url=endpoint
        )

    async def list_all_buckets(self) -> list[str]:
        """
        Get all buckets that available
        :return: List of bucket
        """
        return [buckets.name for buckets in self.s3_resource.buckets.all()]

    async def list_all_objects(self, bucket: str, prefix: str, file_type: str = None) -> list[str]:
        """
        Get all objects in certain buckets with some path or file type preference
        :param bucket:
        :param prefix:
        :param file_type:
        :return:
        """
        try:
            bucket = self.s3_resource.Bucket(bucket)

        except self.s3_resource.meta.client.exceptions.NoSuchBucket:
            raise BucketNotFound

        if not prefix:
            files = bucket.objects.all()

            if not file_type:
                return [file.key for file in files]

            return [file.key for file in files if file.key.endswith(file_type)]

        else:
            files = bucket.objects.filter(Prefix=prefix)

            if not file_type:
                return [file.key for file in files]

            return [file.key for file in files if file.key.endswith(file_type)]

    async def upload_file(self, bucket: str, prefix: str, filename: str, file: io.BytesIO) -> list[str]:
        path = f"{prefix}/{filename}" if prefix else filename

        self.s3_client.upload_fileobj(file, bucket, path)

        return {
            "status": True,
            "filename": filename,
            "url": path
        }
