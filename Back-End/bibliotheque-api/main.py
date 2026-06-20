from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api import api
from src.core.database.database import Base, engine

origins = [
    "http://localhost:4200"
]

app = FastAPI(title="Bibliotheque API",
              description="API pour la gestion de la bibliothèque",
              version="à déterminer",
              contact={
                  "name": "Support Bibliotheque API",
                  "email": "support@bibliotheque-api.com"
              },
              license_info={
                  "name": "MIT License",
                  "url": "https://opensource.org/licenses/MIT"
              })

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
app.include_router(api.routeur,prefix='/api')
# cette ligne est à décommenter pour créer les tables dans la base de données
# Base.metadata.create_all(bind=api.engine)
Base.metadata.create_all(engine)
