from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy environment class (replace with your actual logic if needed)
class ResumeEnv:
    def step(self, action):
        return {"result": f"Processed action: {action}"}

env = ResumeEnv()

class ActionRequest(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "Resume OpenEnv API is running 🚀"}

@app.post("/step")
def step(request: ActionRequest):
    result = env.step(request.action)
    return result