# abrir "regex_sum_995579.txt"
import re
'''importa o "REGULAR EXPRESSIONS"'''

nome_arquivo = input("Entre com o nome do arquivo: ")
if len(nome_arquivo) < 1:
    nome_arquivo = "regex_sum_995579.txt"

x = list()
soma = 0

abre_arquivo = open(nome_arquivo)
for line in abre_arquivo:
    if len(re.findall('[0-9]+', line)) == 0:
        continue
    x += (re.findall('[0-9]+', line))
    #retira todos os números de dentro do texto e coloca em uma lista


print(soma)
