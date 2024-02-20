def codi(s):
    """
    >>> codi('Mireia Belmonte Garcia')
    'MBG20'
    >>> codi('Bruce Frederick Joseph Springsteen')
    'BFJS31'
    >>> codi('')
    ''

    """

    ini = ""
    count = 0

    for char in s:
        if char.isalpha():
            if char.isupper():
                ini += char
            count += 1

    return ini + str(count) if count > 0 else ''


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())