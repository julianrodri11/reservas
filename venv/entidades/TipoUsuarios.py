from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
from config.conexion import conectar_db
from sqlalchemy import create_engine

engine=conectar_db()

Base = declarative_base()



class TipoUsuarios(Base):
    __tablename__ = "tipo_usuariosA"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(25), nullable=False)

#crear las tablas en caso de ser necesario
#Base.metadata.create_all(engine)

def guardar(nombre:str):  
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()

    registro=TipoUsuarios(nombre=nombre)
    session.add(registro)
    session.commit()
    session.close()

def consultar(nombre:str):  
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()

    # Obtiene un registro específico por nombre
    tipousuario = session.query(TipoUsuarios).filter_by(nombre=nombre).first()

    # Si el registro existe, imprime la información
    if tipousuario:
        session.close()
        return {"id":tipousuario.id,"nombre":tipousuario.nombre}
    else:
        session.close()
        return ("Usuario no encontrado")
