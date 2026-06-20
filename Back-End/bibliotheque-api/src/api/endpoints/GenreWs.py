from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Genre import Genre
from src.core.service import genreService

routeur = APIRouter()

@routeur.get("/", response_model=list[Genre])
async def get_all_genres(db : Session = Depends(get_db)):
    return genreService.get_all_Genres(db)

# @routeur.get("/{id}",response_model=Genre)
# async def get_genre_by_id(id: int):
#     print('test')
#     return genreService.get_Genre_by_id(db, id)