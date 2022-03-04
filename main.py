
from fastapi import FastAPI
app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")

@app.get("/")
async def test():
    return "okk"
