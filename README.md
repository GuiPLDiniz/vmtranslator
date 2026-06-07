# VMTranslator – Parte 1

## Disciplina

Compiladores

## Integrante

* **Guilherme Pessoa Lima Diniz**
* **Matrícula:** 20260001310

## Linguagem Utilizada

* Python 3
* Versão utilizada: Python 3.14

## Descrição do Projeto

Este projeto implementa a **Parte 1 do VMTranslator** do curso **nand2tetris**, responsável por traduzir programas escritos na linguagem de máquina virtual (VM) para código Assembly da arquitetura Hack.

Nesta etapa foram implementados:

* Comandos de acesso à memória (`push` e `pop`)
* Operações aritméticas
* Operações lógicas
* Operações relacionais

O tradutor recebe um arquivo `.vm` como entrada e gera automaticamente um arquivo `.asm` equivalente.

---

## Funcionalidades Implementadas

### Comandos de Memória

#### Push

* `push constant`
* `push local`
* `push argument`
* `push this`
* `push that`
* `push temp`
* `push pointer`
* `push static`

#### Pop

* `pop local`
* `pop argument`
* `pop this`
* `pop that`
* `pop temp`
* `pop pointer`
* `pop static`

---

### Operações Aritméticas

* `add`
* `sub`
* `neg`

---

### Operações Lógicas

* `and`
* `or`
* `not`

---

### Operações Relacionais

* `eq`
* `gt`
* `lt`

As operações relacionais utilizam geração automática de rótulos (*labels*) únicos para evitar conflitos durante a tradução.

---

## Estrutura do Projeto

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
│   └── projects07/
│       ├── StackArithmetic/
│       │   ├── SimpleAdd/
│       │   └── StackTest/
│       │
│       └── MemoryAccess/
│           ├── BasicTest/
│           ├── PointerTest/
│           └── StaticTest/
│
├── .gitignore
└── README.md
```

---

## Componentes do Sistema

### Parser

Responsável por:

* Ler arquivos `.vm`
* Ignorar comentários
* Ignorar linhas vazias
* Identificar o tipo de comando
* Extrair argumentos

Principais métodos:

* `has_more_commands()`
* `advance()`
* `command_type()`
* `arg1()`
* `arg2()`

---

### CodeWriter

Responsável por converter comandos VM em instruções Assembly Hack.

Principais métodos:

* `write_push()`
* `write_pop()`
* `write_arithmetic()`
* `write_comparison()`
* `close()`

---

### Main

Responsável por:

* Receber o arquivo VM informado pelo usuário
* Instanciar Parser e CodeWriter
* Processar todos os comandos
* Gerar o arquivo `.asm`

---

## Como Executar

### Traduzir um arquivo VM

Exemplo:

```bash
python src/main.py tests/projects07/MemoryAccess/BasicTest/BasicTest.vm
```

O comando acima gera automaticamente:

```text
BasicTest.asm
```

na mesma pasta do arquivo de entrada.

---

## Exemplo de Uso

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

## Testes Realizados

A implementação foi validada utilizando os testes oficiais do **Project 07** do nand2tetris.

### StackArithmetic

* SimpleAdd
* StackTest

### MemoryAccess

* BasicTest
* PointerTest
* StaticTest

Todos os testes foram executados por meio dos scripts oficiais `.tst` utilizando o CPU Emulator.

Resultado obtido:

```text
Comparison ended successfully
```

em todos os casos.

---

## Estratégia de Implementação

O desenvolvimento foi realizado de forma incremental:

1. Implementação do Parser
2. Implementação de `push constant`
3. Implementação das operações aritméticas básicas
4. Implementação dos segmentos de memória
5. Implementação das operações lógicas
6. Implementação das operações relacionais
7. Validação com os testes oficiais

Essa abordagem facilitou a identificação e correção de erros durante o desenvolvimento.

---

## Conclusão

O projeto atende aos requisitos da Parte 1 do VMTranslator propostos pelo nand2tetris e pela disciplina de Compiladores.

Foram implementados todos os comandos de acesso à memória e todas as operações aritméticas, lógicas e relacionais exigidas, com validação bem-sucedida através dos testes oficiais disponibilizados para o Project 07.
