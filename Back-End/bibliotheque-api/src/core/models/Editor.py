"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from src.core.database.database import Base


 Représentaion d'un éditeur

class Editor(Base):
  
    __tablename__ = "Editor"

    editor_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    name = Column(String(144), nullable=False)
    books = relationship("Book")  # Relation avec le modèle Book, en utilisant le champ "editor" défini dans le modèle Book


    __table_args__ = (PrimaryKeyConstraint('editor_id'), {},)"""