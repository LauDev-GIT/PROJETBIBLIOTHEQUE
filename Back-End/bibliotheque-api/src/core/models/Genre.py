"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from src.core.database.database import Base


 Représentaion d'un genre


class Genre(Base):
  
    __tablename__ = "Genre"

    genre_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    name = Column(String(144), nullable=False)
    books = relationship("Book")  # Relation avec le modèle Book, en utilisant le champ "genre" défini dans le modèle Book


    __table_args__ = (PrimaryKeyConstraint('genre_id'), {},)"""