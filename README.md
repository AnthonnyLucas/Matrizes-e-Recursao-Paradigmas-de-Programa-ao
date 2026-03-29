# 📚 Matrizes e Recursão — Paradigmas de Programação

> Lista de exercícios da disciplina **Paradigmas de Programação**  
> UFRPE — Unidade Acadêmica de Belo Jardim | Prof. Denini Gabriel

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos](#requisitos)
- [Como Executar](#como-executar)
- [Exercícios](#exercícios)
  - [Parte I — Matrizes](#parte-i--matrizes)
  - [Parte II — Recursão](#parte-ii--recursão)
- [Exemplos de Saída](#exemplos-de-saída)
- [Guia de Modificação](#guia-de-modificação)
- [Decisões de Implementação](#decisões-de-implementação)
- [Autor](#autor)

---

## Sobre o Projeto

Este repositório contém a solução da **Lista de Exercícios — Matrizes e Recursão**, desenvolvida para a disciplina de Paradigmas de Programação da UFRPE-UAB.

O objetivo da lista é praticar a implementação de funções que manipulam **matrizes** (representadas como listas de listas em Python) e funções **estritamente recursivas** — sem o uso de laços `for` ou `while` onde o enunciado assim exige.

Todas as soluções foram implementadas como **funções puras**: recebem parâmetros, processam os dados e retornam o resultado, sem efeitos colaterais ou dependência de estado externo.

---

## Estrutura do Repositório

```
📦 matrizes-e-recursao/
├── 📄 s.py                      # Código principal com todas as soluções comentadas
├── 📄 Tabela_de_Consulta.txt    # Guia de uso e modificação para cada questão
└── 📄 README.md                 # Este arquivo
```

---

## Requisitos

- **Python** `3.6+`
- Nenhuma biblioteca externa necessária — apenas a biblioteca padrão do Python.

Para verificar sua versão do Python:

```bash
python --version
# ou
python3 --version
```

---

## Como Executar

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/matrizes-e-recursao.git
cd matrizes-e-recursao
```

**2. Execute o arquivo principal:**

```bash
python s.py
```

**3. A saída no terminal seguirá o formato:**

```
============================================================
  PARTE I — MATRIZES
============================================================

Q1  - Soma de todos os elementos:
      Entrada: [[1,2],[3,4]]  →  Saída: 10

Q2  - Maior elemento:
      Entrada: [[3,7],[2,9],[5,1]]  →  Saída: 9

...
```

---

## Exercícios

### Parte I — Matrizes

| # | Nome da Função | Descrição | Entrada | Saída |
|---|---|---|---|---|
| 1 | `soma_todos_elementos(matriz)` | Soma todos os elementos da matriz | `[[1,2],[3,4]]` | `10` |
| 2 | `maior_elemento(matriz)` | Retorna o maior valor presente na matriz | `[[3,7],[2,9],[5,1]]` | `9` |
| 3 | `soma_diagonal_principal(matriz)` | Soma os elementos da diagonal principal | `[[1,2,3],[4,5,6],[7,8,9]]` | `15` |
| 4 | `transposta(matriz)` | Retorna a transposta da matriz (sem funções prontas) | `[[1,2,3],[4,5,6]]` | `[[1,4],[2,5],[3,6]]` |
| 5 | `multiplicacao_escalar(matriz, k)` | Multiplica todos os elementos por um escalar k | `[[1,2],[3,4]], 3` | `[[3,6],[9,12]]` |
| 6 | `eh_matriz_identidade(matriz)` | Verifica se a matriz é a identidade | `[[1,0],[0,1]]` | `True` |
| 7 | `soma_matrizes(A, B)` | Soma elemento a elemento duas matrizes de mesma dimensão | `[[1,2],[3,4]], [[5,6],[7,8]]` | `[[6,8],[10,12]]` |
| 8 | `contar_maiores_que(matriz, X)` | Conta elementos estritamente maiores que X | `[[1,5,3],[8,2,7]], 4` | `3` |
| 9 | `linha_com_maior_soma(matriz)` | Retorna o índice da linha com maior soma | `[[1,2,3],[9,0,1],[4,4,4]]` | `2` |
| 10 | `media_todos_elementos(matriz)` | Retorna a média aritmética de todos os elementos | `[[2,4],[6,8]]` | `5.0` |

---

### Parte II — Recursão

| # | Nome da Função | Descrição | Entrada | Saída |
|---|---|---|---|---|
| 11 | `fatorial(n)` | Calcula n! de forma recursiva | `5` | `120` |
| 12 | `fibonacci(n)` | Retorna o n-ésimo termo da sequência de Fibonacci | `6` | `8` |
| 13 | `soma_ate_n(n)` | Calcula 1 + 2 + ... + n recursivamente | `4` | `10` |
| 14 | `potencia(b, e)` | Calcula b elevado a e recursivamente (e ≥ 0) | `2, 10` | `1024` |
| 15 | `contar_digitos(n)` | Conta a quantidade de dígitos de n recursivamente | `4823` | `4` |
| 16 | `inverter_string(s)` | Retorna a string invertida sem funções prontas | `"python"` | `"nohtyp"` |
| 17 | `eh_palindromo(s)` | Verifica recursivamente se a string é palíndromo (case-insensitive) | `"radar"` | `True` |
| 18 | `soma_digitos(n)` | Calcula a soma dos dígitos de n recursivamente | `1234` | `10` |

---

## Exemplos de Saída

Ao executar o arquivo, a saída completa esperada no terminal é:

```
============================================================
  PARTE I — MATRIZES
============================================================

Q1  - Soma de todos os elementos:
      Entrada: [[1,2],[3,4]]  →  Saída: 10

Q2  - Maior elemento:
      Entrada: [[3,7],[2,9],[5,1]]  →  Saída: 9

Q3  - Soma da diagonal principal:
      Entrada: [[1,2,3],[4,5,6],[7,8,9]]  →  Saída: 15

Q4  - Transposta:
      Entrada: [[1,2,3],[4,5,6]]  →  Saída: [[1, 4], [2, 5], [3, 6]]

Q5  - Multiplicação por escalar:
      Entrada: [[1,2],[3,4]], k=3  →  Saída: [[3, 6], [9, 12]]

Q6  - Verificar matriz identidade:
      [[1,0,0],[0,1,0],[0,0,1]]  →  True
      [[1,0],[1,1]]              →  False

Q7  - Soma de duas matrizes:
      A=[[1,2],[3,4]], B=[[5,6],[7,8]]  →  Saída: [[6, 8], [10, 12]]

Q8  - Contar elementos maiores que X:
      [[1,5,3],[8,2,7]], X=4  →  Saída: 3

Q9  - Linha com maior soma:
      [[1,2,3],[9,0,1],[4,4,4]]  →  Saída: 2

Q10 - Média de todos os elementos:
      [[2,4],[6,8]]  →  Saída: 5.0

============================================================
  PARTE II — RECURSÃO
============================================================

Q11 - Fatorial:
      fatorial(5)  →  120
      fatorial(0)  →  1

Q12 - Fibonacci:
      fibonacci(6)  →  8

Q13 - Soma de 1 até n:
      soma_ate_n(4)  →  10

Q14 - Potência inteira:
      potencia(2, 10)  →  1024

Q15 - Contar dígitos:
      contar_digitos(4823)  →  4

Q16 - Inverter string:
      inverter_string('python')  →  nohtyp

Q17 - Verificar palíndromo:
      eh_palindromo('radar')  →  True
      eh_palindromo('mundo')  →  False

Q18 - Soma dos dígitos:
      soma_digitos(1234)  →  10

============================================================
```

---

## Guia de Modificação

Para testar as funções com entradas diferentes, basta alterar os valores nos `print()` ao final do arquivo.

**Exemplo — alterando a questão 1:**

```python
# Valor atual
print(soma_todos_elementos([[1, 2], [3, 4]]))   # saída: 10

# Modificado
print(soma_todos_elementos([[5, 10], [15, 20]]))  # saída: 50
```

**Exemplo — alterando a questão 14:**

```python
# Valor atual
print(potencia(2, 10))   # saída: 1024

# Modificado
print(potencia(3, 5))    # saída: 243
```

> 📄 Para um guia completo com exemplos e cuidados para cada função individualmente, consulte o arquivo [`Tabela_de_Consulta.txt`](./Tabela_de_Consulta.txt).

---

## Decisões de Implementação

Algumas escolhas de implementação merecem destaque:

**Sem laços de repetição na Parte II**  
Todas as funções da Parte II (questões 11 a 18) foram implementadas sem o uso de `for` ou `while`, respeitando o enunciado original. O controle de fluxo é feito exclusivamente por chamadas recursivas com casos base bem definidos.

**Funções puras**  
Nenhuma função modifica a entrada original. Em `transposta` e `multiplicacao_escalar`, por exemplo, novas listas são criadas — as matrizes originais permanecem intactas. O mesmo vale para as funções de string como `inverter_string`.

**Palíndromo case-insensitive**  
A questão 17 converte a string para letras minúsculas antes da verificação, garantindo que `"Radar"` e `"radar"` sejam corretamente identificadas como palíndromos.

**Produto inicializado corretamente no Fatorial**  
Na questão 11, o caso base é `fatorial(0) = 1` (elemento neutro da multiplicação), garantindo que a recursão funcione corretamente para todos os inteiros não-negativos.

**Fibonacci e desempenho**  
A questão 12 utiliza recursão direta, que pode ser lenta para valores de n acima de 35 por recalcular os mesmos sub-problemas repetidamente. Para uso intensivo, recomenda-se aplicar memoização.

**Matrizes como listas de listas**  
Todas as funções da Parte I representam matrizes como listas de listas Python. As funções `soma_diagonal_principal` e `eh_matriz_identidade` assumem que a matriz de entrada é quadrada (n×n), conforme exigido pelo enunciado.

---

## Autor

Desenvolvido como atividade avaliativa da disciplina de **Paradigmas de Programação**.  
UFRPE — Unidade Acadêmica de Belo Jardim | Prof. Denini Gabriel.
