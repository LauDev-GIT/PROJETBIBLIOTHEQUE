"""from pydantic import BaseModel, validator


class PictureBase(BaseModel):
    picture_id: int = None
    image_data: str

class PictureUpdate(BaseModel):
    pass

class PictureCreate(PictureBase):
    pass


class Picture(PictureBase):

    @validator("picture_id", pre=True)
    def picture_id_is_primary_key(cls, value):
        return value

class Config:
        orm_mode = True
        
"""
        
