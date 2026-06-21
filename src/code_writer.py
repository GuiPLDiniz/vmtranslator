class CodeWriter:
    SEGMENT_BASE = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT"
    }

    def __init__(self, output_file):

        self.file = open(output_file, "w", encoding="utf-8")
        self.label_count = 0
        self.call_count = 0
        self.current_file = ""

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
        
        elif segment == "temp":

            address = 5 + index

            self.file.write(
f"""@R{address}
D=M
@SP
A=M
M=D
@SP
M=M+1
"""
        )

        elif segment == "pointer":

            if index == 0:
                pointer = "THIS"
            elif index == 1:
                pointer = "THAT"
            else:
                raise ValueError("Segmento pointer aceita apenas índice 0 ou 1")

            self.file.write(
f"""@{pointer}
D=M
@SP
A=M
M=D
@SP
M=M+1
"""
        )

        elif segment == "static":

            self.file.write(
f"""@{self.current_file}.{index}
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
        
        elif segment == "temp":

            address = 5 + index

            self.file.write(
f"""@SP
AM=M-1
D=M
@R{address}
M=D
"""
        )

        elif segment == "pointer":

            if index == 0:
                pointer = "THIS"
            elif index == 1:
                pointer = "THAT"
            else:
                raise ValueError("Segmento pointer aceita apenas índice 0 ou 1")

            self.file.write(
f"""@SP
AM=M-1
D=M
@{pointer}
M=D
"""
        )

        elif segment == "static":

            self.file.write(
f"""@SP
AM=M-1
D=M
@{self.current_file}.{index}
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
        
        elif command == "eq":

            self.write_comparison("JEQ")

        elif command == "gt":

            self.write_comparison("JGT")

        elif command == "lt":

            self.write_comparison("JLT")
            
    def write_comparison(self, jump_command):

        true_label = f"BOOL_TRUE_{self.label_count}"
        end_label = f"BOOL_END_{self.label_count}"
        self.label_count += 1

        self.file.write(
f"""@SP
AM=M-1
D=M
A=A-1
D=M-D
@{true_label}
D;{jump_command}
@SP
A=M-1
M=0
@{end_label}
0;JMP
({true_label})
@SP
A=M-1
M=-1
({end_label})
"""
    )
    
    def write_label(self, label):

            self.file.write(
            f"""({label})
            """
                    )

    def write_goto(self, label):

            self.file.write(
            f"""@{label}
            0;JMP
            """
                    )

    def write_if(self, label):

            self.file.write(
f"""@SP
AM=M-1
D=M
@{label}
D;JNE
"""
        )
            
    def write_function(self, function_name, n_vars):

        self.file.write(
f"""({function_name})
"""
        )

        for _ in range(n_vars):

            self.file.write(
"""@0
D=A
@SP
A=M
M=D
@SP
M=M+1
"""
            )
    
    def write_return(self):

        self.file.write(
"""@LCL
D=M
@R13
M=D

@5
A=D-A
D=M
@R14
M=D

@SP
AM=M-1
D=M
@ARG
A=M
M=D

@ARG
D=M+1
@SP
M=D

@R13
AM=M-1
D=M
@THAT
M=D

@R13
AM=M-1
D=M
@THIS
M=D

@R13
AM=M-1
D=M
@ARG
M=D

@R13
AM=M-1
D=M
@LCL
M=D

@R14
A=M
0;JMP
"""
        )

    def write_call(self, function_name, n_args):

        return_label = f"RETURN_{self.call_count}"
        self.call_count += 1

        self.file.write(
f"""@{return_label}
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@{n_args + 5}
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@{function_name}
0;JMP

({return_label})
"""
    )
        
    def write_init(self):

            self.file.write(
"""@256
D=A
@SP
M=D
"""
        )

            self.write_call("Sys.init", 0)

    def set_file_name(self, file_path):

        from pathlib import Path

        self.current_file = Path(file_path).stem

    def close(self):

        self.file.close()
    
