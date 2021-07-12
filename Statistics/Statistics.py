from Statistics.Median import Median
from calculator import Calculatorr
from Statistics import Mean


class Statistics(Calculatorr.Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, sample_data):
        try:
            self.result = Mean.mean(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)

    def median(self, sample_data):
        try:
            self.result = Median.median(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)
