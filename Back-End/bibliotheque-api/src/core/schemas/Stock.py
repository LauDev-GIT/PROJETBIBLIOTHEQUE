"""from pydantic import BaseModel, validator

class StockBase(BaseModel):
    stock_id: int = None
    location: str

class StockUpdate(BaseModel):
    pass

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    @validator("picture_id", pre=True)
    def picture_id_is_primary_key(cls, value):
        return value
    
class Config:
        orm_mode = True
        
"""
        
