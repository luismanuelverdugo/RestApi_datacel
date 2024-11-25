from fastapi import APIRouter
from database.db import connexion
from schemas.clientes import Clientes

rutaclientes=APIRouter()

@rutaclientes.post("/getclientes")
def get_clientes():
    consulta="select * from vista_clientes"
    try:
        sql=connexion.cursor()
        sql.execute(consulta)
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("-----Error:",err)
        return {"error:":err}
    
@rutaclientes.post("/insertcliente")
def insert_cliente(cli:Clientes):
    inserta=f'''call insertar_cliente('{cli.nombre}',
    '{cli.apellido_paterno}','{cli.apellido_materno}'
    ,'{cli.num_telefono}','{cli.rfc}','{cli.calle}',
    '{cli.colonia}','{cli.cp}','{cli.ciudad}',
    '{cli.correo_electronico}');
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
    
@rutaclientes.post("/delcliente")
def del_cliente(cli:Clientes):
    delete=f'''call elimina_cliente('{cli.id_cliente}');''';
    try:
        #connexion.open()
        sql=connexion.cursor()
        sql.execute(delete)
        connexion.commit()
        #sql.close()
        #connexion.close()
        return {"message":"1"}
    except Exception as err:
        print("----- error:",err)
        return {"error:":err}    

@rutaclientes.post("/updatecliente")
def update_cliente(cli:Clientes):
    inserta=f'''call actualiza_cliente('{cli.id_cliente}','{cli.nombre}',
    '{cli.apellido_paterno}','{cli.apellido_materno}'
    ,'{cli.num_telefono}','{cli.rfc}','{cli.calle}',
    '{cli.colonia}','{cli.cp}','{cli.ciudad}',
    '{cli.correo_electronico}');
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

@rutaclientes.post("/getcliente")
def get_cliente(cli:Clientes):
    consulta=f'''select * from vista_clientes va 
                where va.id_cliente={cli.id_cliente}
    '''
    try:
        sql=connexion.cursor()
        sql.execute(consulta)
        resultado=sql.fetchall()
        return resultado
    except Exception as err:
        print("-----Error:",err)
        return {"error:":err}