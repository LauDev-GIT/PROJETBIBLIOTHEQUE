"""from sqlalchemy import Column, Integer, String,Boolean,PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from src.core.database.database import Base


    Représentaion d'une copie a finir rajouter les cléfs étrangères
    

class Copy(Base):
  
    __tablename__ = "Copy"

    copy_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    number_of_copies = Column(Integer, nullable=False)
    available = Column(Boolean, nullable=False)  # Champ pour indiquer si la copie est disponible ou non
    book_id = Column(Integer, nullable=False)  # Clé étrangère vers le livre
    stock_id = Column(Integer, nullable=False)  # Clé étrangère vers le stock
    wear_id = Column(Integer, nullable=False)  # Clé étrangère vers l'usure
    books = relationship("Book")  # Relation avec le modèle Book, en utilisant le champ "copy" défini dans le modèle Book
    stocks = relationship("Stock")  # Relation avec le modèle Stock, en utilisant le champ "copy" défini dans le modèle Stock
    wears = relationship("Wear")  # Relation avec le modèle Wear, en utilisant le champ "copy" défini dans le modèle Wear


    __table_args__ = (PrimaryKeyConstraint('copy_id'), {},)"""