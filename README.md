# Curso de Python 3
  Registrando meu aprendizado no Curso de Python do professor Gustavo Guanabara.

  ## Minha jornada em Python 3 - Curso em Vídeo
  Esse repositório foi criado para registrar toda a minha evolução, códigos e desafios com a linguagem Python.

  ## Progresso do Curso
  - [x] **Mundo 1:** Fundamentos 
  - [ ] **Mundo 2:** Estruturas de Controle
  - [ ] **Mundo 3:**

  ## Mundo 1: Fundamentos
  Aulas assistidas e conceitos práticos aplicados até o momento:

  ### Aula 04 - Primeiros comandos em Python

  Sintaxe básica da linguagem, interação com usuário e criação de variáveis.

  * **Comandos aprendidos:** `print()`, `input()` - escreva / leia
  * **Código exemplo:** 
  ``` python
  nome = input('Qual é o seu nome? ')
  print('Olá', nome, '! Prazer em te conhecer!')
  ```
  ### Aula 05 - Instalando o PyCharm e o Python
  Configuração do ambiente de desenvolvimento para escrever os códigos.

  ### Aula 06 - Tipos Primitivos e Saídas de Dados

  Aprendi a converter os dados para o tipo correto e usar a máscara de formatação `.format()`.

  * **Tipos vistos:** 
    - `int`: números inteiros (3, 6, 89, -0, 12)
    - `float`: números reais (-3.5, 2.1, 67.8, 0.0)
    - `bool`: valores lógicos (True ou False)
    - `str`: tudo que está entre  aspas simples ou duplas ('Olá', '78', '3.5')
    
  * **Código exemplo:**
  ``` python
  n1 = int(input('Escolha um número: '))
  n2 = int(input('Escolha o segundo: '))
  soma = n1 + n2
  print(f'A soma entre {n1} e {n2} vale {soma}.')
  ```
  * O uso do `f` antes das aspas em Python serve para criar uma `f-string` (string formatada).

  ### Aula 07 - Operadores Aritméticos e Ordem de Precedência

  Entendi a ordem de precedência que o computador utiliza para fazer contas e como realizar operações matemáticas básicas.

  #### Operadores Aritméticos 
  | Operador | Operação | Exemplo | Resultado |
  |   ---    |     ---  |   ---   |    ---    |
  |   `+`    | `Adição` | `5 + 2` |    `7`    |
  |   `-`    | `Subtra.`| `5 - 2` |    `3`    |
  |   `*`    | `Multp.` | `5 * 2` |    `10`   |
  |   `/`    | `Divisão`| `5 / 2` |    `2.5`  |
  |   `//`   | `Div.Int`| `5 // 2`|    `2`    |
  |   `%`    |`Rest.Div`| `5 % 2` |    `1`    |
  |   `**`   |`Potencia`| `5 ** 5`|    `25`   |

  #### Ordem de Precedência
  Quem vamos resolver primeiro em uma equação? 

  1. **`()` Parenteses:** Tudo dentro dele é resolvido primeiro.
  2. **`**` Potência:** Logo em seguida vem a potência.
  3. **`*`, `/`, `//`, `%` Mult, Div, Div.Inteira, Resto.Div:** Possuem a mesma importância, e são resolvidas na ordem que aparecem.
  4. **`+`,`-` Adição e Subt.:** Realizada por último.

  ### Aula 08 - Utilizando Módulos (Bibliotecas)

  Nesta aula aprendi a expandir as capacidades do Python importando módulos. Entendi a diferença entre trazer todas as ferramentas de uma biblioteca, ou importar somente as que eu vou usar.

  #### Formas de Importação

  * **Importação Geral (`import`):** Traz a biblioteca inteira para o projeto.

    ```python
    import math
    num = int(input('Digite um número: '))
    raiz = math.sqrt(num)
    # É obrigatório usar o 'math' antes do comando
    ```
  * **Importação Otimizada (`from..import`):** Traz somente as funções específicas que você vai utilizar.
    * **Dica:** Para importar mais de uma função ao mesmo tempo, separamos elas com uma **vírgula**.
    
    ```python
    from math import sqrt, floor
    num = int(input('Digite um número: '))
    raiz = sqrt(num) # Não tem necessidade do 'math'
    print(f'A raiz é {raiz:.2f}, e arredondada para baixo é {floor(raiz)}.')
    ```

  #### Alguns módulos vistos:
  * `math`: Biblioteca de funções matemáticas.
  * `random`: Biblioteca para gerar e escolher números/itens aleatoriamente.
  * `floor()`: Função que arredonda um número para baixo.
  * `pow()` : Função para cálculo de potência.
  * `trunc()`: Elimina os valores após a vírgula.

  ### Aula 09 - Manipulando Cadeias de Texto (Strings)

  Nesta aula aprendi a a manipular textos em Python. Para o computador, uma frase é uma sequência de caracteres guardados em posições (índices), que iniciam em **0**, e não em **1**.

  **Mapa de Índice da frase:** `Curso em Vídeo Python`
  * No Python, a contagem real dos índices começa em 0: `0,1,2,3,4...até 20` (Total de 21 caracteres).
  * *Regra:* Para o Python, letras maiúsculas são completamentes diferentes das minúsculas (`A` , `a`).

  #### Fatiamento (Pegar pedaços da string)
  ```python
  frase = 'Curso em Vídeo Python
  print(frase[9]) # Retorna 'V'. A contagem inicia em 0, pegando o caractere da posição 9.
  print(frase[9:14]) # Retorna 'Vídeo'. Vai do 9 ao 13. O último valor (14) sempre fica de fora.
  print(frase[9:21]) # Retorna 'Vídeo Python'. Vai de 9 até o fim do texto (índice 20)
  print(frase[9:21:2]) # Retorna 'VdoPto'. Fatia de 9 ao 20 pulando de 2 em 2.
  print(frase[:5]) # Retorna 'Curso'. Quando não há inicio, ele começa no 0 e vai até 4.
  print(frase[15:]) # Retorna 'Python'. Começa no índice 15 e vai até o final.
  print(frase[9::3]) # Retorna 'Venty'. Começa em 9, vai até o final (pois não mostra onde ele dev parar) pulando de 3 em 3.
  ```
  #### Análise de String
  ```python
  print(len(frase)) # Retorna 21. Verifica o tamanho total da frase em caracteres.
  print(frase.count('o')) # Retorna 3. Conta quantas letras 'o' minúsculas existem na frase.
  print(frase.count('o',0,14)) # Retorna 2. Conta a letra 'o' apenas no pedaço que vai do índice 0 ao 13.
  print(frase.find('deo')) # Retorna 11. Diz em qual posição o pedaço 'deo' começou.
  print(frase.find('Android')) # Retorna -1. Quando você procura algo que não existe, o resultado é sempre -1.
  print('Curso' in frase) # Retorna True. Verifica se a palavra existe na frase e retorna True ou False.
  ```

  #### Transformação de Strings
  ```python
  print(frase.replace('Python', 'Android')) # Substitui 'Python' por 'Android' apenas na exibição.
  print(frase.upper()) # Transforma todas as letras em MAIÚSCULAS.
  print(frase.lower()) # Transforma todas as letras em minúsculas.
  print(frase.capitalize()) # Joga tudo para minúsculo e deixa SÓ o primeiro caractere da frase em maiúsculo.
  print(frase.title()) # Analisa os espaços e transforma a primeira letra de CADA palavra em maiúscula.
  print(frase.strip()) # Remove espaços inúteis antes do início e depois do fim do texto.
  print(frase.rstrip()) # Remove espaços inúteis apenas do lado direito (Right).
  print(frase.lstrip()) # Remove espaços inúteis apenas do lado esquerdo (Left)
  ```

  *Combinando métodos:* É possível juntar transformações em sequência, o código `print(frase.upper().count('o'))` vai retornar `0`, pois o `.upper` transformou toda a frase em maiúscula, logo, não existe mais letras minúsculas para serem contadas.

  #### Divisão e Junção
  ```python
  print(frase.split()) # Divide a frase onde existem espaços, criando uma lista de palavras com novos índices.
  print('-'.join(frase)) # Junta os elementos inserindo o hífen entre cada caractere ('C-u-r-s-o...').
  ```
  *Dica para texto:* Para escrevar um texto com várias linhas sem precisar escrever inúmeros `print()`, coloque o texto dentro de três aspas duplas ***(""")***, abrindo e fechando seu texto.
  ```python
  print("""Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica.
  Ele sobreviveu não apenas a muitas décadas, mas também à transição 
  para a editoração eletrônica.""")
  ```
  ### Aula 10 - Estruturas Condicionais (Parte 1)
  Nesta aula aprendi a criar desvios com as estruturas condicionais, permitindo que o programa siga caminhos diferentes, 

  * **Identação:** É o recuo do código para direita. No Python, ela serve para dizer quais comandos estão no bloco `if`, e os que estão no `else.` Tudo fora desse bloco SEMPRE irá aparecer, idependente do resultado da condição.

  #### Condicionais Simples
  Possui apenas o bloco `if` (Se). Se a condição for falsa, o programa ignora o bloco e segue em frente.

  ```python
  nome = str(input('Digite seu nome: '))
  if nome == 'Gabriela':
    print('Nossa, que nome lindo!') # esse bloco só acontece se o nome for Gabriela
  print(f'Bom dia, {nome}!') # esse bloco SEMPRE vai acontecer, está fora do bloco identado.
  ```
  #### Condicionais Compostas
  Possui o bloco `if` (Se) e o bloco `else` (Senão), abrindo dois caminhos possíveis no programa.

  ```python
  tempo = int(input('Quanto tempo tem seu carro? '))
  if tempo <= 5:
    print(f'Seu carro só tem {tempo} anos, está novinho') # executa se for Verdadeiro
  else:
    print(f'Seu carro já tem {tempo} anos, hora de ficar de olho.') # executa se for Falso
  print('--------- FIM DO PROGRAMA ------------')
  ```
  * **OBS:** As duas condições nunca acontecem juntas ao mesmo tempo. 
  Ou será o bloco True, ou o False.

  #### Exemplo Prático: Cálculo de Média
  ```python
  n1 = float(input('Digite a primeira nota: '))
  n2 = float(input('Digite a segunda nota: '))
  media = (n1 + n2) / 2
  print(f'A média do aluno foi {media:.1f}')

  if media <= 6.0:
    print(f'Sua média foi {media:.1f}, você consegue melhorar um pouquinho.')
  else:
    print(f'Oba! Sua média foi {media:.1f}, continue assim!')
  ```
  ### Aula 11 - Cores no Terminal
  Nesta aula aprendi a usar o padrão **ANSI (escape sequence)** para adicionar cores e estilos aos textos exibidos no terminal.

  #### Estrutura do Código ANSI
  O código sempre começa com `\033[` e termina coma letra `m`. Entre eles, separamos por ponto e vírgula os códigos de **Estilo;Texto;Fundo**.
  * **Exemplo:** `print(\033[0;33;44m)` \ `0` (Estilo), `33` (Cor do Texto), `44` (Cor de Fundo).

  #### Tabelas de Referência ANSI
  | Código | Estilo de Texto|
  | ---    |    ---         | 
  | `0`    |   **Padrão**   |
  | `1`    |   **Negrito**  |
  | `4`    | **Sublinhado** |
  | `7`    |   **Inversão** | # (inverte as cores de texto e fundo)

  
