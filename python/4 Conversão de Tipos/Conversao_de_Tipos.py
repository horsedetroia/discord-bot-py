# Converter tipos é como dizer: "antes, eu tinha o texto 5, agora, eu tenho o número 5". É possível transformar uma string em um número inteiro, qualquer tipo de dado pode se tornar outro tipo de dado. 

# Essas conversões servem para facilitar e alterar o modo no qual valores podem ser manipulados. Por exemplo, se o número 5 está armazenado dentro de uma string (valor textual), eu nunca poderei realizar uma adição com um texto.

# Por exemplo:
print('1' + '1') # As aspas declaram que o número 1 é uma string (é um texto), portanto ao "somar", o resultado será 11

print(1 + 1) # A falta de aspas, indica que 1 é um número inteiro, e pode ser somado, resultando em 2

# print('1' + 1) # Um número não pode ser somado com um texto, gerando um erro no código e parando sua execução.

"""Do mesmo modo, a conversão de números pode ser utilizada quando há necessidade de trabalhar com números quebrados (float), ou controlar o tamanho do arquivo (bytes):
"""

preço = 30
print('Preço inteiro:', preço)

preço = float(30)
print('Preço com ponto flutuante:', preço)
