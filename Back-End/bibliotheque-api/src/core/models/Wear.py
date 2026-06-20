"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base


Représentation d'une usure

class Wear(Base):
  
    __tablename__ = "Wear"

    wear_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    
    copies = relationship("Copy")  # Relation avec le modèle Copy, en utilisant le champ "wear" défini dans le modèle Copy


    __table_args__ = (PrimaryKeyConstraint('wear_id'), {},)"""