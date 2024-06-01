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

def guardar(nombre:str):  
    # Crea una sesión para interactuar con la base de datos
    session = sessionmaker(bind=engine)
    session = session()

    #crear las tablas en caso de ser necesario
    #Base.metadata.create_all(engine)

    registro=TipoUsuarios(nombre=nombre)
    session.add(registro)
    session.commit()
    session.close()