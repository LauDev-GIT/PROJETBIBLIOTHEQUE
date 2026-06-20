"""from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from src.core.database.database import Base


 Représentaion d'un stock


class Stock(Base):
  
    __tablename__ = "Stock"

    stock_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    location = Column(String(144), nullable=False)
    copies = relationship("Copy")  # Relation avec le modèle Book, en utilisant le champ "stock" défini dans le modèle Book


    __table_args__ = (PrimaryKeyConstraint('stock_id'), {},)"""