class Scientist():
    def __init__(self, born, died):
        self.born = born
        self.died = died

def simultaneously_alive(A, B):
    if A.died <= B.born or B.died <= A.born:
        return False
    return True

def max_alive(S):
    most_living = 0
    currently_living = []
    scientists = sorted(S, key = lambda s: s.born)

    for s in scientists:
        for o in currently_living:
            if not simultaneously_alive(s, o):
                currently_living.remove(o)
        currently_living.append(s)
        most_living = max(most_living, len(currently_living))

    return most_living

S = [
    Scientist(1950, 1980),
    Scientist(1940, 1990),
    Scientist(1930, 1970),
    Scientist(1980, 2019)
]

print(max_alive(S))