from fastapi import APIRouter
from connectdb import db

router = APIRouter()

#endpoint para eliminar un usuario por su dni
@router.delete("/eliminar")
async def eliminar_usuario(dni: str):
    doc_ref = db.collection("usuarios").document(dni)
    doc = doc_ref.get()

    if not doc.exists:
        return {"mensaje": "Usuario no encontrado"}

    doc_ref.delete()
    return {"mensaje": "Usuario eliminado"}
