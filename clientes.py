from pydantic import BaseModel

class Clientes(BaseModel):
    id_cliente:int
    nombre:str	
    apellido_paterno:str
    apellido_materno:str
    num_telefono:str
    rfc:str
    calle:str
    colonia:str
    cp:str
    ciudad:str
    correo_electronico:str