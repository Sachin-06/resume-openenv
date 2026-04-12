def grade_easy(score):
    return min(1.0, score)

def grade_medium(score):
    return min(1.0, score * 0.8)

def grade_hard(score):
    return min(1.0, score * 0.6)