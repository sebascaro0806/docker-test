from fastapi import Depends, FastAPI, APIRouter, Request
from fastapi.security import HTTPBasic, HTTPBearer

boards = APIRouter()
security = HTTPBearer()

app = FastAPI(
    title="API Test",
    description="API to manage users",
    version=1.0,
    docs_url='/boards/api/v1/docs',
    redoc_url='/boards/api/v1/redoc',
    openapi_url='/boards/api/v1/openapi.json'
)

@boards.get("/test", response_model=str)
def get_users():
    return "Hola Mundo test"

@boards.post("/test3", response_model=str)
def gettt(test: dict, request: Request):
    print(test)
    print(request.headers)
    print(request.client)
    print(request.json())
    return "Hola Mundo test"

@boards.get("/test4", response_model=str, dependencies=[Depends(security)])
def get_users():
    return "Hola Mundo test"

app.include_router(boards, prefix='/boards/api/v1')
