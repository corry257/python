# Introdução ao Python
- O que é o Python?
Python é uma linguagem de programação popular. Foi criada por Guido van Rossum e lançada em 1991.

- Ela é usada para:

   * Desenvolvimento web (lado do servidor),
   * Desenvolvimento de software,
   * Matemática,
   * Scripts de sistema.

- O que o Python pode fazer?
   * O Python pode ser usado em um servidor para criar aplicações web.
   * Ser usado junto com outros softwares para criar fluxos de trabalho.
   * Ele pode se conectar a sistemas de banco de dados. também pode ler e modificar arquivos.
   * Ser usado para lidar com grandes volumes de dados e realizar cálculos matemáticos complexos.
   * E ser utilizado para prototipagem rápida ou para o desenvolvimento de softwares prontos para produção.

- Por que Python?
   * O python funciona em diferentes plataformas (Windows, Mac, Linux, Raspberry Pi, etc.).
   * Tem uma sintaxe simples, semelhante à língua inglesa.
   * Possui uma sintaxe que permite aos desenvolvedores escrever programas com menos linhas em comparação com outras linguagens de programação.
   * É executado em um sistema interpretador, o que significa que o código pode ser executado assim que é escrito. Isso torna a prototipagem muito rápida.
   * Também pode ser usado de forma procedural, orientada a objetos ou funcional.
   
- É bom saber
A versão mais recente e principal do Python é o Python 3, que será utilizado aqui. No entanto, o Python 2, embora não receba atualizações além das de segurança, ainda é bastante popular.

# Váriaveis 

Em Python, os tipos de dados que podem ser atribuídos a variáveis são bastante diversos, 
eles podem ser classificados em categorias fundamentais e compostas.

Principais tipos de dados e como escrever para atribuir valores:

1. Numéricos
Usados para representar números.

class 'int'
Números inteiros (ex.: 1, 100, -5)
    x = 10

class 'float'
Números de ponto flutuante (ex.: 3.14, -0.5)
    x = 3.14

float em Python são usados para representar números decimais, 
ou seja, números que possuem uma parte inteira e uma parte fracionária separadas por um ponto decimal.

Por exemplo:

 3.14
 -0.5
 100.0

O nome "float" vem de "floating-point" (ponto flutuante), 
que se refere à forma como esses números são representados internamente no computador.
Esse tipo de dado é útil para cálculos que envolvem valores decimais ou frações.

No entanto, vale notar que números decimais em Python, quando representados como float, 
podem apresentar pequenas imprecisões devido à forma como os computadores lidam com números de ponto flutuante em binário.

Se você precisa de maior precisão para cálculos com números decimais (como em finanças),
o Python também oferece o módulo decimal. Por exemplo:

    from decimal import Decimal

    x = Decimal('0.1') + Decimal('0.2')
    pint(x)  # Retorna: 0.3

Enquanto com float:

    x = 0.1 + 0.2
    print(x) # Retorna: 0.30000000000000004 (imprecisão)

class 'complex'
Números complexos, na forma a + bj (ex.: 3+4j, 1j)
    x = 1 + 2j


2. Tipos de Texto
Usados para armazenar texto ou sequências de caracteres.

class 'str'
Cadeias de caracteres ou strings (ex.: "Hello", 'Python')
    x = "Hello, Python!"


3. Tipos Booleanos
Representam valores lógicos (verdadeiro ou falso).

class 'bool'
Verdadeiro (True) ou falso (False)
    x = True
    y = False


4. Tipos de Sequência
Representam coleções ordenadas de itens.

class 'list'
Listas são coleções mutáveis e ordenadas (ex.: [1, 2, 3])
    x = [1, 2, 3]

class 'tuple'
Tuplas são coleções imutáveis e ordenadas (ex.: (1, 2, 3))
    x = (1, 2, 3)

class 'range'
Intervalos de números, geralmente usados em loops (ex.: range(0, 10))
    x = range(5)


5. Tipos de Mapeamento
Representam pares chave-valor.

class 'dict'
Dicionários são coleções mutáveis e não ordenadas (ex.: {"chave": "valor"})
    x = {"name": "Alice", "age": 25}


6. Tipos de Conjuntos
Representam coleções não ordenadas e únicas de elementos.

class 'set'
Conjuntos mutáveis, sem elementos duplicados (ex.: {1, 2, 3})
    x = {1, 2, 3}

class 'frozenset'
Conjuntos imutáveis, sem elementos duplicados (ex.: frozenset({1, 2, 3}))
    x = frozenset({1, 2, 3})


7. Tipos Binários
Usados para armazenar dados em formato binário.

class 'bytes'
Bytes são sequências imutáveis de dados binários (ex.: b"data")
    x = b"Hello"

class 'bytearray'
Bytearray são sequências mutáveis de dados binários (ex.: bytearray(5))
    x = bytearray(5)

class 'memoryview'
Memoryview fornece uma visualização de objetos binários (ex.: memoryview(bytes(5)))
    x = memoryview(b"data")


8. Tipos Especiais
Usados para representar valores ou objetos especiais.

class 'NoneType'
NoneType representa a ausência de valor ou None (ex.: x = None)
    x = None

Esses são os principais tipos de dados em Python!