from env import ResumeEnv
import os

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

def run():
    env = ResumeEnv()

    obs = env.reset()

    action = "shortlist"

    obs, reward, done, info = env.step(action)

    print("START")
    print("STEP:", action)
    print("REWARD:", reward)
    print("END")

if __name__ == "__main__":
    run()