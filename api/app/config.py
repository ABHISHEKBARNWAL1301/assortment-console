from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_service: str
    uvicorn_workers: str
    app_port: str
    redis_service: str
    redis_port: str
    redis_db: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()







# class Settings(BaseSettings):
#     postgres_user: str = "abhishek"
#     postgres_password: str = "abhishek"
#     postgres_db: str = "newsearchdb"
#     postgres_service: str = "localhost"
#     uvicorn_workers: str = '2'
#     app_port: str = '8000'
#     redis_service: str = "localhost"
#     redis_port: str = '6379'
#     redis_db: str = '5'

#     class Config:
#         env_file = ".env"


# settings = Settings()









