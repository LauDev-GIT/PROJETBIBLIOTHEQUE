"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from src.core.database.database import Base


 Représentaion d'une image

class Picture(Base):
  
    __tablename__ = "Picture"

    picture_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    image_data = Column(String(144), nullable=False)
    books = relationship("Book")  # Relation avec le modèle Book, en utilisant le champ "picture" défini dans le modèle Book


    __table_args__ = (PrimaryKeyConstraint('picture_id'), {},)"""