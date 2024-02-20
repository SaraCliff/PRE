def multiples_interval(m, x, y) :
    """
    >>> multiples_interval(2, 2, 10)
    [2, 4, 6, 8, 10]
    >>> multiples_interval(5, -5, 4)
    [-5, 0]
    >>> multiples_interval(7, -15, 10)
    [-14, -7, 0, 7]
    >>> multiples_interval(13, 1, 9)
    []
    """
    result = []
    for i in range(x, y + 1):
        if i % m == 0:
            result.append(i)
    return result
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())