from pydantic import BaseModel

class DadosSchema(BaseModel):
    text : str

    class Config:
        from_attributes = True