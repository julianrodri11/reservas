from pydantic import BaseModel
from typing import Optional
from datetime import date


class UsuariosResponse(BaseModel):
    id_usuario:Optional[int]=None
    nombres:str         
    apellidos:str       
    fecha_nacimiento:date
    tipo_documento:int  
    documento:str       
    tipo_usuario:int    