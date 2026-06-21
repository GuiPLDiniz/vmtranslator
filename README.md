# VMTranslator – Projects 07 e 08

## Disciplina

Compiladores

## Integrante

* **Guilherme Pessoa Lima Diniz**
* **Matrícula:** 20260001310

---

## Linguagem Utilizada

* Python 3
* Versão utilizada: Python 3.14

---

## Descrição do Projeto

Este projeto implementa o **VMTranslator** do curso **nand2tetris**, responsável por traduzir programas escritos na linguagem de Máquina Virtual (VM) para código Assembly da arquitetura Hack.

A implementação contempla integralmente os requisitos dos **Projects 07 e 08**, incluindo:

* Acesso à memória (`push` e `pop`)
* Operações aritméticas
* Operações lógicas
* Operações relacionais
* Controle de fluxo (`label`, `goto`, `if-goto`)
* Declaração de funções (`function`)
* Chamadas de funções (`call`)
* Retorno de funções (`return`)
* Código de inicialização (*bootstrap*)
* Tradução de múltiplos arquivos `.vm` em um único programa Assembly

O tradutor recebe como entrada um arquivo `.vm` ou um diretório contendo múltiplos arquivos `.vm`, gerando automaticamente um arquivo `.asm` equivalente.

---

# Funcionalidades Implementadas

## Comandos de Memória

### Push

* `push constant`
* `push local`
* `push argument`
* `push this`
* `push that`
* `push temp`
* `push pointer`
* `push static`

### Pop

* `pop local`
* `pop argument`
* `pop this`
* `pop that`
* `pop temp`
* `pop pointer`
* `pop static`

---

## Operações Aritméticas

* `add`
* `sub`
* `neg`

---

## Operações Lógicas

* `and`
* `or`
* `not`

---

## Operações Relacionais

* `eq`
* `gt`
* `lt`

As operações relacionais utilizam geração automática de rótulos (*labels*) únicos para evitar conflitos durante a tradução.

---

## Controle de Fluxo

* `label`
* `goto`
* `if-goto`

---

## Chamadas de Funções

* `function`
* `call`
* `return`

Implementadas conforme a especificação oficial do nand2tetris, incluindo:

* Criação de variáveis locais
* Salvamento e restauração do contexto da função chamadora
* Manipulação dos segmentos `LCL`, `ARG`, `THIS` e `THAT`
* Geração automática de endereços de retorno

---

## Bootstrap

Foi implementado o código de inicialização obrigatório:

```asm
@256
D=A
@SP
M=D
```

seguido da chamada:

```vm
call Sys.init 0
```

necessária para execução dos programas dos testes do Project 08.

---

## Segmento Static

O segmento `static` foi implementado utilizando namespace por arquivo, conforme exigido pelo nand2tetris.

Exemplos:

```text
Class1.0
Class1.1
Class2.0
Class2.1
```

---

# Estrutura do Projeto

```text
vmtranslator/
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── code_writer.py
│   └── test_runner.py
│
├── tests/
│   ├── projects07/
│   │   ├── StackArithmetic/
│   │   └── MemoryAccess/
│   │
│   └── projects08/
│       ├── ProgramFlow/
│       └── FunctionCalls/
│
├── .gitignore
└── README.md
```

---

# Componentes do Sistema

## Parser

Responsável por:

* Ler arquivos `.vm`
* Ignorar comentários
* Ignorar linhas vazias
* Identificar o tipo de comando
* Extrair argumentos

Tipos de comando suportados:

* `C_PUSH`
* `C_POP`
* `C_ARITHMETIC`
* `C_LABEL`
* `C_GOTO`
* `C_IF`
* `C_FUNCTION`
* `C_CALL`
* `C_RETURN`

Principais métodos:

* `has_more_commands()`
* `advance()`
* `command_type()`
* `arg1()`
* `arg2()`

---

## CodeWriter

Responsável pela geração do código Assembly Hack.

Principais métodos:

* `write_push()`
* `write_pop()`
* `write_arithmetic()`
* `write_comparison()`
* `write_label()`
* `write_goto()`
* `write_if()`
* `write_function()`
* `write_call()`
* `write_return()`
* `write_init()`
* `close()`

---

## Main

Responsável por:

* Receber um arquivo ou diretório como entrada
* Instanciar Parser e CodeWriter
* Traduzir múltiplos arquivos VM
* Gerar o arquivo `.asm`
* Inserir automaticamente o bootstrap quando necessário

---

# Como Executar

## Traduzir um único arquivo VM

Exemplo:

```bash
python src/main.py tests/projects07/MemoryAccess/BasicTest/BasicTest.vm
```

Será gerado:

```text
BasicTest.asm
```

na mesma pasta do arquivo de entrada.

---

## Traduzir um diretório

Exemplo:

```bash
python src/main.py tests/projects08/FunctionCalls/NestedCall
```

Será gerado:

```text
NestedCall.asm
```

na pasta do diretório informado.

---

# Exemplo de Uso

Entrada:

```vm
push constant 7
push constant 8
add
```

Saída Assembly gerada:

```asm
@7
D=A
@SP
A=M
M=D
@SP
M=M+1

@8
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
A=A-1
M=M+D
```

---

# Testes Realizados

A implementação foi validada utilizando os testes oficiais dos Projects 07 e 08 do nand2tetris.

## Project 07

### StackArithmetic

* SimpleAdd
* StackTest

### MemoryAccess

* BasicTest
* PointerTest
* StaticTest

---

## Project 08

### ProgramFlow

* BasicLoop
* FibonacciSeries

### FunctionCalls

* SimpleFunction
* NestedCall
* FibonacciElement
* StaticsTest

Todos os testes foram executados utilizando os scripts oficiais `.tst` fornecidos pelo nand2tetris e validados através do CPU Emulator.

Resultado obtido em todos os testes:

```text
Comparison ended successfully
```

---

# Estratégia de Implementação

O desenvolvimento foi realizado de forma incremental:

1. Implementação do Parser
2. Implementação de acesso à memória
3. Implementação das operações aritméticas
4. Implementação das operações lógicas
5. Implementação das operações relacionais
6. Implementação do controle de fluxo
7. Implementação de funções
8. Implementação de chamadas e retornos
9. Implementação do bootstrap
10. Suporte a múltiplos arquivos
11. Correção do segmento static
12. Validação com os testes oficiais

---

# Conclusão

O projeto atende integralmente aos requisitos dos Projects 07 e 08 do nand2tetris e da disciplina de Compiladores.

Foram implementados todos os comandos de acesso à memória, operações aritméticas, lógicas e relacionais, controle de fluxo, chamadas de função, retorno de função, bootstrap e tradução de múltiplos arquivos VM, com validação bem-sucedida através dos testes oficiais disponibilizados pelo nand2tetris.
