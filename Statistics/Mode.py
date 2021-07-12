from collections import Counter

class Mode:
    def __init__(self):
        pass

    @staticmethod
    def mode(data):
        c = Counter(data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
