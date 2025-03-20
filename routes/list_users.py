from fastapi import APIRouter, HTTPException
from connectdb import db
from pydantic import BaseModel
from typing import List


router = APIRouter()

# Modelo para la respuesta
class UsuarioSchema(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    email: str
    fecha_nac: str 

router = APIRouter()

@router.get("/usuarios")
async def obtener_usuarios():
    usuarios_ref = db.collection("usuarios").stream()
    usuarios = [usuario.to_dict() for usuario in usuarios_ref]

    if not usuarios:
        return []

    return usuarios
