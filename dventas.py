from pydantic import BaseModel

class Dventas(BaseModel):
    id_dventa: int
    cantidad: float 
    precio: float 
    id_producto: int
    id_venta: int
    llave: str
    llave_s: str