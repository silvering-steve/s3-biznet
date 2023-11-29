import io

from fastapi import UploadFile

from ..error.exception import DetailedHTTPException, ReadFileFailed
from ..resources import s3client

from starlette.responses import JSONResponse



class S3Resources:
    @staticmethod
    async def check_health() -> JSONResponse:
        try:
            return JSONResponse(
                status_code=200,
                content={
                    "content":
                        "Hello World"
                }
            )

        except Exception as e:
            raise DetailedHTTPException

    @staticmethod
    async def get_all_buckets() -> JSONResponse:
        try:
            return JSONResponse(
                status_code=200,
                content={
                    "content": {
                        "buckets": await s3client.list_all_buckets()
                    }
                }
            )

        except Exception as e:
            raise DetailedHTTPException

    @staticmethod
    async def get_all_objects_in_bucket(bucket: str, prefix: str, file_type: str = None) -> JSONResponse:
        try:
            return JSONResponse(
                status_code=200,
                content={
                    "content": {
                        "objects": await s3client.list_all_objects(bucket, prefix, file_type)
                    }
                }
            )

        except Exception as e:
            raise DetailedHTTPException

    @staticmethod
    async def upload_files(bucket: str, prefix: str, filename: str, files: list[UploadFile]):
        results = []

        try:
            for file in files:
                contents = file.file.read()

                temp_file = io.BytesIO()
                temp_file.write(contents)
                temp_file.seek(0)

                name = filename if filename else file.filename

                results.append(await s3client.upload_file(bucket, prefix, name, temp_file))

        except Exception as e:
            print(e)

            raise ReadFileFailed

        finally:
            temp_file.close()

        return JSONResponse(
            status_code=200,
            content={
                "content": {
                    "objects": results
                }
            }
        )
