from pydantic import BaseModel,Field
from typing import Optional


class TipoUsuarioRequest(BaseModel):
    id:Optional[int]=None
    nombre:str=Field(min_length=3,max_length=8)
   