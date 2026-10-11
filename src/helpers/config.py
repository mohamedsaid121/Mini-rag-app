from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    App_Name: str
    App_Version: str
    OpenAI_API_Key: str

    File_Allowed_Types: list
    File_Max_Size: int
    File_Default_Chunk_Size: int

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()