class Division:
    def __init__(self):
        pass

    @staticmethod
    def division(a, b):
        try:
            a = float(a)
            b = float(b)
        except ZeroDivisionError:
            print("Error: Can't Divide by 0")
        return a / b
