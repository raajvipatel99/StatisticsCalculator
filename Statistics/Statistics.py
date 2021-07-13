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
        self.result = mean(sample_data)
        return self.result

    def median(self, sample_data):
        self.result = median(sample_data)
        return self.result

    def mode(self, sample_data):
        self.result = mode(sample_data)
        return self.result

    def variance(self, sample_data):
        self.result = variance(sample_data)
        return self.result

    def standardDeviation(self, sample_data):
        self.result = standardDeviation(sample_data)
        return self.result

