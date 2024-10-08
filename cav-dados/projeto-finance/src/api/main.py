from fastapi import FastAPI
from routers.news import router as news_router
from routers.ibov import router as ibov_router
from dotenv import load_dotenv
import os

load_dotenv()
root_path = os.getenv('ROOT_PATH', '')

app = FastAPI(root_path=root_path)

app.include_router(news_router)
app.include_router(ibov_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
