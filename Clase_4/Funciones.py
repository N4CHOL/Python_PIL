#   Una funcion es un bloque de codigo reutilizable

#   Nombre
#   Argumento
#   Retorno


#   Funcion 1
def suma_de_dos(a, b):

    resultado = a + b

    return resultado


#   Funcion 2
def saludo(cantidad_saludos):
    lista_nombres = []
    for i in range(cantidad_saludos):
        nombre = input('ingrese su nombre: ')
        print('hola', nombre)
        lista_nombres.append(nombre)
    print(lista_nombres)
    return lista_nombres


nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar')))

#   Funcion 3


def orden(Lista, sentido):
    Lista.sort(reverse=sentido)
    return Lista


print(
    orden(nombres, False)
)
