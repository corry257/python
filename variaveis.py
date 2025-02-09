# Em Python, os tipos de dados que podem ser atribuídos a variáveis são bastante diversos 
# podem ser classificados em categorias fundamentais e compostas.

# 1.Numéricos
# Usados para representar números.

# int: Números inteiros (ex.: 1, 100, -5)
# x = 10  # Tipo: int

# float: Números de ponto flutuante (ex.: 3.14, -0.5)
# x = 3.14  # Tipo: float

# os números float em Python são usados para representar números decimais, 
# ou seja, números que possuem uma parte inteira e uma parte fracionária separadas por um ponto decimal.

# Por exemplo:

# 3.14
# -0.5
# 100.0

# O nome "float" vem de "floating-point" (ponto flutuante), 
# que se refere à forma como esses números são representados internamente no computador. 
# Esse tipo de dado é útil para cálculos que envolvem valores decimais ou frações.

# No entanto, vale notar que números decimais em Python, quando representados como float, 
# podem apresentar pequenas imprecisões devido à forma como os computadores lidam com números de ponto flutuante em binário.

# Se você precisa de maior precisão para cálculos com números decimais (como em finanças), o Python também oferece a biblioteca decimal. Por exemplo:

# por exemplo: 
# # from decimal import Decimal

# x = Decimal('0.1') + Decimal('0.2')
# print(x)  # Retorna: 0.3 (precisão)

# Enquanto com float:

# x = 0.1 + 0.2
# print(x)  # Retorna: 0.30000000000000004 (imprecisão)

# complex: Números complexos, na forma a + bj (ex.: 3+4j, 1j)
# x = 1 + 2j  # Tipo: complex


# 2. Tipos de Texto
# Usados para armazenar texto ou sequências de caracteres.

# str: Cadeias de caracteres ou strings (ex.: "Hello", 'Python')
# x = "Hello, Python!"  # Tipo: str


# 3. Tipos Booleanos
# Representam valores lógicos (verdadeiro ou falso).

# bool: Verdadeiro (True) ou falso (False)
# x = True  # Tipo: bool


# 4. Tipos de Sequência
# Representam coleções ordenadas de itens.

# list: Lista, coleção mutável e ordenada (ex.: [1, 2, 3])
# x = [1, 2, 3]  # Tipo: list

# tuple: Tupla, coleção imutável e ordenada (ex.: (1, 2, 3))
# x = (1, 2, 3)  # Tipo: tuple

# range: Intervalo de números, geralmente usado em loops (ex.: range(0, 10))
# x = range(5)  # Tipo: range


# 5. Tipos de Mapeamento
# Representam pares chave-valor.

# dict: Dicionário, coleção mutável e não ordenada (ex.: {"chave": "valor"})
# x = {"name": "Alice", "age": 25}  # Tipo: dict


# 6. Tipos de Conjuntos
# Representam coleções não ordenadas e únicas de elementos.

# set: Conjunto mutável, sem elementos duplicados (ex.: {1, 2, 3})
# x = {1, 2, 3}  # Tipo: set

# frozenset: Conjunto imutável, sem elementos duplicados (ex.: frozenset({1, 2, 3}))
# x = frozenset({1, 2, 3})  # Tipo: frozenset


# 7. Tipos Binários
# Usados para armazenar dados em formato binário.

# bytes: Sequência imutável de dados binários (ex.: b"data")
# x = b"Hello"  # Tipo: bytes

# bytearray: Sequência mutável de dados binários (ex.: bytearray(5))
# x = bytearray(5)  # Tipo: bytearray

# memoryview: Visualização de objetos binários (ex.: memoryview(bytes(5)))
# x = memoryview(b"data")  # Tipo: memoryview


# 8. Tipos Especiais
# Usados para representar valores ou objetos especiais.

# NoneType: Representa a ausência de valor ou None (ex.: x = None)
# x = None  # Tipo: NoneType


# Outras Características
# Variáveis dinâmicas: O Python permite que você mude o tipo da variável ao longo do código, pois é uma linguagem de tipagem dinâmica.

# x = 42       # Tipo: int
# x = "texto"  # Tipo: str

print('Em Python, os tipos de dados que podem ser atribuídos a variáveis são bastante diversos, ')
print('eles podem ser classificados em categorias fundamentais e compostas.')
print('\nPrincipais tipos de dados e como escrever para atribuir valores:')

print('\n1. Numéricos')
print('Usados para representar números.\n')

x = 10
print(type(x)) 
print('Números inteiros (ex.: 1, 100, -5)') 
print('x = 10\n') 

x = 3.14
print(type(x))
print('Números de ponto flutuante (ex.: 3.14, -0.5)')
print('x = 3.14\n') 

print('float em Python são usados para representar números decimais, ')
print('ou seja, números que possuem uma parte inteira e uma parte fracionária separadas por um ponto decimal.')

print('\nPor exemplo:\n')

print(' 3.14\n','-0.5\n','100.0\n')

print('O nome "float" vem de "floating-point" (ponto flutuante), ')
print('que se refere à forma como esses números são representados internamente no computador.')
print('Esse tipo de dado é útil para cálculos que envolvem valores decimais ou frações.\n')

print('No entanto, vale notar que números decimais em Python, quando representados como float, ')
print('podem apresentar pequenas imprecisões devido à forma como os computadores lidam com números de ponto flutuante em binário.\n')

print('Se você precisa de maior precisão para cálculos com números decimais (como em finanças),')
print('o Python também oferece o módulo decimal. Por exemplo:\n')

print('from decimal import Decimal\n')

print("x = Decimal('0.1') + Decimal('0.2')")
print("pint(x)  # Retorna: 0.3\n")

print('Enquanto com float:\n')

print('x = 0.1 + 0.2')
print('print(x) # Retorna: 0.30000000000000004 (imprecisão)\n')

x = 1 + 2j
print(type(x))
print('Números complexos, na forma a + bj (ex.: 3+4j, 1j)')
print('x = 1 + 2j\n') 


print('\n2. Tipos de Texto')
print('Usados para armazenar texto ou sequências de caracteres.\n')

x = "Hello, Python!"
print(type(x))
print('Cadeias de caracteres ou strings (ex.: "Hello", \'Python\')')
print('x = "Hello, Python!"\n') 


print('\n3. Tipos Booleanos')
print('Representam valores lógicos (verdadeiro ou falso).\n')

x = True
print(type(x))
print('Verdadeiro (True) ou falso (False)')
print('x = True') 
print('y = False\n')


print('\n4. Tipos de Sequência')
print('Representam coleções ordenadas de itens.\n')

x = [1, 2, 3]
print(type(x))
print('Listas são coleções mutáveis e ordenadas (ex.: [1, 2, 3])')
print('x = [1, 2, 3]\n') 

x = (1, 2, 3)
print(type(x))
print('Tuplas são coleções imutáveis e ordenadas (ex.: (1, 2, 3))')
print('x = (1, 2, 3)\n') 

x = range(5)
print(type(x))
print('Intervalos de números, geralmente usados em loops (ex.: range(0, 10))')
print('x = range(5)\n') 


print('\n5. Tipos de Mapeamento')
print('Representam pares chave-valor.\n')

x = {"name": "Alice", "age": 25}
print(type(x))
print('Dicionários são coleções mutáveis e não ordenadas (ex.: {"chave": "valor"})')
print('x = {"name": "Alice", "age": 25}\n') 


print('\n6. Tipos de Conjuntos')
print('Representam coleções não ordenadas e únicas de elementos.\n')

x = {1, 2, 3}
print(type(x))
print('Conjuntos mutáveis, sem elementos duplicados (ex.: {1, 2, 3})')
print('x = {1, 2, 3}\n') 

x = frozenset({1, 2, 3})
print(type(x))
print('Conjuntos imutáveis, sem elementos duplicados (ex.: frozenset({1, 2, 3}))')
print('x = frozenset({1, 2, 3})\n') 


print('\n7. Tipos Binários')
print('Usados para armazenar dados em formato binário.\n')

x = b"Hello"
print(type(x))
print('Bytes são sequências imutáveis de dados binários (ex.: b"data")')
print('x = b"Hello"\n') 

x = bytearray(5)
print(type(x))
print('Bytearray são sequências mutáveis de dados binários (ex.: bytearray(5))')
print('x = bytearray(5)\n') 

x = memoryview(b"data")
print(type(x))
print('Memoryview fornece uma visualização de objetos binários (ex.: memoryview(bytes(5)))')
print('x = memoryview(b"data")\n') 


print('\n8. Tipos Especiais')
print('Usados para representar valores ou objetos especiais.\n')

x = None
print(type(x))
print('NoneType representa a ausência de valor ou None (ex.: x = None)')
print('x = None') 


print('\nEsses são os principais tipos de dados em Python!')


# Função isnistance()
# a = 10 
# b = 'sol'
# print(isinstance(a,(int, float)))

# a = 40 
# c = 3 
# r = a * c 
# print(r)