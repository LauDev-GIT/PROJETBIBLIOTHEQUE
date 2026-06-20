"""from sqlalchemy import  Integer,Column, String,Boolean,ForeignKey,PrimaryKeyConstraint
                   
from sqlalchemy.orm import relationship
from src.core.database.database import Base

Représentaion d'un Adherent
class Member(Base):

    __tablename__ = "Member"

    member_id = Column(Integer,index=True, autoincrement=True)
    last_name = Column(String(144), nullable=False)
    first_name = Column(String(144), nullable=False)
    email = Column(String(144), nullable=False)
    phone_number = Column(String(144), nullable=False)
    caution = Column(Boolean, nullable=False)
    
    
    opinion_id = Column(Integer, ForeignKey('Opinion.opinion_id'))
    Opinion = relationship("Opinion", back_populates="members")  # Relation avec le modèle Member
    
    borrowings = relationship("Borrowing")  # Relation avec le modèle Borrowing

    __table_args__ = (PrimaryKeyConstraint('member_id'), {})
"""