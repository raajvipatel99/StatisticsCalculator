import statistics
import unittest
from Statistics import Statistics
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Variance import Variance
from random_generator import generator
import pprint
from random_generator.generator import getSampleListNonRepeating, getSampleListDecimalNonRepeating


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics.Statistics()
        self.test_data_int = [generator.getSampleList(0, 40, 10) for i in range(10)]
        self.test_data_dec = [generator.getSampleListDecimal(0, 40, 10) for i in range(10)]



    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics.Statistics)

    def test_mean_calculator(self):
        for k in self.test_data_int:
            mean = Mean.mean(k)
            self.assertEqual(abs(mean - statistics.mean(k)) < 10 ** -5, True)

        for k in self.test_data_dec:
            mean = Mean.mean(k)
            self.assertEqual(abs(mean - statistics.mean(k)) < 10 ** -5, True)
    print("Mean Test cases passed")

    def test_median_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            median = Median.median(k)
            self.assertEqual(median, statistics.median(k))

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            median = Median.median(k)
            # self.assertEqual(abs(median - statistics.median(k)) < 10 ** -5, True)
            self.assertEqual(median, statistics.median(k))
        print("Median Test cases passed")

    def test_mode_calculator(self):

        test_data = [getSampleListNonRepeating(0, 10, 100) for i in range(10)]
        for k in test_data:
            mode = Mode.mode(k)
            actual_mode = statistics.multimode(k)
            self.assertListEqual(mode, actual_mode)

        test_data = [getSampleListDecimalNonRepeating(0, 1, 10 ** 2) for i in range(10)]
        for k in test_data:
            mode = Mode.mode(k)
            actual_mode = statistics.multimode(k)
            self.assertListEqual(mode, actual_mode)
        print("Mode Test cases passed")

    def test_variance_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            variance = Variance.variance(k)
            # self.assertEqual(abs(variance - statistics.variance(k)) < 10 ** -5, True)
            self.assertAlmostEqual(variance, statistics.variance(k), 3)

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            variance = Variance.variance(k)
            self.assertAlmostEqual(variance, statistics.variance(k), 3)
        print("Variance Test cases passed")

    def test_standardDeviation_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            sd = StandardDeviation.standardDeviation(k)
            self.assertAlmostEqual(sd, statistics.stdev(k), 3)

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            sd = StandardDeviation.standardDeviation(k)
            self.assertAlmostEqual(sd, statistics.stdev(k), 3)
        print("Standard Deviation Test cases passed")


if __name__ == '__main__':
    unittest.main()
