from fastapi import FastAPI
from src.auth.router import auth
from src.config.setup import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.URL_PREFIX + '/docs',
    redoc_url=settings.URL_PREFIX + '/redoc',
    openapi_url=settings.URL_PREFIX + '/openapi.json'
)

app.include_router(auth, prefix="/authentication/api/v1")