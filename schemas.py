from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class CategoryEnum(str, Enum):
    FINISHED = "finished"
    SEMI_FINISHED = "semi-finished"
    RAW = "raw"


class UnitEnum(str, Enum):
    MTR = "mtr"
    MM = "mm"
    LTR = "ltr"
    ML = "ml"
    CM = "cm"
    MG = "mg"
    GM = "gm"
    UNIT = "unit"
    PACK = "pack"


class ProductCreate(BaseModel):
    name: str = Field(max_length=100)
    category: CategoryEnum
    description: Optional[str] = Field(default=None, max_length=250)
    product_image: Optional[str] = None
    sku: str = Field(max_length=100)
    unit_of_measure: UnitEnum
    lead_time: int


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=100)
    category: Optional[CategoryEnum] = None
    description: Optional[str] = Field(default=None, max_length=250)
    product_image: Optional[str] = None
    sku: Optional[str] = Field(default=None, max_length=100)
    unit_of_measure: Optional[UnitEnum] = None
    lead_time: Optional[int] = None


class ProductResponse(BaseModel):
    product_id: int
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[str]
    sku: str
    unit_of_measure: UnitEnum
    lead_time: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

