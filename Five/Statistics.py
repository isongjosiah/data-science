from collections import Counter
import matplotlib.pyplot as plt
from Four.Vector import sum_of_squares
from Four.Vector import dot
import math


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def _median_even(xs: List[float]) -> float:
    """ If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return(sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]


def median(v: List[float]) -> float:
    """ Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_Counter = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_Counter]


def de_mean(xs: List[float]) -> float:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "varianc erequres at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(
        ys), "xs and ys must have the same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / len(xs)-1


def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandme about their means """
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0
