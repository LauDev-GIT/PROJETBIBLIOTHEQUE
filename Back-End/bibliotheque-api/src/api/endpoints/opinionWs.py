from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db
from src.core.schemas.Opinion import Opinion
from src.core.service import opinionService


routeur = APIRouter()

# @routeur.get("/")
# async def hello_world():
#    return {"message": "Liste des avis"}

# récupération de tous les avis en base de données
@routeur.get("/", response_model=list[Opinion])
async def get_all_opinions(db : Session = Depends(get_db)):
    return opinionService.get_all_opinions(db)
    

# récupération d'un avis par son id
@routeur.get("/{id}",response_model=Opinion)
async def get_opinion_by_id(id: int):
  
  print('test')

# modification d'un avis en base de données
@routeur.put("/{id}")
async def update_opinion_by_id(id: int, opinion: Opinion):

    print('cela est ok pour moi')
#    return {"message": f"Mettre à jour l'avis avec l'id {id}", "opinion": opinion}

# suppression d'un avis en base de données
@routeur.delete("/{id}")
async def delete_opinion_by_id(id: int):
    print('cela fonctionne bien')
#    return {"message": f"Supprimer l'avis avec l'id {id}"}


# création d'un nouvel avis en base de données
@routeur.post("/")
async def create_opinion(opinion: Opinion):
    print ('test')