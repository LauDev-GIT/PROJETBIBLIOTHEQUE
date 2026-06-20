"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base



 Représentaion d'un auteur

class Author(Base):
  
    __tablename__ = "Author"

    author_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    first_name = Column(String(144), nullable=False)
    last_name = Column(String(144), nullable=False)
    biography = Column(String(288), nullable=False)
    nationality = Column(String(144), nullable=False)
    books = relationship("Book")  # Relation avec le modèle Book, en utilisant le champ "author" défini dans le modèle Book


    __table_args__ = (PrimaryKeyConstraint('author_id'), {},)"""