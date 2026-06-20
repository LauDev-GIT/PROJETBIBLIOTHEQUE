from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Picture import Picture
from src.core.service import pictureService

routeur = APIRouter()

@routeur.get("/", response_model=list[Picture])
async def get_all_pictures(db : Session = Depends(get_db)):
    return pictureService.get_all_Pictures(db)

# @routeur.get("/{id}",response_model=Picture)
# async def get_picture_by_id(id: int):
#     print('test')
#     return pictureService.get_Picture_by_id(db, id)