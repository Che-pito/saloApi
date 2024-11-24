from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.database.configuration import sessionLocal, engine
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.modelosApp import Gasto
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.models.modelosApp import Categoria
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.models.modelosApp import MetodoPago
 
#Para que un api funciones debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVIVIOS
# QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
            nombre=datosPeticion.nombre,
            apellido=datosPeticion.apellido,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        ) 

        db.add(usuario) 
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")  

#Rutas Gastos
@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        gasto=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )

        db.add(gasto) 
        db.commit()
        db.refresh(gasto)
        return gasto
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
    
@rutas.get("/gastos", response_model=List[GastoDTORespuesta])    
def buscarGastos(db:Session=Depends(getDataBase)):
    try:
        listadoDeGastos=db.query(Gasto).all()
        return listadoDeGastos
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
    
#Rutas Categoria
@rutas.post("/categorias", response_model=CategoriaDTORespuesta )
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        categoria=Categoria(
        nombreCategoria=datosPeticion.nombreCategoria,
        descripcion=datosPeticion.descripcion,
        fotoIcono=datosPeticion.fotoIcono
        
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
    
@rutas.get("/categorias", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db:Session=Depends(getDataBase)):
    try:
        listadoDeCategoria=db.query(Categoria).all()
        return listadoDeCategoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")

#Rutas Metodo de pago
@rutas.post("/metodosPagos", response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        metodos_pago=MetodoPago(
        nombreMetodo=datosPeticion.nombreMetodo,
        descripcion=datosPeticion.descripcion
        
        )

        db.add(metodos_pago)
        db.commit()
        db.refresh(metodos_pago)
        return metodos_pago
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
    
@rutas.get("/metodosPagos", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db:Session=Depends(getDataBase)):
    try:
        listadoDeMetodoPago=db.query(MetodoPago).all()
        return listadoDeMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
