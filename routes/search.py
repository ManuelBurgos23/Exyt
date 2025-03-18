from fastapi import APIRouter
from connectdb import db
from models import Usuario  

router = APIRouter()

#endpoint para obtener un usuario por cualquiera de sus campos
@router.get("/consulta")
async def consultar_datos(campo,value):
    usuarios = []
    docs = db.collection("usuarios").where(campo, "==", value).stream()
    for doc in docs:
        usuarios.append(doc.to_dict())
    return usuarios