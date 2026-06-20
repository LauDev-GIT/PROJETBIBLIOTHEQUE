"""from sqlalchemy.orm import Session

from src.core.models.Book import Book

# on retourne tous les livres de la base de données
def get_all_books(db : Session):
    return db.query(Book).all()
    """