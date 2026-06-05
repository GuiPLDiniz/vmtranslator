import subprocess
from pathlib import Path


TESTS = [
    "tests/projects07/StackArithmetic/SimpleAdd/SimpleAdd.vm",
    "tests/projects07/StackArithmetic/StackTest/StackTest.vm",
    "tests/projects07/MemoryAccess/BasicTest/BasicTest.vm",
    "tests/projects07/MemoryAccess/PointerTest/PointerTest.vm",
    "tests/projects07/MemoryAccess/StaticTest/StaticTest.vm",
]


for test in TESTS:

    print(f"Testando: {test}")

    result = subprocess.run(
        ["python", "src/main.py", test],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("[OK]\n")

    else:
        print("[FALHOU]")
        print(result.stderr)