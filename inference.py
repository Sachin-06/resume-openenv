import os
import requests
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

print("[START]")

# Reset environment
requests.post(f"{BASE_URL}/reset", params={"task": "easy"})

prompt = "Resume: I know python and ml. Job: Need python, ml, aws"

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": prompt}]
)

# Simulated action (you can parse LLM output later)
payload = {
    "resume": "I know python and ml",
    "job_description": "Need python, ml, aws"
}

res = requests.post(f"{BASE_URL}/step", json=payload).json()

print("[STEP]")
print(res)

print("[END]")