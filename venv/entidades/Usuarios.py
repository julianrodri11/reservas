from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
from config.conexion import conectar_db
from sqlalchemy import create_engine
from request.Usuarios_request import UsuariosRequest

engine=conectar_db()

Base = declarative_base()



class Usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario= Column(Integer, primary_key=True)
    primer_nombre= Column(String(25), nullable=False)
    segundo_nombre= Column(String(25), nullable=True)
    primer_apellido= Column(String(25), nullable=False)
    segundo_apellido= Column(String(25), nullable=True)
    #fecha_nacimiento= Column(String(25), nullable=False)
    tipo_documento= Column(String(25), nullable=False)
    documento= Column(String(25), nullable=False)
    tipo_usuario= Column(String(25), nullable=False)

#crear las tablas en caso de ser necesario
Base.metadata.create_all(engine)



def guardar_usuarios(usuariorequest:UsuariosRequest):  
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()

    registro=Usuarios(primer_nombre=usuariorequest.primer_nombre,segundo_nombre=usuariorequest.segundo_nombre,primer_apellido=usuariorequest.primer_apellido,segundo_apellido=usuariorequest.segundo_apellido,tipo_documento=usuariorequest.tipo_documento,documento=usuariorequest.documento,tipo_usuario=usuariorequest.tipo_usuario)
    
    session.add(registro)
    session.commit()
    session.close()



def consultar_usuarios(nombre:str,apellido:str,documento:str):  
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()

    # Obtiene un registro específico por nombre
    #usuario = session.query(Usuarios).filter_by(primer_nombre=nombre).first()

    # Crear un filtro condicional
    filtro = []

    if nombre:
        filtro.append(Usuarios.primer_nombre == nombre)

    if apellido:
        filtro.append(Usuarios.primer_apellido == apellido)
    
    if documento:
        filtro.append(Usuarios.documento == documento)
    
    # Aplicar el filtro a la consulta
    if filtro:
        usuario = session.query(Usuarios).filter(*filtro).all()
    else:
        usuario = session.query(Usuarios).all()

    # Si el registro existe, imprime la información
    if usuario:
        session.close()
        return list(usuario)
        #return {"id":usuario.id_usuario,"nombre":usuario.primer_nombre}
    else:
        session.close()
        return ("Usuario no encontrado")
    


def actualizar_usuarios_controller(usuariorequest:UsuariosRequest):
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()
    # Obtiene un registro específico por ID
    usuario = session.query(Usuarios).filter_by(id_usuario=usuariorequest.id_usuario).first()

    # Si el registro existe, actualiza la información y guarda los cambios
    if usuario:
        usuario.primer_nombre = usuariorequest.primer_nombre
        usuario.segundo_nombre = usuariorequest.segundo_nombre
        usuario.primer_apellido = usuariorequest.primer_apellido
        usuario.segundo_apellido = usuariorequest.segundo_apellido
        usuario.documento = usuariorequest.documento
        session.commit()
        print("Usuario actualizado")
    else:
        print("Usuario no encontrado")

    # Cerrar la sesión
    session.close()



def eliminar_usuarios_controller(id_usuario:int):
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()
    # Obtiene un registro específico por ID
    usuario = session.query(Usuarios).filter_by(id_usuario=id_usuario).first()

    # Si el registro existe, actualiza la información y guarda los cambios
    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuario Eliminado")
    else:
        print("Usuario no encontrado")

    # Cerrar la sesión
    session.close()