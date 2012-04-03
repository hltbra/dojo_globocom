def eh_bissexto(numero):
    return (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0)
