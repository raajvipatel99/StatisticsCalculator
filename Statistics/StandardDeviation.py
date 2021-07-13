from calculator import SquareRoot
from Statistics.Variance import variance


def standardDeviation(data):
    sd = SquareRoot.SquareRoot.squareroot(variance(data))
    return sd
