print("=======================================================")
print("======================{ CALCULADORA }==================")
print("=======================================================")

cut = "not"
number = 0
total = 0
operacion_pendiente = "nada"

while cut == "not":
    number = int(input("Enter a number:"))
    print(total)
    operacion_pendiente = input("Enter a symbol:")

    simbolo = operacion_pendiente

    if operacion_pendiente == "+":
        total = total + number
        operacion_pendiente = "+"

    elif simbolo == "=":
        print("resultado", total)
        cut = "yes"

    print(total)

