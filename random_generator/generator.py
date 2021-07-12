import random


def getRandom(m, n):
    return random.randint(m, n)


def getRandomDecimal(m, n):
    return m + random.random() * (n - m)


def getSampleList(m, n, sample_size):
    arr = set()
    for _ in range(sample_size):
        arr.add(getRandom(m, n))
    return list(arr)


def getSampleListNonRepeating(m, n, sample_size):
    arr = []
    for _ in range(sample_size):
        arr.append(getRandom(m, n))
    return arr


def getSampleListDecimal(m, n, sample_size):
    arr = set()
    for _ in range(sample_size):
        arr.add(getRandomDecimal(m, n))
    return list(arr)


def getSampleListDecimalNonRepeating(m, n, sample_size):
    arr = []
    for _ in range(sample_size):
        arr.append(getRandomDecimal(m, n))
    return arr
