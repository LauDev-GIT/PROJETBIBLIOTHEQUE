"""from pydantic import BaseModel, validator

class WearBase(BaseModel):
    wear_id: int = None
    name: str

class WearUpdate(BaseModel):
    pass

class WearCreate(WearBase):
    pass

class Wear(WearBase):
    @validator("picture_id", pre=True)
    def picture_id_is_primary_key(cls, value):
        return value

class Config:
        orm_mode = True
        
"""
        
