def solution(participant, completion):
    people = {}
    for e in participant:
        if e in people:
            people[e] += 1
        else: people[e] = 1

    for e in completion:
        if e in people:
            people[e] -= 1

    for e in people:
        if people[e] == 1:
            return e