from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db
from src.core.schemas.Author import Author
from src.core.service import authorService

routeur = APIRouter()

@routeur.get("/", response_model=list[Author])
async def get_all_authors(db : Session = Depends(get_db)):
    return authorService.get_all_Authors(db)

# @routeur.get("/{id}",response_model=Author)
#async def get_author_by_id(id: int):
#    print('test')
#    return authorService.get_Author_by_id(db, id)

#@routeur.put("/{id}")
#async def update_author_by_id(id: int, author: Author):
#    print('cela est ok pour moi')
#    return {"message": f"Mettre à jour l'auteur avec l'id {id}", "author": author}