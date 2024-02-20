def pos_a(s, k):
    """
    >>> pos_a('', 1)
    -1
    >>> pos_a('hola', 2)
    -1
    >>> pos_a('ara', 3)
    -1
    >>> pos_a('lalaland', 3)
    5
    >>> pos_a('almendro', 1)
    0

    """

    count_a = 0

    for i, char in enumerate(s):
        if char == 'a':
            count_a += 1
            if count_a == k:
                return i

    return -1



if __name__ == "__main__":
    import doctest

    print(doctest.testmod())