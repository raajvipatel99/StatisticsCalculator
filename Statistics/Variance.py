class Variance:
    def __init__(self):
        pass

    @staticmethod
    def variance(data):
        n = len(data)
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / (n-1)
        return variance
