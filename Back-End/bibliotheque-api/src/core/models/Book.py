"""from sqlalchemy import Column, String,ForeignKey,Integer,Boolean,Date,PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base


Représentation d'un livre


class Book(Base):

    __tablename__ = "Book"

    book_id = Column(Integer,index=True,nullable=False, autoincrement=True)
    title = Column(String(144), nullable=False)
    description = Column(String(288), index=True, nullable=False)
    number_of_pages = Column(Integer, nullable=False)
    publication_date = Column(String(144), nullable=False)
    isbn = Column(String(144), nullable=False)
    archive = Column(Boolean, nullable=False)
    
    author_id = Column(Integer, ForeignKey('Author.author_id'), nullable=False)  # Clé étrangère vers Author
    author = relationship("Author")  # Relation avec le modèle Author, en utilisant le champ "author_id" défini dans le modèle Book

    editor_id = Column(Integer, ForeignKey('Editor.editor_id'), nullable=False)  # Clé étrangère vers Editor
    editor = relationship("Editor")  # Relation avec le modèle Editor, en utilisant le champ "editor_id" défini dans le modèle Book


    pictures = relationship("Picture")  # Relation avec le modèle Image, en utilisant le champ "book" défini dans le modèle Image
    genres = relationship("Genre", secondary="book_genre", back_populates="books")  # Relation avec le modèle Genre, en utilisant la table d'association "book_genre" et le champ "books" défini dans le modèle Genre
    copy = relationship("Copy")  # Relation avec le modèle Borrowing, en utilisant le champ "borrowing_id" défini dans le modèle Book

    __table_args__ = (PrimaryKeyConstraint('book_id'), {},)

"""