# Exemplo de causa TypeError

try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)
else: 
    print("tudo ocorreu bem")
finally:
    print("o importante eh participar")


numero = print("Insira um numero: ")
if isinstance(numero, int):
    print("A variavel é um inteiro")
else:
    print("A variavel nao é um inteiro")