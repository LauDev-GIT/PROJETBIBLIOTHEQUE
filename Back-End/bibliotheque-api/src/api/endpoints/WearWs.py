from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Wear import Wear
from src.core.service import wearService


routeur = APIRouter()

@routeur.get("/", response_model=list[Wear])
async def get_all_wears(db : Session = Depends(get_db)):
    return wearService.get_all_Wears(db)

# @routeur.get("/{id}",response_model=Wear)
# async def get_wear_by_id(id: int):
#     print('test')
#     return wearService.get_Wear_by_id(db, id)