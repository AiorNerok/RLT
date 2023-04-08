from pydantic import BaseModel, validator, ValidationError
from datetime import datetime


class MessageSchemas(BaseModel):
    dt_from: str
    dt_upto: str
    group_type: str

    @validator("dt_from")
    def dt_from_validator(cls, v: str) -> str:
        if datetime.fromisoformat(v):
            return v
        raise ValueError("Invalid dt_from. dt_from can be iso format")

    @validator("dt_upto")
    def dt_upto_validator(cls, v: str) -> str:
        if datetime.fromisoformat(v):
            return v
        raise ValueError("Invalid dt_upto. dt_upto can be iso format")

    @validator("group_type")
    def group_type_validation(cls, v: str) -> str:
        if v.strip() in ("hour", "day", "month"):
            return v
        raise ValueError(
            """
                        Invalid group_type key. 
                        group_type can contain the following values:
                        - hour
                        - day 
                        - month
            """
        )


class ItemsSchemas(BaseModel):
    value: str
    dt: str
