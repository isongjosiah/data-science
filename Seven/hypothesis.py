from typing import Tuple
import math
from Six.probability import normal_cdf


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """ Returns mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sprt(p * (1 - p) * n)

    return mu, sigma
