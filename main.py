from fastapi import FastAPI, Body,Depends
from typing import List
from pydantic import BaseModel
from fastapi.responses import JSONResponse
#from sqlalchemy.orm import sessionmaker,declarative_base

from request.TipoUsuario_request import TipoUsuarioRequest
from request.Usuarios_request import UsuariosRequest
from request.Login_request import LoginRequest
from responses.usuarios_response import UsuariosResponse
from config.jwt_manager import  crear_token
from config.jwt_manager import  JWTBearer
from config.conexion import conectar_db
from entidades.TipoUsuarios import TipoUsuarios,guardar,consultar


app = FastAPI()

app.title="Mi primera aplicación con FAST API"
app.version="1.0.0"

#Ruta estandar
@app.get('/',tags=['Home'])
def home():
    return "Home Controller Bienvenido a la API"




#LOGIN
#ruta con query paramams CLAVE VALOR COMO JSON O BODY
@app.post('/autenticacion',tags=['Login'])
def crear_usuarios_body(login:LoginRequest):
    if login.correo=='julianrodri11@gmail.com' and login.contrasena=='123':
        token: str = crear_token(login.dict())
        return JSONResponse(status_code=200, content=token)
    else:
        return {"Error":"Usuario no encontrado"}
        

#ruta con query paramams CLAVE VALOR
@app.post('/crear_tipo_usuarios',tags=['Tipo Usuarios'],dependencies=[Depends(JWTBearer())])
#@app.post('/crear_tipo_usuarios',tags=['Tipo Usuarios'])
def crear_tipo_usuarios(tipo_usuario: TipoUsuarioRequest):
    guardar(tipo_usuario.nombre)    
    return {"message": "Controller para post QUERY PARAMS crear un tipo usuario", "data": tipo_usuario.dict()}



#ruta con path parameter
@app.post('/consultar_usuarios/',tags=['Usuarios'])
def get_usuario_id(tipo_usuario: TipoUsuarioRequest):
    r:str=consultar(tipo_usuario.nombre)
    return r

#ruta con dos path paramateter
@app.get('/consultar_usuarios/{tipo_doc}/{id}',tags=['Usuarios'])
def get_usuario_tipo_doc_id(tipo_doc:str, id:int):
    return "parametros recibidos por PATH PARAMETER",{tipo_doc,id}

#ruta con query paramams CLAVE VALOR
@app.post('/crear_usuarios',tags=['Usuarios'])
def crear_usuarios(tipo_doc:str, id:int):
    return "Controller para post QUERY PARAMS ",{tipo_doc,id}

#ruta con query paramams CLAVE VALOR COMO JSON O BODY
@app.post('/crear_usuarios_body',tags=['Usuarios'])
def crear_usuarios_body(usuarios:UsuariosRequest):
    usuariosres:UsuariosResponse
    usuariosres = usuarios
    #return {"message": "Controller para post QUERY PARAMS BODY", "data": usuarios.nombres}
    #return {"message": "Controller para post QUERY PARAMS BODY", "data": usuarios}
    return usuariosres

@app.put('/actualizar_usuarios',tags=['Usuarios'])
def actualizar_usuarios():
    return "Controller para put "

@app.delete('/eliminar_usuarios',tags=['Usuarios'])
def eliminar_usuarios():
    return "Controller para delete "

@app.patch('/subir_usuarios',tags=['Usuarios'])
def usuarios():
    return "Controller para patch "
    
@app.patch('/subir_usuarios',tags=['Usuarios'])
def usuarios():
    return "Controller para patch "





@app.get('/enditades',tags=['Entidades'])
def get_all_entidades():
    return "Controller para get "

@app.get('/enditades_by_id',tags=['Entidades'])
def get_entidades_by_id():
    return "Controller para get entidades por id"

@app.post('/crear_entidades',tags=['Entidades'])
def create_entidades():
    return "Controller para post "

@app.put('/actualizar_entidades',tags=['Entidades'])
def actualizar_entidades():
    return "Controller para put "

@app.delete('/eliminar_entidades',tags=['Entidades'])
def eliminar_entidades():
    return "Controller para delete "

@app.patch('/subir_archivo_entidades',tags=['Entidades'])
def subir_entidades():
    return "Controller para patch "
