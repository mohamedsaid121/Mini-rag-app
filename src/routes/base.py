from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1"
)



@base_router.get("/")
async def welcome(App_settings: Settings = Depends(get_settings)):
    APP_Name = App_settings.App_Name
    App_Version = App_settings.App_Version

    return {
        "message": "Hello all",
        "app_name": APP_Name,
        "app_version": App_Version
        } 