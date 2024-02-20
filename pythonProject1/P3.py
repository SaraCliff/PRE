def cercanias(linea,sentido):
    """
    >>> cercanias(3,'N')
    12
    >>> cercanias(7,'N')
    0
    >>> cercanias(4,'S')
    15
    >>> cercanias(2,'W')
    0
    """

    if linea == 1:
        if sentido == 'N':
            resultado = 8
            return resultado
        elif sentido == 'S':
            resultado = 7
            return resultado
        else:
            resultado = 0
            return resultado
    elif linea == 2:
        if sentido == 'N':
            resultado = 10
            return resultado
        elif sentido == 'S':
            resultado = 9
            return resultado
        else:
            resultado = 0
            return resultado
    elif linea == 3:
        if sentido == 'N':
            resultado = 12
            return resultado
        elif sentido == 'S':
            resultado = 13
            return resultado
        else:
            resultado = 0
            return resultado
    elif linea == 4:
        if sentido == 'N':
            resultado = 14
            return resultado
        elif sentido == 'S':
            resultado = 15
            return resultado
        else:
            resultado = 0
            return resultado
    else:
        resultado = 0
        return resultado


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())