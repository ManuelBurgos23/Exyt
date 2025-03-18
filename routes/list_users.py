from fastapi import APIRouter
from connectdb import db

router = APIRouter()

@router.get("/usuarios")
async def obtener_usuarios():
    usuarios_ref = db.collection("usuarios").order_by("nombre").stream()
    usuarios = [usuario.to_dict() for usuario in usuarios_ref]
    return {"usuarios": usuarios}
