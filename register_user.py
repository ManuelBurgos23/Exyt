from fastapi import FastAPI, Request
from pydantic import BaseModel , field_validator 
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import uvicorn 
from datetime import datetime
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
cred = credentials.Certificate("C:/python/api_key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

#Configurar CORS para permitir peticiones desde cualquier origen(Frontend con Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
usuarios = []

class Usuario(BaseModel):
    #Definir campos
    nombre: str
    apellidos: str
    dni: str
    email: str
    fecha_nac: str
    
    #Validar datos
    @field_validator("dni")
    def validar_dni(dni):
        dniRegex = re.compile(r"^\d{8}[A-Z]$")
        if dniRegex.match(dni) == None:
            raise ValueError("DNI inválido")
        return dni
    @field_validator("email")
    def email_valido(email):
        if "@" not in email:
            raise ValueError("Email inválido")
        return email
    @field_validator("fecha_nac")
    def validar_fecha(fecha_nac):
        try:
            datetime.strptime(fecha_nac, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido, debe ser dd/mm/aaaa")
        return fecha_nac
    @field_validator("nombre")
    def nombre_valido(nombre):
        if nombre.isnumeric():
            raise ValueError("El nombre no puede ser un número")
        return nombre
    @field_validator("apellidos")
    def apellidos_validos(apellidos):
        if apellidos.isnumeric():
            raise ValueError("Los apellidos no pueden ser un número")
        return apellidos

#endpoint para registrar un usuario
@app.post("/registro")
async def registrar_usuario(usuario: Usuario):
    doc_ref = db.collection("usuarios").document(usuario.dni)
    doc_ref.set({"nombre":usuario.nombre,"dni":usuario.dni,"email":usuario.email,"fecha_nac":usuario.fecha_nac,"apellidos": usuario.apellidos})
    return {"mensaje":"Usuario registrado"}

#endpoint para obtener todos los usuarios
@app.get("/usuarios")
async def obtener_usuarios():
    usuarios_ref = db.collection("usuarios").order_by("nombre").stream()
    usuarios = []
    for usuario in usuarios_ref:
        usuarios.append(usuario.to_dict())
    return {"usuarios": usuarios}

#endpoint para obtener un usuario por cualquiera de sus campos
@app.get("/consulta")
async def consultar_datos(campo,value):
    usuarios = []
    docs = db.collection("usuarios").where(campo, "==", value).stream()
    for doc in docs:
        usuarios.append(doc.to_dict())
    return usuarios

#endpoint para actualizar un usuario
@app.patch("/actualizar")
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

#endpoint para eliminar un usuario
@app.delete("/eliminar")
async def eliminar_usuario(dni: str):
    doc_ref = db.collection("usuarios").document(dni)
    doc = doc_ref.get()
    
    if not doc.exists:
        return {"mensaje": "Usuario no encontrado"}
    
    doc_ref.delete()
    
    return {"mensaje": "Usuario eliminado"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)