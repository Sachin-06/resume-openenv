def grade(obs, action):
    required = set(obs["job_required_skills"])
    skills = set(obs["candidate_skills"])

    match_ratio = len(skills & required) / len(required)

    if match_ratio >= 0.5 and action == "shortlist":
        return 1.0
    elif match_ratio < 0.5 and action == "reject":
        return 1.0
    else:
        return 0.0