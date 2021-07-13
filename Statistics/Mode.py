from collections import Counter


def mode(data):
    try:
        c = Counter(data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
        return None
    except ValueError:
        print("Error: Data can't be string")
        return None
