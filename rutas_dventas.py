from fastapi import APIRouter
from database.db import connexion
from schemas.dventas import Dventas
from access.funcSha256 import verifica_Hash

rutadventas=APIRouter()

@rutadventas.post("/getdventas")
def get_ventas(ven:Dventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    consulta='''select td.id_dventa , td.cantidad , td.precio, 
                td.id_producto , td.id_venta 
                from tabla_dventas td
                order by td.id_venta , td.id_producto
    '''
    try:
        sql=connexion.cursor()
        sql.execute(consulta)
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("-----Error:",err)
        return {"error:":err}
    
@rutadventas.post("/insertdventas")
def insert_dventas(ven:Dventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    inserta=f'''call inserta_dventas('{ven.cantidad}',
    '{ven.precio}','{ven.id_producto}',
    '{ven.id_venta}');
    '''
    #print(inserta)
    try:
        sql=connexion.cursor()
        sql.execute(inserta)
        connexion.commit()
        return {"message":"1"}
    except Exception as err:
        print("----- error:",err)
        return {"error:":err} 

@rutadventas.post("/updatedventa")
def update_dventa(ven:Dventas):
    if(verifica_Hash(ven.llave, ven.llave_s)!=1):
        return {"error:":"error en los datos"}
    update=f'''call actualiza_dventas('{ven.cantidad}',
    '{ven.id_producto}',
    '{ven.id_venta}');
    '''
    try:
        sql=connexion.cursor()
        sql.execute(update)
        connexion.commit()
        return {"message":"1"}
    except Exception as err:
        print("----- error:",err)
        return {"error:":err}
    