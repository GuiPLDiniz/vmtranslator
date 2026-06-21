import sys
from pathlib import Path

from parser import Parser
from code_writer import CodeWriter


def translate_file(input_path, writer):

    parser = Parser(input_path)

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

        elif command_type == "C_CALL":
            writer.write_call(
                parser.arg1(),
                parser.arg2()
            )

        elif command_type == "C_RETURN":
            writer.write_return()


def translate(input_path_str):

    input_path = Path(input_path_str)

    if not input_path.exists():
        print(f"Erro: caminho não encontrado: {input_path}")
        sys.exit(1)

    if input_path.is_file():

        if input_path.suffix.lower() != ".vm":
            print("Erro: o arquivo de entrada deve ter extensão .vm")
            sys.exit(1)

        output_path = input_path.with_suffix(".asm")
        writer = CodeWriter(output_path)

        translate_file(input_path, writer)

        writer.close()

        print(f"[OK] Arquivo gerado: {output_path}")

    elif input_path.is_dir():

        vm_files = list(input_path.glob("*.vm"))

        if not vm_files:
            print("Erro: nenhum arquivo .vm encontrado no diretório")
            sys.exit(1)

        output_path = input_path / f"{input_path.name}.asm"

        writer = CodeWriter(output_path)

        writer.write_init()

        for vm_file in vm_files:
            translate_file(vm_file, writer)

        writer.close()

        print(f"[OK] Arquivo gerado: {output_path}")


def main():

    if len(sys.argv) != 2:
        print("Uso: python src/main.py <arquivo.vm | diretorio>")
        sys.exit(1)

    translate(sys.argv[1])


if __name__ == "__main__":
    main()