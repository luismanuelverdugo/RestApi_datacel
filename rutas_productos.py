from fastapi import APIRouter
from database.db import connexion
from schemas.productos import Productos

rutaproductos=APIRouter()

@rutaproductos.post("/getproductos")
def get_productos():
    consulta="select * from vista_productos vp "
    try:
        sql=connexion.cursor()
        sql.execute(consulta)
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("-----Error:",err)
        return {"error:":err}
    
@rutaproductos.post("/insertproductos")
def insert_productos(pro:Productos):
    inserta=f'''call inserta_productos('{pro.descripcion}',
    '{pro.preciou}','{pro.preciov}',
    '{pro.id_umedida}','{pro.inventario}'
    );
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
    
@rutaproductos.post("/delproductos")
def del_productos(pro:Productos):
    delete=f'''call elimina_producto('{pro.id_producto}');
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