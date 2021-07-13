from calculator import Subtraction, Division, Addition


def median(data):
    try:
        data_length = len(data)
        index = data_length // 2
        if data_length % 2:
            return sorted(data)[index]
        sub = Subtraction.Subtraction.subtraction(index, 1)
        add = Addition.Addition.addition(index, 1)
        x = sorted(data)[int(sub):int(add)]
        total = 0
        for num in x:
            total = Addition.Addition.addition(total, num)
        return Division.Division.division(total, 2)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
        return None
    except ValueError:
        print("Error: Data can't be string")
        return None





# def median(data):
#     try:
#         data_length = len(data)
#         index = data_length // 2
#         if data_length % 2:
#             return sorted(data)[index]
#         sub = Subtraction.Subtraction.subtraction(index, 1)
#         add = Addition.Addition.addition(index, 1)
#         x = sorted(data)[int(sub):int(add)]
#         y = sum(x)
#         return Division.Division.division(y, 2)
#     except ZeroDivisionError:
#         print("Error: Can't Divide by 0")
#         return None
#     except ValueError:
#         print("Error: Data can't be string")
#         return None
