def valor_presente(I, r):
    """
    >>> round(valor_presente([5000, 5000, 5000, 45000], 5), 2)
    53169.74
    >>> round(valor_presente([100, -50, 35], 7), 2)
    83.84
    >>> valor_presente([], 3)
    0.0
    """
    result = 0.0
    for i, value in enumerate(I):
        result += value / ((1 + r / 100) ** (i))
    return round(result, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())