a = "EsTo Es uN sTrIng"

largo = len(a)
#Indice un elemento
print(a[0])
#Indice rango de elementos
print(a[0:4])
#  Incide negativo
print(a[-1])
#  Incide complto
print(a[0:largo])


#Metodos

#   Mayusculas
print(a.upper())
#   Minusculas
print(a.lower())

#   Split
print(a.split())


#ARRAY

lista_1 = [1,2,3,4,5,6]
print(lista_1)
#APPEND

print(lista_1.append(7))



# Diccionario

d1 = {
    'nombre': 'octavio',
    'apellido':'Oto',
    'edad': 38,
    'hobbies': ['anime','juego anal'],
    'mascotas': 'no tiene' 
}

print(d1)


# Metodos

print(d1.get('puesto','no encontrado'))

keys= list(d1.keys())