word = input("Insertar texto: ")

lengt = len(word)

passw = "*" * lengt
print( word, "*" * lengt)

diccionario = {
    'word': word,
    'pass' : passw
}
print(diccionario)