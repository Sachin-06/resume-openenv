from fastapi import FastAPI
from pydantic import BaseModel
from env import ResumeEnv

app = FastAPI()

# Request model
class ActionRequest(BaseModel):
    action: str

# Create env instance
env = ResumeEnv()

# Health check (VERY IMPORTANT for HF)
@app.get("/")
def home():
    return {"status": "healthy"}

# Reset endpoint (IMPORTANT)
@app.post("/reset")
def reset_env():
    state = env.reset()
    return {"state": state}

# Step endpoint
@app.post("/step")
def step_action(request: ActionRequest):
    # Ensure env is initialized
    if env.state_data is None:
        env.reset()

    state, reward, done, info = env.step(request.action)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }