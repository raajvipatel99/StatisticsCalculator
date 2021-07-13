from calculator import SquareRoot
from Statistics.Variance import variance


def standardDeviation(data):
    try:
        sd = SquareRoot.SquareRoot.squareroot(variance(data))
        return sd
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
        return None
    except ValueError:
        print("Error: Data can't be string")
        return None
