"""import datetime
from pydantic import BaseModel, validator
# pydantic est une bibliothèque de validation de données pour Python, utilisée pour définir des modèles de données et valider les données d'entrée
#  dans les applications FastAPI.
#


class BorrowingBase(BaseModel):
    borrowing_id: int = None
    
    statut : str
    borrowing_date: datetime
    return_date: datetime
    member_id: int = None
    copy_id: int = None

class BorrowingUpdate(BaseModel):
    pass

class BorrowingCreate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):

    @validator("borrowing_id", pre=True)
    def borrowing_id_is_primary_key(cls, value):
        return value


class Config:
        orm_mode = True
        
"""
