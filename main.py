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

@app.post("/task/",response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    task.append(task)
    return task


@app.get("/tasks/",response_model=List[Task])
def read_task():
    return task



if __name__ == "__main__":
    import uvicorn


    uvicorn.run(app, host="127.0.0.1",port=8000)