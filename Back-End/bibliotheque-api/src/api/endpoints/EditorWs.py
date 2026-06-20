from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Editor import Editor
from src.core.service import editorService

routeur = APIRouter()

@routeur.get("/", response_model=list[Editor])
async def get_all_editors(db : Session = Depends(get_db)):
    return editorService.get_all_Editors(db)

# @routeur.get("/{id}",response_model=Author)
# async def get_editor_by_id(id: int):
#     print('test')
#     return editorService.get_Editor_by_id(db, id)