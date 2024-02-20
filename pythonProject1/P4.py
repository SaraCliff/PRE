def leading_hand(h, m):
    """
    >>> leading_hand(22, 51)
    'minute hand'
    >>> leading_hand(21, 45)
    'draw'
    >>> leading_hand(6, 28)
    'hour hand'
    >>> leading_hand(4, 20)
    'draw'

    """

    if h >= 12:
        hour= (h-12)*180/6
    else:
        hour = h*180/6
    minutos = m * 6


    if hour < minutos:
        return 'minute hand'
    elif minutos < hour:
        return 'hour hand'
    else:
        return 'draw'


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())