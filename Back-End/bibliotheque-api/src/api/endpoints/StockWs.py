from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db

from src.core.schemas.Stock import Stock
from src.core.service import stockService

routeur = APIRouter()

@routeur.get("/", response_model=list[Stock])
async def get_all_stocks(db : Session = Depends(get_db)):
    return stockService.get_all_Stocks(db)

# @routeur.get("/{id}",response_model=Stock)
# async def get_stock_by_id(id: int):
#     print('test')
#     return stockService.get_Stock_by_id(db, id)