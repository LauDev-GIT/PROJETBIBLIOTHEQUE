"""from pydantic import BaseModel, validator

class AuthorBase(BaseModel):
    author_id: int = None
    first_name: str
    last_name: str
    biography: str
    nationality: str



class AuthorUpdate(BaseModel):
    pass

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):

    @validator("author_id", pre=True)
    def author_id_is_primary_key(cls, value):
        return value
    
class Config:
        orm_mode = True
    """