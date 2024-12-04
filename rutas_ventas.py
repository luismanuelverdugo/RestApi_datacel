from fastapi import APIRouter
from database.db import connexion
from schemas.ventas import Ventas
from access.funcSha256 import verifica_Hash

rutaventas=APIRouter()

@rutaventas.post("/getventas")
def get_ventas(ven:Ventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    consulta="select * from vista_ventas vp "
    try:
        sql=connexion.cursor()
        sql.execute(consulta)
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("-----Error:",err)
        return {"error:":err}
    
@rutaventas.post("/insertventas")
def insert_ventas(ven:Ventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    inserta=f'''select inserta_venta('{ven.fecha}',
    '{ven.ticket}','{ven.iva}');
    '''
    #print(inserta)
    try:
        sql=connexion.cursor()
        sql.execute(inserta)
        connexion.commit()
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("----- error:",err)
        return {"error:":err} 

@rutaventas.post("/delventas")
def del_ventas(ven:Ventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    delete=f'''call elimina_venta('{ven.id_venta}');
    '''
    #print(inserta)
    try:
        sql=connexion.cursor()
        sql.execute(delete)
        connexion.commit()
        return {"message":"1"}
    except Exception as err:
        print("----- error:",err)
        return {"error:":err}  
    
@rutaventas.post("/updateventa")
def update_venta(ven:Ventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    inserta=f'''select inserta_venta('{ven.fecha}',
    '{ven.ticket}','{ven.iva}');
    '''
    try:
        sql=connexion.cursor()
        sql.execute(inserta)
        connexion.commit()
        return {"message":"1"}
    except Exception as err:
        print("----- error:",err)
        return {"error:":err} 