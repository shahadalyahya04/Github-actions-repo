import sys
import platform

def main():
    name = sys.arfv[1] if len(sys.arfv) > 1 else "Person"
    print("Hello from Python!")
    print(f"Python version: {sys.version}")
    print(f"Running on: {platform.system()}")

if __name__ == "__main__":
    main()
    
