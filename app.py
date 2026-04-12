from fastapi import FastAPI
from env import ResumeEnv
from models import Action

app = FastAPI()
env = ResumeEnv()

@app.get("/")
def home():
    return {"message": "OpenEnv Resume Environment Running 🚀"}

@app.post("/reset")
def reset(task: str = "easy"):
    return env.reset(task)

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: Action):
    return env.step(action)