from fastapi  import FastAPI
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID,uuid4

app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


task = []


@app.get("/")
def read():
    return {"hello":"world"}



if __name__ == "__main__":
    import uvicorn


    uvicorn.run(app, host="127.0.0.1",port=8000)