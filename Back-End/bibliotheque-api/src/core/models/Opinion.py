from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base



"""
 Représentaion d'un avis
"""
class Opinion(Base):
  
    __tablename__ = "Opinion"

    opinion_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    description = Column(String(144), nullable=False)
    

    __table_args__ = (PrimaryKeyConstraint('opinion_id'), {},)




