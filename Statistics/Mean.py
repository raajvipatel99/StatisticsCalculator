from calculator import Addition, Division

def mean(data):
    if len(data) == 0:
        raise Exception("List empty")
    data_length = len(data)
    total = 0
    for num in data:
          total = Addition.Addition.addition(total, num)
    return Division.Division.division(total, data_length)
