from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#Conexion a la BD
#nombreBD
dataBaseName="gestionbd"

#usuarioBD
userNAme="root"

#Contraseña del usuario
userPassword=""

#PUERTO DE CONEXION
conexionPort="3306"

#SERVIDOR CONEXION
severConnection="localhost"

#CREANDO LA CONEXION
conexionToDataBAse=f"mysql+mysqlconnector://{userNAme}:{userPassword}@{severConnection}:{conexionPort}/{dataBaseName}"

engine=create_engine(conexionToDataBAse)
sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)