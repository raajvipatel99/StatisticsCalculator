# StatisticsCalculator

Travis Status

[![Build Status](https://travis-ci.com/raajvipatel99/StatisticsCalculator.svg?branch=master)](https://travis-ci.com/raajvipatel99/StatisticsCalculator)

Successful build through Travis CI

Description
This project is part of IS601 course. It is a calculator using Python that has automated unit tests. It performs operations such as addition, subtraction, multiplication, division, square root, square, mean, median, mode, random, variance and standard deviation. The unit tests file for specific operation contains 18 tests for addition, subtraction, multiplication, division, square root and square and 2 unit tests for each statistical operation. This project strictly follows the SOLID principle with a well-thought-out architecture.

Program Requirements
Demonstrate inheritance by extending the calculator
Demonstrate encapsulation by having the calculator have methods and a result property
Demonstrate abstraction by layering your code and using static methods. Object methods should call static methods to perform the operation.
Check values for being valid numbers and not strings
Throw an exception for divide by zero
Throw exception for empty list
Use random data for tests and be able to increase the number of calculations required i.e. be able to increase the list of numbers that the mean calculation is done on. You can actually use built-in libraries or 3rd party libraries to check the calculations that you complete yourself. i.e. you can use the standard deviation function from a stats library to compute the correct value for your list of random numbers and then use that to test that your own calculation is correct for that list.

Program Outline
This project demonstrates inheritance by extending the Calculator (calculator/Calculator.py) by Statistics (Statistics/Statistics.py). The functions added to the statistics calculator are mean, median, mode, variance and standard deviation. These functions are imported from Mean.py, Median.py, Mode.py, Variance.py and StandardDeviation.py. In order to test these statistical functions, unit test cases are written in calculator/test_StatisticsTest.py and values for checking them are generated using Random class.

