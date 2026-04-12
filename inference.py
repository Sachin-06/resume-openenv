import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")

print("[START]")

# Reset environment
requests.post(f"{BASE_URL}/reset")

payload = {
    "resume": "I know python and ml",
    "job_description": "Need python, ml, aws"
}

res = requests.post(f"{BASE_URL}/step", json=payload).json()

print("[STEP]")
print(res)

print("[END]")