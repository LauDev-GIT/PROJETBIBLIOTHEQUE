"""import datetime
from pydantic import BaseModel, validator
# pydantic est une bibliothèque de validation de données pour Python, utilisée pour définir des modèles de données et valider les données d'entrée
#  dans les applications FastAPI.

class BookBase(BaseModel):
    book_id: int = None 
    title : str
    description : str
    number_of_pages: int = None
    publication_date: datetime
    isbn : str
    archive : bool
    
    author_id: int = None

    editor_id: int = None

class BookUpdate(BaseModel):
        pass

class BookCreate(BookBase):
        pass

class Book(BookBase):

        @validator("book_id", pre=True)
        def book_id_is_primary_key(cls, value):
            return value


class Config:
        orm_mode = True
        

"""