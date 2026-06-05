class CodeWriter:
    SEGMENT_BASE = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT"
    }

    def __init__(self, output_file):

        self.file = open(output_file, "w", encoding="utf-8")

    def write_push(self, segment, index):

        if segment == "constant":

            self.file.write(
    f"""@{index}
D=A
@SP
A=M
M=D
@SP
M=M+1
"""
        )

        elif segment in self.SEGMENT_BASE:

            base = self.SEGMENT_BASE[segment]

            self.file.write(
f"""@{base}
D=M
@{index}
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
"""
        )
    
    def write_pop(self, segment, index):

        if segment in self.SEGMENT_BASE:

            base = self.SEGMENT_BASE[segment]

            self.file.write(
f"""@{base}
D=M
@{index}
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
"""
        )

    def write_arithmetic(self, command):

        if command == "add":

            self.file.write(
"""@SP
AM=M-1
D=M
A=A-1
M=M+D
"""
        )

        elif command == "sub":

            self.file.write(
"""@SP
AM=M-1
D=M
A=A-1
M=M-D
"""
        )

        elif command == "neg":

            self.file.write(
"""@SP
A=M-1
M=-M
"""
        )

        elif command == "and":

            self.file.write(
"""@SP
AM=M-1
D=M
A=A-1
M=M&D
"""
        )

        elif command == "or":

            self.file.write(
"""@SP
AM=M-1
D=M
A=A-1
M=M|D
"""
        )

        elif command == "not":

            self.file.write(
"""@SP
A=M-1
M=!M
"""
        )

    def close(self):

        self.file.close()
    
