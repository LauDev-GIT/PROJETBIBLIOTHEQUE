from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db
from src.core.schemas.Book import Book
from src.core.service import bookService


routeur = APIRouter()

@routeur.get("/", response_model=list[Book])
async def get_all_books(db : Session = Depends(get_db)):
    return bookService.get_all_Books(db)
