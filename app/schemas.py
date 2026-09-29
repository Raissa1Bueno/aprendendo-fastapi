
from pydantic import BaseModel

class Message(BaseModel):
    message: str

class AdicionarUsuario(BaseModel):
    usuario: str
    email: str
    password: str
    idade: int

class ObterUsuario(AdicionarUsuario):
    codigo: int
