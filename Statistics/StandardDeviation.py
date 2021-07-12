from calculator import SquareRoot
from Statistics import Variance


class StandardDeviation:
    def __init__(self):
        pass

    @staticmethod
    def standardDeviation(data):
        sd = SquareRoot.SquareRoot.squareroot(Variance.Variance.variance(data))
        return sd
