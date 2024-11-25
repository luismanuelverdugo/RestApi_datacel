from fastapi import FastAPI
from routes.rutas_clientes import rutaclientes
from routes.rutas_productos import rutaproductos

app=FastAPI()

app.include_router(rutaclientes)
app.include_router(rutaproductos)
