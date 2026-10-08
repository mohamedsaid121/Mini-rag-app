from fastapi import APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1"
)



@base_router.get("/")
async def welcome():
    APP_Name = os.getenv("APP_NAME")
    App_Version = os.getenv("APP_VERSION")

    return {
        "message": "Hello all",
        "app_name": APP_Name,
        "app_version": App_Version
        } 