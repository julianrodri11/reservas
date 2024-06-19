from pydantic import BaseModel,Field
from typing import Optional
from datetime import date, datetime, time, timedelta



class UsuariosRequest(BaseModel):
    id_usuario:Optional[int]=None
    primer_nombre:str         =   Field(min_length=3,max_length=25)
    segundo_nombre:str         =   Field(min_length=3,max_length=25)
    primer_apellido:str       =   Field(min_length=3,max_length=25)
    segundo_apellido:str       =   Field(min_length=3,max_length=25)
    #fecha_nacimiento:date
    tipo_documento:int  =   Field(gt=0,lt=10)
    documento:str       =   Field(min_length=3,max_length=25)
    tipo_usuario:int    =   Field(gt=0,lt=9)