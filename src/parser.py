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

        if parts[0] == "push":
            return "C_PUSH"

        if parts[0] == "pop":
            return "C_POP"

        if parts[0] in self.ARITHMETIC_COMMANDS:
            return "C_ARITHMETIC"

        raise ValueError(f"Comando desconhecido: {self.current_command}")

    def arg1(self):

        if self.command_type() == "C_ARITHMETIC":
            return self.current_command.split()[0]

        return self.current_command.split()[1]

    def arg2(self):

        return int(self.current_command.split()[2])