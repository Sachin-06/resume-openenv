from env import ResumeEnv
from grader import grade

def simple_agent(obs):
    skills = obs["candidate_skills"]
    required = obs["job_required_skills"]

    match = len(set(skills) & set(required)) / len(required)

    if match >= 0.5:
        return "shortlist"
    else:
        return "reject"

def run_agent():
    env = ResumeEnv()

    obs = env.reset()

    action = simple_agent(obs)

    obs, reward, done, info = env.step(action)

    g = grade(obs, action)

    print("START")
    print("STEP:", action)
    print("REWARD:", reward)
    print("GRADE:", g)
    print("END")

if __name__ == "__main__":
    run_agent()