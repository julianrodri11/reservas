from fastapi import HTTPException, Request
from fastapi.security.http import HTTPAuthorizationCredentials
from jwt import encode,decode
from fastapi.security import HTTPBearer



def crear_token(data:dict):
    token:str= encode(payload=data,key="my_secret_key",algorithm="HS256")
    return token

def validar_token(token:str)->dict:
    data:str = decode(token,key="my_secret_key", algorithms=['HS256'])
    return data



class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data=validar_token(auth.credentials)
        if data['correo'] != "julianrodri11@gmail.com":
            raise HTTPException(status_code=403,detail="Credenciales invalidas")