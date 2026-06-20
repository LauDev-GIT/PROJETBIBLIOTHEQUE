"""from sqlalchemy import Column, ForeignKey, Integer, String, Date,PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base

Représentation d'un emprunt


class Borrowing(Base):
    
    __tablename__ = "Borrowing"

    borrowing_id = Column(Integer,index=True, autoincrement=True)
    statut = Column(String(144), nullable=False)
    borrow_date = Column(Date,  nullable=False)
    return_date = Column(Date,  nullable=False)

    
    member_id = Column(Integer, ForeignKey('Member.member_id'))
    Member = relationship("Member", back_populates="borrowings")  # Relation avec le modèle Member

    copy_id = Column(Integer, ForeignKey('Copy.copy_id'))
    copies = relationship("Copy", back_populates="borrowings")  # Relation avec le modèle Copy

    __table_args__ = (PrimaryKeyConstraint('borrowing_id'), {})
"""