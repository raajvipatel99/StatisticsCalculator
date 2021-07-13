from Statistics.Mean import mean
from calculator.Addition import Addition


def variance(data):
    try:
        n = len(data)
        m = mean(data)
        deviations = [(x - m) ** 2 for x in data]
        total = 0
        for num in deviations:
            total = Addition.addition(total, num)
        return total / (n - 1)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
        return None
    except ValueError:
        print("Error: Data can't be string")
        return None


# def variance(data):
#     try:
#         n = len(data)
#         mean = sum(data) / n
#         deviations = [(x - mean) ** 2 for x in data]
#         return sum(deviations) / (n - 1)
#     except ZeroDivisionError:
#         print("Error: Can't Divide by 0")
#         return None
#     except ValueError:
#         print("Error: Data can't be string")
#         return None