from fastapi import FastAPI

app = FastAPI()

from routes.dados_router import dados_router

app.include_router(dados_router)
