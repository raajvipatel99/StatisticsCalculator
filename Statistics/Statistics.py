from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import standardDeviation
from calculator import Calculatorr
from Statistics import Mean


class Statistics(Calculatorr.Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, sample_data):
        try:
            self.result = mean(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)

    def median(self, sample_data):
        try:
            self.result = median(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)

    def mode(self, sample_data):
        try:
            self.result = mode(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)

    def variance(self, sample_data):
        try:
            self.result = variance(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)

    def standardDeviation(self, sample_data):
        try:
            self.result = standardDeviation(sample_data)
            return self.result
        except Exception as e:
            raise Exception("Statistics Exception" + e)
