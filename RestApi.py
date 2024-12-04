from fastapi import FastAPI
from routes.rutas_clientes import rutaclientes
from routes.rutas_productos import rutaproductos
from routes.rutas_ventas import rutaventas
from routes.rutas_dventas import rutadventas

app=FastAPI()

app.include_router(rutaclientes)
app.include_router(rutaproductos)
app.include_router(rutaventas)
app.include_router(rutadventas)
