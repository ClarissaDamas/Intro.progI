#funcao somando dois numeros

def fibonacci(num1):
    if num1 == 0:
        return 1
    elif num1 == 1:
        return 1
    else:
        num1 += 1
        num1 = num1 + (num1+1)
    print(num1)
    
valor = int(input('qual valor voce quer somar? '))
print(fibonacci(valor))



