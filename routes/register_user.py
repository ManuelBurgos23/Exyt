from fastapi import APIRouter, HTTPException
from connectdb import db
from models import Usuario  

router = APIRouter() 

@router.post("/registrar")
async def registrar_usuario(usuario: Usuario):
    usuarios_ref = db.collection("usuarios")

    email_query = usuarios_ref.where("email", "==", usuario.email).get()
    dni_query = usuarios_ref.where("dni", "==", usuario.dni).get()
    
    if email_query:
       raise HTTPException(status_code=400, detail="Email ya registrado en la base de datos, prueba con otro")
    
    if dni_query:
       raise HTTPException(status_code=400, detail="DNI ya registrado en la base de datos")

    try:
        doc_ref = db.collection("usuarios").document(usuario.dni)
        doc_ref.set({
            "nombre": usuario.nombre,
            "dni": usuario.dni,
            "email": usuario.email,
            "fecha_nac": usuario.fecha_nac,
            "apellidos": usuario.apellidos
        })
        return {"mensaje": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar usuario: {str(e)}")
