# API Auditoria Digital

API desenvolvida em FastAPI para cadastro e consulta de conteúdos, usando SQLite como banco de dados e SQLAlchemy como ORM.

## Estrutura do projeto

- `main.py` - aplicação FastAPI principal e inclusão do roteador.
- `routes/dados_router.py` - rotas de cadastro e consulta de dados.
- `models/models.py` - definição do modelo `Conteudo`, conexão com SQLite e base do SQLAlchemy.
- `schemas/schemas.py` - esquema Pydantic para validação dos dados de entrada.
- `dependencies/dependencies.py` - gerenciador de sessão do banco para injeção de dependência.
- `alembic/` - configuração e migrations do Alembic.
- `database/db.sqlite3` - arquivo SQLite local usado pela aplicação.

## Dependências principais

- `fastapi`
- `uvicorn`
- `SQLAlchemy`
- `pydantic`
- `alembic`

Todas as dependências estão listadas em `requirements.txt`.

## Instalação

1. Crie o ambiente virtual:

```powershell
python -m venv venv
```

2. Ative o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Executar a aplicação

No diretório do projeto:

```powershell
python -m uvicorn main:app --reload
```

A API ficará disponível em:

- `http://127.0.0.1:8000`
- Documentação automática: `http://127.0.0.1:8000/docs`

## Endpoints

- `POST /dados/cadastro` - cadastra dados via JSON.
- `GET /dados/consulta` - retorna todos os registros ordenados por data e hora.

### Exemplo de payload para cadastro

```json
{
  "text": "Meu texto de auditoria"
}
```

## Banco de dados

A aplicação usa SQLite local em `database/db.sqlite3`.

Para aplicar migrações com Alembic:

```powershell
alembic upgrade head
```

## Observações

- O endpoint de cadastro já existe, mas a implementação atual retorna apenas uma mensagem de sucesso sem persistir o registro.
- Ajuste o modelo e a lógica de persistência em `routes/dados_router.py` conforme necessário.
