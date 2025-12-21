from pydantic import BaseModel, Field

class SqliteCredential(BaseModel):
    drivername: str = Field(default="sqlite")
    database: str = Field(default="../covid.db")
