from fastapi import FastAPI
from env import ResumeEnv

app = FastAPI()
env = ResumeEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs

@app.post("/step")
def step(action: str):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"message": "OpenEnv running"}