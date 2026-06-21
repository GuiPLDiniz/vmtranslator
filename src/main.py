import sys
from pathlib import Path

from parser import Parser
from code_writer import CodeWriter


def translate(input_file):
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Erro: arquivo não encontrado: {input_path}")
        sys.exit(1)

    if input_path.suffix.lower() != ".vm":
        print("Erro: o arquivo de entrada deve ter extensão .vm")
        sys.exit(1)

    output_path = input_path.with_suffix(".asm")

    parser = Parser(input_path)
    writer = CodeWriter(output_path)

    while parser.has_more_commands():
        parser.advance()

        command_type = parser.command_type()

        if command_type == "C_PUSH":
            writer.write_push(parser.arg1(), parser.arg2())

        elif command_type == "C_POP":
            writer.write_pop(parser.arg1(), parser.arg2())

        elif command_type == "C_ARITHMETIC":
            writer.write_arithmetic(parser.arg1())

        elif command_type == "C_LABEL":
            writer.write_label(parser.arg1())

        elif command_type == "C_GOTO":
            writer.write_goto(parser.arg1())

        elif command_type == "C_IF":
            writer.write_if(parser.arg1())
        
        elif command_type == "C_FUNCTION":
            writer.write_function(
                parser.arg1(),
                parser.arg2()
            )
        
        elif command_type == "C_RETURN":
            writer.write_return()
        
        elif command_type == "C_CALL":
            writer.write_call(
                parser.arg1(),
                parser.arg2()
            )

    writer.close()

    print(f"[OK] Arquivo gerado: {output_path}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python src/main.py <arquivo.vm>")
        sys.exit(1)

    translate(sys.argv[1])


if __name__ == "__main__":
    main()