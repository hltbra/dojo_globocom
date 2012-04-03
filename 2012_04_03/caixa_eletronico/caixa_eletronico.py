notas = [10, 20, 50, 100]

def sacar_dinheiro(valor):
    resultado = {}
    for nota in notas[::-1]:
        div, valor = divmod(valor, nota)
        if div > 0:
            resultado[nota] = div
    return resultado
