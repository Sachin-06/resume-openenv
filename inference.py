from env import ResumeEnv

def run():
    env = ResumeEnv()
    obs = env.reset()

    action = "shortlist"

    obs, reward, done, info = env.step(action)

    print("Final Score:", reward.score)

if __name__ == "__main__":
    run()