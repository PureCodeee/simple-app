from fastapi import FastAPI
from app.routes import router

app = FastAPI()


app.include_router(router)


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}