""" from fastapi import FastAPI, Body
from models.TipoUsuarioDTO import TipoUsuarioDTO

app = FastAPI()

#ruta con query paramams CLAVE VALOR
@app.post('/crear_tipo_usuarios',tags=['Tipo Usuarios'])
def crear_tipo_usuarios(tipo_usuario: TipoUsuarioDTO):
    return {"message": "Controller para post QUERY PARAMS crear un tipo usuario", "data": tipo_usuario.dict()}
 """