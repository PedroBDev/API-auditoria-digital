from fastapi import APIRouter, Depends, UploadFile, File
from dependencies.dependencies import pegar_sessao
from models.models import Conteudo
from schemas.schemas import DadosSchema
from services.service_whatsapp import processar_conversa

'''o APIRouter é utilizado para organizar as rotas da aplicação,
permitindo que sejam agrupadas por funcionalidade ou recurso.'''

dados_router = APIRouter(prefix="/dados", tags=["dados"])

#aqui serão implementadas as rotas para cadastrar e consultar os dados
@dados_router.post("/cadastro")
async def cadastrar_dados(file: UploadFile = File(...), session=Depends(pegar_sessao)):
    #implementação da lógica para cadastrar os dados
    
    conteudo = await file.read()
    texto = conteudo.decode("utf-8") 
    processar_conversa(texto)

    #exemplo de resposta
    return {"message": "Dados cadastrados com sucesso!"}

@dados_router.get("/consulta")
async def consultar_dados(session=Depends(pegar_sessao)):
    return session.query(Conteudo).order_by(Conteudo.data.desc(), Conteudo.hora.desc()).all()
    