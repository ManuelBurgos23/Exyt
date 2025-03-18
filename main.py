from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Importar los routers correctamente
from routes.register_user import router as register_router
from routes.list_users import router as list_users_router
from routes.delete_user import router as delete_user_router
from routes.update import router as actualizar_usuario
from routes.search import router as consultar_usuario

# Inicializar la app
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers con prefijos
app.include_router(register_router, tags=["Registro"])
app.include_router(list_users_router, tags=["Usuarios"])
app.include_router(actualizar_usuario, tags=["Actualizar"])
app.include_router(consultar_usuario, tags=["Consultar"])
app.include_router(delete_user_router, tags=["Eliminar"])



# Iniciar la app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)
