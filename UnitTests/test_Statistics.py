import statistics
import unittest
from Statistics import Statistics
from Statistics.Mean import Mean
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




if __name__ == '__main__':
    unittest.main()
