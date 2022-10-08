#Conte as vogais em uma string
#Crie uma função em Python que aceite uma única palavra e retorne o número de vogais dessa palavra. Nesta função, apenas a, e, i, o e u serão contados como vogais — não y.

def conte_as_vogais(frase):
    """Conte as vogais.
    """
    vogais = [ 'a', 'e', 'i', 'o', 'u']
    for i in vogais:
        bonita += frase.count (i)
    return bonita