from calculator import Addition, Division


def mean(data):
    try:
        data_length = len(data)
        total = 0
        for num in data:
            total = Addition.Addition.addition(total, num)
        return Division.Division.division(total, data_length)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
        return None
    except ValueError:
        print("Error: Data can't be string")
        return None
