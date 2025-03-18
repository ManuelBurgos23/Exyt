from connectdb import db
from fastapi import APIRouter


router = APIRouter()

#endpoint para actualizar un usuario
@router.patch("/actualizar")
async def actualizar_usuario(dni: str, campo: str, valor: str):
    doc_ref = db.collection("usuarios").document(dni)
    doc = doc_ref.get()
    
    if not doc.exists:
        return {"mensaje": "Usuario no encontrado"}

    if campo == "dni":
        # Crear un nuevo documento con el nuevo DNI
        nuevo_dni = valor
        nuevo_doc_ref = db.collection("usuarios").document(nuevo_dni)
        nuevo_doc_ref.set(doc.to_dict())
        
        # Actualizar el campo en el nuevo documento
        nuevo_doc_ref.update({campo: valor})
        
        # Eliminar el documento antiguo
        doc_ref.delete()
    else:
        # Actualizar el campo en el documento existente
        doc_ref.update({campo: valor})

    return {"mensaje": "Usuario actualizado"}

    