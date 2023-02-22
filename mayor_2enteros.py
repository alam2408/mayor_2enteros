# Pedir al usuario que ingrese dos enteros
num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo entero: "))

# Comparar los dos enteros y mostrar el mayor
if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}.")
else:
    print("Los dos enteros son iguales.")
