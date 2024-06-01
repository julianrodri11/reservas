from sqlalchemy import create_engine

def conectar_db():
    """
    Establece una conexión con la base de datos PostgreSQL.
    """
    engine = create_engine("postgresql://postgres:123@localhost:5432/reservas", echo=False)
    return engine

# Ejemplo de uso
#engine = conectar_db()