from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db
from src.core.schemas.Borrowing import Borrowing
from src.core.service import BorrowingService


routeur = APIRouter()

# récupération de tous les emprunts en base de données
@routeur.get("/", response_model=list[Borrowing])
async def get_all_borrowings(db: Session = Depends(get_db)):
    return BorrowingService.get_all_borrowings(db)