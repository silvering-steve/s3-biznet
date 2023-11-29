import uvicorn

from app.settings.config import (
    APP_HOST,
    APP_PORT,
    APP_STAGE
)

if __name__ == '__main__':
    uvicorn.run("app:app", port=APP_PORT, host=APP_HOST, reload=APP_STAGE)