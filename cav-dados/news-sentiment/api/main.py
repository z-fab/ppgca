from fastapi import FastAPI
from api.routers.category import router as category_router
from api.routers.root import router as root_router

app = FastAPI()


# Inclui as rota root
app.include_router(root_router, tags=["root"])

# Inclui as rotas de category
app.include_router(category_router, prefix="/category", tags=["category"])
