def CleanList(x):
    if not isinstance(x, list):
        return x

    return [
        'Não informado' if pais.strip() == ''
        else pais.strip().title()
        for pais in x
        if isinstance(pais, str)
    ]
