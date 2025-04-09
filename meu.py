def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("=== Calculadora Matemática ===")
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = somar(num1, num2)
elif operacao == '-':
    resultado = subtrair(num1, num2)
elif operacao == '*':
    resultado = multiplicar(num1, num2)
elif operacao == '/':
    resultado = dividir(num1, num2)
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
