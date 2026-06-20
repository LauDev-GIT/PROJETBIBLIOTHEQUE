"""from sqlalchemy.orm import Session

from src.core.models.Stock import Stock

# on retourne tout le stock de la base de données
def get_all_stocks(db : Session):
    return db.query(Stock).all()"""