from fastapi import APIRouter
from connectdb import db
from models import Usuario  

router = APIRouter() 

@router.post("/registrar")
async def registrar_usuario(usuario: Usuario):
    doc_ref = db.collection("usuarios").document(usuario.dni)
    doc_ref.set({
        "nombre": usuario.nombre,
        "dni": usuario.dni,
        "email": usuario.email,
        "fecha_nac": usuario.fecha_nac,
        "apellidos": usuario.apellidos
    })
    return {"mensaje": "Usuario registrado"}
