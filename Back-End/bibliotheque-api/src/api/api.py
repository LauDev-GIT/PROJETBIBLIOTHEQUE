from fastapi import APIRouter
from src.api.endpoints import opinionWs
""",BorrowingWs,MemberWs,BookWs,CopyWs,EditorWs,AuthorWs,WearWs,GenreWs,PictureWs,StockWs
"""




routeur = APIRouter()

routeur.include_router(opinionWs.routeur, prefix="/Avis",
                      tags=["Avis"],

                      responses={404: {"description": "impossible de trouver les avis"}})
"""
routeur.include_router(MemberWs.routeur, prefix="/Adherent",
                      tags=["Adhérent"],
                     responses={404: {"description": "impossible de trouver les adhérents"}})
 
routeur.include_router(BorrowingWs.routeur, prefix="/Emprunt",
                     tags=["Emprunt"],
                      responses={404: {"description": "impossible de trouver les emprunts"}})

Ce module contient la définition de l'API de la bibliothèque,
en utilisant FastAPI. Il regroupe les différents endpoints pour les avis, 
les adhérents et les emprunts, facilitant ainsi 
l'organisation et la maintenance du code.

routeur.include_router(BookWs.routeur, prefix="/Livre",
                        tags=["Livre"],
                      responses={404: {"description": "impossible de trouver les livres"}})

routeur.include_router(CopyWs.routeur, prefix="/Exemplaire",
                        tags=["Exemplaire"],
                      responses={404: {"description": "impossible de trouver les exemplaires"}})

routeur.include_router(EditorWs.routeur, prefix="/Editeur",
                        tags=["Editeur"],
                        responses={404: {"description": "impossible de trouver les éditeurs"}})

routeur.include_router(AuthorWs.routeur, prefix="/Auteur",
                        tags=["Auteur"],
                        responses={404: {"description": "impossible de trouver les auteurs"}})

routeur.include_router(WearWs.routeur, prefix="/Usure",
                        tags=["Usure"],
                        responses={404: {"description": "impossible de trouver les usures"}})

routeur.include_router(GenreWs.routeur, prefix="/Genre",
                        tags=["Genre"],
                        responses={404: {"description": "impossible de trouver les genres"}})

routeur.include_router(PictureWs.routeur, prefix="/Image",
                        tags=["Image"],
                        responses={404: {"description": "impossible de trouver les images"}})

routeur.include_router(StockWs.routeur, prefix="/Stock",
                        tags=["Stock"],
                        responses={404: {"description": "impossible de trouver les stocks"}})

"""