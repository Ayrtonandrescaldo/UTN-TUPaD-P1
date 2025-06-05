# 1
def factorial(n):
    if n < 0:
        return None
    return 1 if n in (0, 1) else n * factorial(n - 1)

def lista_factoriales_hasta(n):
    return [factorial(i) for i in range(1, n + 1)]

# 2
def fibonacci(n):
    if n < 0:
        return None
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)

def serie_fibonacci_hasta(n):
    return [fibonacci(i) for i in range(n + 1)]

# 3
def potencia(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / potencia(base, -exp)
    return base * potencia(base, exp - 1)

# 4
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7
def contar_bloques(n):
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)

# 8
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

if __name__ == "__main__":
    print("Factoriales:", lista_factoriales_hasta(5))
    print("Fibonacci:", serie_fibonacci_hasta(7))
    print("Potencia:", potencia(2, 8))
    print("Binario:", decimal_a_binario(10))
    print("Palíndromo:", es_palindromo("reconocer"))
    print("Suma dígitos:", suma_digitos(1234))
    print("Bloques pirámide:", contar_bloques(4))
    print("Contar dígitos:", contar_digito(12233421, 2))
