from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base 


# SQL_ALCHEMY_DATABASE_URL = "mariadb://mariadbconnector://<notreuser>:<notrePassword>@<Host>/<db>"


# Création du moteur sqlAchemy
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# connection = engine.connect()
# Conception de la session de base de données
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()