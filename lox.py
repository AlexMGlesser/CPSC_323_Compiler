import sys

def runPrompt():
    print("Usage: python3 lox.py [script]")

def runFile(path):
    with open(path, 'r') as file:
        source = file.read()
        

def main():
    if __name__ == "__main__":
        if len(sys.argv) > 1 or len(sys.argv) == 0:
            runPrompt()
        else:
            runFile(sys.argv[0])

