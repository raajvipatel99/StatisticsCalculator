import statistics
import unittest
from Statistics import Statistics
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standardDeviation
from Statistics.Variance import variance
from random_generator import generator
import pprint
from random_generator.generator import getSampleListNonRepeating, getSampleListDecimalNonRepeating


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.my_statistics = Statistics.Statistics()
        self.test_data_int = [generator.getSampleList(0, 40, 10) for i in range(10)]
        self.test_data_dec = [generator.getSampleListDecimal(0, 40, 10) for i in range(10)]



    def test_instantiate_calculator(self):
        self.assertIsInstance(self.my_statistics, Statistics.Statistics)

    def test_mean_calculator(self):
        for k in self.test_data_int:
            self.assertAlmostEqual(self.my_statistics.mean(k), statistics.mean(k), 3)

        for k in self.test_data_dec:
            self.assertAlmostEqual(self.my_statistics.mean(k), statistics.mean(k), 3)
    print("Mean Test cases passed")

    def test_median_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            self.assertEqual(self.my_statistics.median(k), statistics.median(k))

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            # self.assertEqual(abs(median - statistics.median(k)) < 10 ** -5, True)
            self.assertEqual(self.my_statistics.median(k), statistics.median(k))
        print("Median Test cases passed")

    def test_mode_calculator(self):

        test_data = [getSampleListNonRepeating(0, 10, 100) for i in range(10)]
        for k in test_data:
            self.assertListEqual(self.my_statistics.mode(k), statistics.multimode(k))

        test_data = [getSampleListDecimalNonRepeating(0, 1, 10 ** 2) for i in range(10)]
        for k in test_data:
            self.assertListEqual(self.my_statistics.mode(k), statistics.multimode(k))
        print("Mode Test cases passed")

    def test_variance_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            self.assertAlmostEqual(self.my_statistics.variance(k), statistics.variance(k), 3)

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            self.assertAlmostEqual(self.my_statistics.variance(k), statistics.variance(k), 3)
        print("Variance Test cases passed")

    def test_standardDeviation_calculator(self):

        # test_data = [getSampleList(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_int:
            self.assertAlmostEqual(self.my_statistics.standardDeviation(k), statistics.stdev(k), 3)

        # test_data = [getSampleListDecimal(0, 10 ** 6, 10 ** 2) for i in range(100)]
        for k in self.test_data_dec:
            self.assertAlmostEqual(self.my_statistics.standardDeviation(k), statistics.stdev(k), 3)
        print("Standard Deviation Test cases passed")


if __name__ == '__main__':
    unittest.main()
