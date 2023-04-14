from pydantic import BaseModel
from decimal import Decimal
from .stores import StoreSchema
from backend.utilities.fields.uuid_type import UUIDType
from typing import Optional

class ItemSchema(BaseModel):
    id: UUIDType
    name: str
    price: Decimal
    store_id: UUIDType

    class Config:
        orm_mode = True

class ItemUpdateSchema(BaseModel):
    name: Optional[str]
    price: Optional[Decimal]

    class Config:
        orm_mode = True


class ItemDetailSchema(BaseModel):
    id: UUIDType
    name: str
    price: Decimal
    store: StoreSchema

    class Config:
        orm_mode = True