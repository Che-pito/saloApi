from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas

Base=declarative_base()

#Listado de modelos de la aplicaciom
#Usuario
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    apellido=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(String(20))
    ciudad=Column(String(50))

#Gasto
class Gasto(Base):
    __tablename__='gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Float)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(20))
    
#Categoria
class Categoria(Base):
    __tablename__='categorias'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(100))
    fotoIcono=Column(String(200))
    
#Metodos de pago
class MetodoPago(Base):
    __tablename__='metodosPagos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100))
    
