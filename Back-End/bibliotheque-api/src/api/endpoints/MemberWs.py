from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session


from src.core.database.database import get_db
from src.core.schemas.Member import Member
from src.core.service import MemberService


routeur = APIRouter()

# récupération de tous les membres en base de données
@routeur.get("/", response_model=list[Member])

async def get_all_members(db: Session = Depends(get_db)):
    return MemberService.get_all_members(db)
