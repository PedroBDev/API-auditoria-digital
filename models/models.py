from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

#cria a conexão com o banco de dados
db = create_engine("sqlite:///./db.sqlite3") 

#cria a base de dados
Base = declarative_base()

#cria as tabelas
class Conteudo(Base):
    __tablename__ = "conteudos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    hora = Column(DateTime, nullable=False)
    remetente = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    
    def __init__(self, data, hora, remetente, conteudo):
        self.data = data
        self.hora = hora
        self.remetente = remetente
        self.conteudo = conteudo
        
        