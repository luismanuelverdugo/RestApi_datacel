from pydantic import BaseModel

class Productos(BaseModel):
    id_producto: int
    descripcion: str
    preciou: float
    preciov: float
    id_umedida: int
    inventario: int
