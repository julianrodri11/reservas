from pydantic import BaseModel
from typing import Optional
from datetime import date


class TipoUsuarioResponse(BaseModel):
    id:Optional[int]=None
    nombre:str