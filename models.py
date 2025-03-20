from pydantic import BaseModel , field_validator, EmailStr
import re
from datetime import datetime

class Usuario(BaseModel):
    
    #Definir campos
    nombre: str
    apellidos: str
    dni: str
    email: EmailStr
    fecha_nac: str
    
    #Validar datos
    @field_validator("dni" , mode="before")
    @classmethod
    def validar_dni(cls, dni: str) -> str: 
        dniRegex = re.compile(r"^\d{8}[A-Z]$")
        if not dniRegex.match(dni):
            raise ValueError("DNI inválido. Debe tener 8 números seguidos de una letra mayúscula.")
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
            raise ValueError("Formato de fecha inválido, debe ser YYYY/MM/DD")
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