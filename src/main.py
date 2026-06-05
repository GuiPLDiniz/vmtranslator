from parser import Parser
from code_writer import CodeWriter


def main():

    parser = Parser("tests/Simple.vm")

    writer = CodeWriter("tests/Simple.asm")

    while parser.has_more_commands():

        parser.advance()

        command_type = parser.command_type()

        if command_type == "C_PUSH":

            writer.write_push(
                parser.arg1(),
                parser.arg2()
            )

        elif command_type == "C_POP":

            writer.write_pop(
                parser.arg1(),
                parser.arg2()
            )

        elif command_type == "C_ARITHMETIC":

            writer.write_arithmetic(
                parser.arg1()
            )

    writer.close()


if __name__ == "__main__":
    main()