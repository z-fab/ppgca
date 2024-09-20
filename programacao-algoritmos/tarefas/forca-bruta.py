""""
Dado um inteiro n, gere todas as possíveis senhas formadas por:
a) n dígitos
b) n dígitos ou letras minusculas
c) n dígitos ou letras minúsculas ou letras maiúsculas
"""
import string

n = int(input("Digite o valor de n: "))


import time

def generate_passwords(n):
    start_time = time.time()
    count = 0
    for i in range(10**n):
        #print(i)
        count += 1
    end_time = time.time()
    return end_time - start_time, count


def generate_passwords_digits_lowercase(n):
    start_time = time.time()
    count = 0
    caracteres = string.digits + string.ascii_lowercase
    
    for i in range(len(caracteres)**n):
        senha = ''
        temp = i
        for _ in range(n):
            senha = caracteres[temp % len(caracteres)] + senha
            temp //= len(caracteres)
        #print(senha)
        count += 1
    end_time = time.time()
    return end_time - start_time, count

def generate_passwords_digits_lowercase_uppercase(n):
    start_time = time.time()
    count = 0
    caracteres = string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    for i in range(len(caracteres)**n):
        senha = ''
        temp = i
        for _ in range(n):
            senha = caracteres[temp % len(caracteres)] + senha
            temp //= len(caracteres)
        #print(senha)
        count += 1
    end_time = time.time()
    return end_time - start_time, count

retorno_digits = generate_passwords(n)  
retorno_digits_lowercase = generate_passwords_digits_lowercase(n)
retorno_digits_lowercase_uppercase = generate_passwords_digits_lowercase_uppercase(n)

print(f"Tempo de execução: {retorno_digits[0]} segundos | Quantidade de senhas geradas: {retorno_digits[1]}")
print(f"Tempo de execução: {retorno_digits_lowercase[0]} segundos | Quantidade de senhas geradas: {retorno_digits_lowercase[1]}")
print(f"Tempo de execução: {retorno_digits_lowercase_uppercase[0]} segundos | Quantidade de senhas geradas: {retorno_digits_lowercase_uppercase[1]}")

