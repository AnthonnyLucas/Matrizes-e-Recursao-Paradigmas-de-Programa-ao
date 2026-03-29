# PARTE I — MATRIZES

# Questão 1: Soma de todos os elementos
def soma_todos_elementos(matriz):
    total = 0
    for linha in matriz:         
        for elem in linha:        
            total += elem
    return total                # Esperado 10

# -----------------------------------------------------------------------------
# Questão 2: Maior elemento

def maior_elemento(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elem in linha:
            if elem > maior:      
                maior = elem
    return maior               # Esperado 9

# -----------------------------------------------------------------------------
# Questão 3: Soma da diagonal principal

def soma_diagonal_principal(matriz):
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][i]    
    return total              # Esperado 15

# -----------------------------------------------------------------------------
# Questão 4: Transposta

def transposta(matriz):
    m = len(matriz)       
    n = len(matriz[0])    
    trans = []
    for j in range(n):           
        nova_linha = []
        for i in range(m):       
            nova_linha.append(matriz[i][j])
        trans.append(nova_linha)
    return trans                    # Esperado [[1,4],[2,5],[3,6]]

# -----------------------------------------------------------------------------
# Questão 5: Multiplicação por escalar

def multiplicacao_escalar(matriz, k):
    resultado = []
    for linha in matriz:
        nova_linha = []
        for elem in linha:
            nova_linha.append(elem * k)   
        resultado.append(nova_linha)
    return resultado                 # Esperado [[3,6],[9,12]]

# -----------------------------------------------------------------------------
# Questão 6: Verificar matriz identidade

def eh_matriz_identidade(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j:                    
                if matriz[i][j] != 1:
                    return False
            else:                         
                if matriz[i][j] != 0:
                    return False
    return True                                   # Esperado True / False

# -----------------------------------------------------------------------------
# Questão 7: Soma de duas matrizes

def soma_matrizes(A, B):
    resultado = []
    for i in range(len(A)):           
        nova_linha = []
        for j in range(len(A[0])):    
            nova_linha.append(A[i][j] + B[i][j])   
        resultado.append(nova_linha)
    return resultado                             # Esperado [[6,8],[10,12]]

# -----------------------------------------------------------------------------
# Questão 8: Contar elementos maiores que um valor

def contar_maiores_que(matriz, X):
    contador = 0
    for linha in matriz:
        for elem in linha:
            if elem > X:              
                contador += 1
    return contador                                # Esperado 3

# -----------------------------------------------------------------------------
# Questão 9: Linha com maior soma

def linha_com_maior_soma(matriz):
    indice_maior = 0                          
    maior_soma = sum(matriz[0])               

    for i in range(1, len(matriz)):           
        soma_atual = sum(matriz[i])
        if soma_atual > maior_soma:
            maior_soma = soma_atual
            indice_maior = i                  
    return indice_maior                            # Esperado 1

# -----------------------------------------------------------------------------
# Questão 10: Média de todos os elementos

def media_todos_elementos(matriz):
    total = 0
    quantidade = 0
    for linha in matriz:
        for elem in linha:
            total += elem
            quantidade += 1           
    return total / quantidade                     # Esperado 5.0


#PARTE II — RECURSÃO (sem laços for/while)

# Questão 11: Fatorial

def fatorial(n):
    if n == 0:                        
        return 1
    return n * fatorial(n - 1)                  # Esperado 120 / 1

# -----------------------------------------------------------------------------
# Questão 12: Fibonacci

def fibonacci(n):
    if n == 0:                              
        return 0
    if n == 1:                              
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # Esperado 8

# -----------------------------------------------------------------------------
# Questão 13: Soma de 1 até n

def soma_ate_n(n):
    if n == 1:                        
        return 1
    return n + soma_ate_n(n - 1)                  # Esperado 10

# -----------------------------------------------------------------------------
# Questão 14: Potência inteira

def potencia(b, e):
    if e == 0:                        
        return 1
    return b * potencia(b, e - 1)                # Esperado 1024

# -----------------------------------------------------------------------------
# Questão 15: Contar dígitos

def contar_digitos(n):
    if n < 10:                              
        return 1
    return 1 + contar_digitos(n // 10)           # Esperado 4

# -----------------------------------------------------------------------------
# Questão 16: Inverter string

def inverter_string(s):
    if len(s) <= 1:                               
        return s
    return s[-1] + inverter_string(s[:-1])        # Esperado nohtyp

# -----------------------------------------------------------------------------
# Questão 17: Verificar palíndromo

def eh_palindromo(s):
    s = s.lower()                              
    if len(s) <= 1:                             
        return True
    if s[0] != s[-1]:                           
        return False
    return eh_palindromo(s[1:-1])                   # Esperado true / false

# -----------------------------------------------------------------------------
# Questão 18: Soma dos dígitos

def soma_digitos(n):
    if n < 10:                              
        return n
    return (n % 10) + soma_digitos(n // 10)           # Esperado 10


# BLOCO DE TESTES 

if __name__ == "__main__":
    print("=" * 60)
    print("  PARTE I — MATRIZES")
    print("=" * 60)

    print(f"\nQ1  - Soma de todos os elementos:")
    print(f"      Entrada: [[1,2],[3,4]]  →  Saída: {soma_todos_elementos([[1,2],[3,4]])}")

    print(f"\nQ2  - Maior elemento:")
    print(f"      Entrada: [[3,7],[2,9],[5,1]]  →  Saída: {maior_elemento([[3,7],[2,9],[5,1]])}")

    print(f"\nQ3  - Soma da diagonal principal:")
    print(f"      Entrada: [[1,2,3],[4,5,6],[7,8,9]]  →  Saída: {soma_diagonal_principal([[1,2,3],[4,5,6],[7,8,9]])}")

    print(f"\nQ4  - Transposta:")
    print(f"      Entrada: [[1,2,3],[4,5,6]]  →  Saída: {transposta([[1,2,3],[4,5,6]])}")

    print(f"\nQ5  - Multiplicação por escalar:")
    print(f"      Entrada: [[1,2],[3,4]], k=3  →  Saída: {multiplicacao_escalar([[1,2],[3,4]], 3)}")

    print(f"\nQ6  - Verificar matriz identidade:")
    print(f"      [[1,0,0],[0,1,0],[0,0,1]]  →  {eh_matriz_identidade([[1,0,0],[0,1,0],[0,0,1]])}")
    print(f"      [[1,0],[1,1]]              →  {eh_matriz_identidade([[1,0],[1,1]])}")

    print(f"\nQ7  - Soma de duas matrizes:")
    print(f"      A=[[1,2],[3,4]], B=[[5,6],[7,8]]  →  Saída: {soma_matrizes([[1,2],[3,4]], [[5,6],[7,8]])}")

    print(f"\nQ8  - Contar elementos maiores que X:")
    print(f"      [[1,5,3],[8,2,7]], X=4  →  Saída: {contar_maiores_que([[1,5,3],[8,2,7]], 4)}")

    print(f"\nQ9  - Linha com maior soma:")
    print(f"      [[1,2,3],[9,0,1],[4,4,4]]  →  Saída: {linha_com_maior_soma([[1,2,3],[9,0,1],[4,4,4]])}")
    
    print(f"\nQ10 - Média de todos os elementos:")
    print(f"      [[2,4],[6,8]]  →  Saída: {media_todos_elementos([[2,4],[6,8]])}")

    print("\n" + "=" * 60)
    print("  PARTE II — RECURSÃO")
    print("=" * 60)

    print(f"\nQ11 - Fatorial:")
    print(f"      fatorial(5)  →  {fatorial(5)}")
    print(f"      fatorial(0)  →  {fatorial(0)}")

    print(f"\nQ12 - Fibonacci:")
    print(f"      fibonacci(6)  →  {fibonacci(6)}")

    print(f"\nQ13 - Soma de 1 até n:")
    print(f"      soma_ate_n(4)  →  {soma_ate_n(4)}")

    print(f"\nQ14 - Potência inteira:")
    print(f"      potencia(2, 10)  →  {potencia(2, 10)}")

    print(f"\nQ15 - Contar dígitos:")
    print(f"      contar_digitos(4823)  →  {contar_digitos(4823)}")

    print(f"\nQ16 - Inverter string:")
    print(f"      inverter_string('python')  →  {inverter_string('python')}")

    print(f"\nQ17 - Verificar palíndromo:")
    print(f"      eh_palindromo('radar')  →  {eh_palindromo('radar')}")
    print(f"      eh_palindromo('mundo')  →  {eh_palindromo('mundo')}")

    print(f"\nQ18 - Soma dos dígitos:")
    print(f"      soma_digitos(1234)  →  {soma_digitos(1234)}")

    print("\n" + "=" * 60)