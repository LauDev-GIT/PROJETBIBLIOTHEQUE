from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Copy import Copy
from src.core.service import copyService

routeur = APIRouter()

# récupération de tous les copies en base de données
@routeur.get("/", response_model=list[Copy])
async def get_all_copies(db : Session = Depends(get_db)):
    return copyService.get_all_Copies(db)