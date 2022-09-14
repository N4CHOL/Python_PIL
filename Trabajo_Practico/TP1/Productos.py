

def Contador():
    cantidad = 0

    cepillo = {
        'nombre': 'cepillo',
        'precio': 250
    }
    escoba = {
        'nombre': 'escoba',
        'precio': 690
    }
    esponja = {
        'nombre': 'esponja',
        'precio': 80
    }
    liquido = {
        'nombre': 'detergente',
        'precio':  cantidad + int(23)
    }
    comida = {
        'nombre': 'Balanceado',
        'precio':  cantidad + int(56)
    }


    total = 0
    x = 0
    cantidad_productos = int(input("Cuantos productos lleva: "))


    while x<cantidad_productos:
        print(' 1-', cepillo.get('nombre'), '\n', '2-', escoba.get('nombre'), '\n', '3-',
            esponja.get('nombre'), '\n', '4-', liquido.get('nombre'), '\n', '5-', comida.get('nombre'), '\n')
        select = int(input("Elige una opcion: "))
        if select == 1:
            total=total + cepillo.get('precio')
        elif select == 2:
            total=total + escoba.get('precio')
            
        x=x+1
        return total
    
    print(total)


