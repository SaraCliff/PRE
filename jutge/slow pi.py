def slow_pi_approx(n):
    """
    >>> slow_pi_approx(10)
    3.2323
    >>> slow_pi_approx(100)
    3.1515
    >>> slow_pi_approx(1000)
    3.1426

    """

    result = 0.0

    for k in range(n + 1):
        result += ((-1) ** k) / (2 * k + 1)

    pi_approx = 4 * result
    return round(pi_approx, 4)



if __name__ == "__main__":
    import doctest

    print(doctest.testmod())