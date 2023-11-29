from .routers import *
from .resources import *

from fastapi import FastAPI


app = FastAPI()

app.include_router(s3_routers.router, prefix="/s3", tags=["S3"])
