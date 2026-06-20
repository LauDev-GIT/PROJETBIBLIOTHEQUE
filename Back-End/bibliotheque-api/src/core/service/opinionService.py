from sqlalchemy.orm import Session

from src.core.models.Opinion import Opinion

# on retourne tous les avis de la base de données
def get_all_opinions(db : Session):
    return db.query(Opinion).all()
