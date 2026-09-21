import sys
import platform

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "stranger"
    print(f"Hello, {name}!")
    print(f"Hello, {name}!")
    print(f"Python version: {sys.version}")
    print(f"Running on: {platform.system()}")

if __name__ == "__main__":
    main()
