import Imprimir
import Productos



print(' 1- Compra de productos varios\n', '2- imprimir imagen\n')
select = int(input("Elige una opcion: "))
if select == 1:
    Productos.Contador()

if select == 2:
    print(' 1- Batman\n', '2- Spider-Man\n')
    meme = int(input("Elige una opcion: "))
    if meme == 1:
        Imprimir.batman()
    elif meme == 2:
        Imprimir.spiderman()

