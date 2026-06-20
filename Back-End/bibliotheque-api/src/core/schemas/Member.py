"""from pydantic import BaseModel, validator
# pydantic est une bibliothèque de validation de données pour Python, utilisée pour définir des modèles de données et valider les données d'entrée
#  dans les applications FastAPI.

class MemberBase(BaseModel):
    member_id: int = None
    last_name: str
    first_name: str
    email: str
    phone_number: str
    caution: bool
    opinion_id: int = None

class MemberUpdate(BaseModel):
    pass

    
class MemberCreate(MemberBase):
    pass
class Member(MemberBase):

    @validator("member_id", pre=True)
    def member_id_is_primary_key(cls, value):
        return value


class Config:
        orm_mode = True
    

"""