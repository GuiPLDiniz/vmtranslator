from parser import Parser


def main():

    parser = Parser("tests/Simple.vm")

    while parser.has_more_commands():

        parser.advance()

        print(
            parser.command_type(),
            parser.arg1(),
            end=""
        )

        if parser.command_type() != "C_ARITHMETIC":
            print(f" {parser.arg2()}")

        else:
            print()


if __name__ == "__main__":
    main()