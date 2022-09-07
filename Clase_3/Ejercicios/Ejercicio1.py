monto = 0
print(" 1-Deposito \n 2-Extraccion \n 3-Transferencia \n 4-Salir")
choice = int(input("Elige una opcion: "))
if choice == 4:
    
  print("bye")

while choice != 4:
    if choice == 1:
        print("Deposito") 
        monto(int(input("Introduce un monto:")))
        continue
    elif choice == 2:
        print("Extraccion")
        monto(int(input("Introduce un monto:")))
    elif choice == 3:
        print("Extraccion")
        monto(int(input("Introduce un monto:")))
    elif choice == 4:
        print("bye")
    choice = int(input("Elige una opcion: "))
    print(" 1-Deposito \n 2-Extraccion \n 3-Transferencia \n 4-Salir")
