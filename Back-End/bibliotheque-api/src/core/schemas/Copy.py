"""from pydantic import BaseModel, validator

class CopyBase(BaseModel):
    copy_id: int = None
    number_of_copies: int
    available: bool = True  # Champ pour indiquer si la copie est disponible ou non
    book_id: int = None
    stock_id: int = None
    wear_id: int = None
    

class CopyUpdate(BaseModel):
    pass

class CopyCreate(CopyBase):
    pass

class Copy(CopyBase):
    @validator("copy_id", pre=True)
    def copy_id_is_primary_key(cls, value):
        return value

class Config:
        orm_mode = True
        """     