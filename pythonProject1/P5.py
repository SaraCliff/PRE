def is_vowel_covered(s):
    """
    >>> is_vowel_covered("AaaaA")
    True
    >>> is_vowel_covered("AaaA")
    False
    >>> is_vowel_covered("AeioUAeioU")
    True
    >>> is_vowel_covered("aAppAlAa")
    False
    >>> is_vowel_covered("AaaaaazZ")
    False

    """

    a = "AEIOU"
    b = "aeiou"
    return len(s) > 4 and s[0] in a and s[-1] in a and s[1] in b and s[-2]  in b



if __name__ == "__main__":
    import doctest

    print(doctest.testmod())