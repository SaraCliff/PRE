def grade(s) :
    """
    >>> grade(4.99)
    'suspens'
    >>> grade(8)
    'notable'
    >>> grade(6.99)
    'aprovat'
    >>> grade(9.5)
    'excel.lent'
    >>> grade(10)
    'MH'
    """

    if 0 <= s < 5:
        return 'suspens'
    elif 5 <= s < 7:
        return 'aprovat'
    elif 7 <= s < 9:
        return 'notable'
    elif 9 <= s < 10:
        return 'excel.lent'
    else:
        return 'MH'

if __name__ == "__main__" :
    import doctest
    print(doctest.testmod())