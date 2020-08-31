def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    ret = []
    while scores and len(ret) < 3:
        ret.append(scores.pop())
    return ret
