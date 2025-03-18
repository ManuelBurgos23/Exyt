from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a FastAPI"}

def suma() -> int:
    valor1: int = 20
    valor2: int = 24
    total = valor1 + valor2
    return total

@app.get("/suma")
def get_suma():
    total = suma()
    return {"total": total}

    