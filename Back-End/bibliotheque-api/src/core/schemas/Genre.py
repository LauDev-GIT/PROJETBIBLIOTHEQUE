"""from pydantic import BaseModel, validator

class GenreBase(BaseModel):
    genre_id: int = None
    name: str

class GenreUpdate(BaseModel):
    pass

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    @validator("genre_id", pre=True)
    def genre_id_is_primary_key(cls, value):
        return value

class Config:
        orm_mode = True
        
"""
        

