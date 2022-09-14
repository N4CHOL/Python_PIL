



class perro:

    #atributos clase global
    especie = "mamifero"

    def __init__(self, nombre, raza):
        #atributos
      self.nombre = nombre
      self.raza = raza

    def ladrar(self):
        print('guau cfk guau')

    def jugar (self, objeto):
        print('el perro esta jugando con ',objeto)

    def saludar (self):
        print('Guau, ni nombre es ',self.nombre)




perro_1 = perro("res",'collie')
print(f'Perro_1-> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}')
perro_1.jugar("pelota")
perro_1.ladrar()
perro_1.saludar()