import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY=os.getenv("ACCESS_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
ENDPOINT_URL=os.getenv("ENDPOINT_URL")

APP_HOST=os.getenv("APP_HOST")
APP_PORT=int(os.getenv("APP_PORT"))

APP_STAGE = True if os.getenv("APP_STAGE") == "DEV" else False
