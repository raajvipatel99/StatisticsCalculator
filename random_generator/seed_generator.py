import random

random.seed(20)


def getRandomSeed(m, n):
    return random.randint(m, n)


def getRandomDecimalSeed(m, n):
    return m + random.random() * (n - m)


def getSampleListSeed(data, sample_size):
    random_values = random.random.sample(data, k=sample_size)
    return random_values
