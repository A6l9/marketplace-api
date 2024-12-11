from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DBSettings(BaseSettings):

    db_host: str = Field(alias='dbhost')
    db_port: int = Field(alias='dbport')
    db_name: str = Field(alias='dbname')
    db_user: str = Field(alias='dbuser')
    db_password: str = Field(alias='dbpassword')

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
