from pydantic import BaseModel
from uuid import UUID
from backend.utilities.fields.uuid_type import UUIDType

class StoreSchema(BaseModel):
    id: UUIDType
    name: str

    class Config:
        orm_mode = True

class StoreUpdateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True