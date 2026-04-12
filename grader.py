def grade(task, score):
    if task == "easy":
        return min(1.0, score)

    elif task == "medium":
        return min(1.0, score * 0.8)

    elif task == "hard":
        return min(1.0, score * 0.6)

    return 0.0