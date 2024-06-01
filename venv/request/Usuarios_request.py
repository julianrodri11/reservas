from pydantic import BaseModel,Field
from typing import Optional
from datetime import date, datetime, time, timedelta



class UsuariosRequest(BaseModel):
    id_usuario:Optional[int]=None
    nombres:str         =   Field(min_length=3,max_length=25)
    apellidos:str       =   Field(min_length=3,max_length=25)
    fecha_nacimiento:date
    tipo_documento:int  =   Field(gt=0,lt=10)
    documento:str       =   Field(min_length=3,max_length=15)
    tipo_usuario:int    =   Field(gt=0,lt=9)