class Parser:

    ARITHMETIC_COMMANDS = {
        "add",
        "sub",
        "neg",
        "eq",
        "gt",
        "lt",
        "and",
        "or",
        "not"
    }

    def __init__(self, filename):

        self.commands = []

        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                line = line.split("//")[0].strip()

                if line:
                    self.commands.append(line)

        self.current_index = -1
        self.current_command = None

    def has_more_commands(self):

        return self.current_index + 1 < len(self.commands)

    def advance(self):

        self.current_index += 1
        self.current_command = self.commands[self.current_index]

    def command_type(self):

        parts = self.current_command.split()
        command = parts[0]

        if command == "push":
            return "C_PUSH"

        if command == "pop":
            return "C_POP"

        if command == "label":
            return "C_LABEL"

        if command == "goto":
            return "C_GOTO"

        if command == "if-goto":
            return "C_IF"

        if command == "function":
            return "C_FUNCTION"

        if command == "call":
            return "C_CALL"

        if command == "return":
            return "C_RETURN"

        if command in self.ARITHMETIC_COMMANDS:
            return "C_ARITHMETIC"

        raise ValueError(f"Comando desconhecido: {self.current_command}")

    def arg1(self):

        command_type = self.command_type()

        if command_type == "C_RETURN":
            raise ValueError("Comando return não possui arg1")

        if command_type == "C_ARITHMETIC":
            return self.current_command.split()[0]

        return self.current_command.split()[1]

    def arg2(self):

        command_type = self.command_type()

        if command_type not in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            raise ValueError(f"Comando {command_type} não possui arg2")

        return int(self.current_command.split()[2])