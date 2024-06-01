from pydantic import BaseModel,Field,validate_email



class LoginRequest(BaseModel):
    correo:str =Field(min_length=3,max_length=30 )
    contrasena:str=Field(min_length=3,max_length=12 )
   