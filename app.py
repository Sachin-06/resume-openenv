from fastapi import FastAPI
from env import ResumeEnv

app = FastAPI()
env = ResumeEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(data: dict):
    action = data.get("action")
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"status": "running"}