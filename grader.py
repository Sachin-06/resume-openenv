def grade(env_state, action):
    skills = env_state["candidate_skills"]
    required = env_state["job_required_skills"]

    matched = len(set(skills) & set(required))
    total = len(required)

    score = matched / total

    # Define correct behavior
    if score >= 0.7:
        correct = "shortlist"
    elif score <= 0.3:
        correct = "reject"
    else:
        correct = "shortlist"  # partial → still acceptable

    if action == correct:
        return 1.0
    elif abs(score - 0.5) < 0.2:
        return 0.5  # partial credit
    else:
        return 0.0