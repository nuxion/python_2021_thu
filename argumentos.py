import sys

def saludar(saludo):
    print(saludo)


if __name__ == "__main__":
    args  = sys.argv
    if len(args) == 3:
        if args[1] == "--saludar":
            saludar(args[2])
    else:
        print("No tengo nada para hacer")

