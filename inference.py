from env import ResumeEnv

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