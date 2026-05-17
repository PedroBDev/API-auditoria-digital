from models.models import db
from sqlalchemy.orm import sessionmaker

#utilizado para realizar as operações de leitura e escrita no banco de dados
'''precisamos fechar a sessão após o uso para evitar problemas de conexão, logo, 
essa função é um gerenciador de contexto que garante o fechamento da sessão após o uso'''

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()