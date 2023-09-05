
from pathlib import Path

def main():
    # function.fun1()
    script_path = Path(__file__).absolute()
    print(script_path)

if __name__ == '__main__':
    main()
