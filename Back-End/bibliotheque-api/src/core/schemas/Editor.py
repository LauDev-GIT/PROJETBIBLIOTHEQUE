"""from pydantic import BaseModel, validator


class EditorBase(BaseModel):
    editor_id: int = None
    name: str
    
class EditorUpdate(BaseModel):
    pass

class EditorCreate(EditorBase):
    pass

class Editor(EditorBase):

    @validator("editor_id", pre=True)
    def editor_id_is_primary_key(cls, value):
        return value

class Config:
        orm_mode = True
        
        """