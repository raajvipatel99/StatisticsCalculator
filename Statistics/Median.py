from calculator import Subtraction, Division, Addition


def median(data):
    if len(data) == 0:
        raise Exception("List empty")
    data_length = len(data)
    index = data_length // 2
    if data_length % 2:
        return sorted(data)[index]
    w = Subtraction.Subtraction.subtraction(index, 1)
    a = Addition.Addition.addition(index, 1)
    x = sorted(data)[int(w):int(a)]
    y = sum(x)
    z = Division.Division.division(y, 2)
    # return Division.Division.division(sum(sorted(data)[Subtraction.Subtraction.subtraction(index, 1):Addition.Addition.addition(index, 1)]), 2)
    return z