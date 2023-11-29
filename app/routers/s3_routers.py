from typing import Annotated

from ..controllers.s3_controllers import S3Resources

from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()


@router.get("/check_health", tags=["Check"])
async def check_health():
    return await S3Resources.check_health()


@router.get("", tags=["Info"])
async def get_all_buckets():
    return await S3Resources.get_all_buckets()


@router.get("/{bucket}/{prefix:path}", tags=["Info"])
async def get_all_objects(bucket: str, prefix: str = None, file_type: str = None):
    return await S3Resources.get_all_objects_in_bucket(bucket, prefix, file_type)


@router.post("", tags=["Upload"])
async def upload_file(
        bucket: Annotated[str, Form()],
        prefix: Annotated[str, Form()] = None,
        filename: Annotated[str, Form()] = None,
        files: list[UploadFile] = File(...)
):
    return await S3Resources.upload_files(bucket, prefix, filename, files)
