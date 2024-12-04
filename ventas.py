from pydantic import BaseModel

class Ventas(BaseModel):
    id_venta: int
    fecha: str
    ticket: str
    iva: float
    llave: str
    llave_s: str
    