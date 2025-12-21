from pydantic import BaseModel, Field


class PostgreCredentials(BaseModel):
    drivername: str = Field(default="postgresql+psycopg2")
    username: str
    password: str
    host: str
    port: int
    database: str
