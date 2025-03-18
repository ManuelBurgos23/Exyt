from pydantic import BaseModel , field_validator 
import re
from datetime import datetime

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