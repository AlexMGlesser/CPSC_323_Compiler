from pdb import run
import sys
from pathlib import Path

had_error = False

def usage():
    print("Usage: lox [script]")
    sys.exit(64)

def runPrompt():
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        run(line)

def runFile(path):
    text = Path(path).read_text(encoding=None)
    run(text)

def run(source):
    scanner = Scanner(source)
    tokens = scanner.scanTokens()

    for token in tokens:
        print(token)


def error(line, message):
    report(line, "", message)

def report(line, where, message):
    global had_error
    print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
    had_error = True

def main():
    if __name__ == "__main__":
        if len(sys.argv) > 1:
            usage()
        elif len(sys.argv) == 1:
            runFile(sys.argv[0])
        else:
            runPrompt()
