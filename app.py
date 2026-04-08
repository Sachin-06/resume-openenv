from fastapi import FastAPI
from pydantic import BaseModel
from env import ResumeEnv

app = FastAPI()
env = ResumeEnv()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    return env.reset()   # ✅ FIXED

@app.post("/step")
def step(req: ActionRequest):
    obs, reward, done, info = env.step(req.action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"status": "running"}