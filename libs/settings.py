from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    Field,
)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.local")
    open_ai_key: str = Field(env="OPEN_AI_KEY")
    open_ai_base_url: str = Field(env="OPEN_AI_BASE_URL")
    kql_connection_string: str = Field(env="KQL_CONNECTION_STRING")

settings = Settings()