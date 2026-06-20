from pydantic import BaseModel, validator
# pydantic est une bibliothèque de validation de données pour Python, utilisée pour définir des modèles de données et valider les données d'entrée
#  dans les applications FastAPI.


class OpinionBase(BaseModel):
    opinion_id: int = None
    description: str

   
class OpinionUpdate(BaseModel):
    pass

class OpinionCreate(OpinionBase):
    pass

class Opinion(OpinionBase):

    @validator("opinion_id", pre=True)
    def opinion_id_is_primary_key(cls, value):
        return value


class Config:
        orm_mode = True