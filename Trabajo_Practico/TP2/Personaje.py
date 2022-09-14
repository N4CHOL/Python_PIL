
# generate random integer values
from random import randint
import Imprimir


class personaje:

    def __init__(self, nombre, raza, nivel, str,dex,int,cha):
        # atributos
        self.nombre = nombre
        self.raza = raza
        self.nivel = nivel
        self.fuerza = str
        self.destreza = dex
        self.inteligencia = int
        self.carisma = cha
        self.defenza = 14
    def atacar(self):
        atk = randint(0, 20)
        return atk



print('Creador de personaje')
Name = str(input('Nombre de Personaje: '))

print(' 1-Humano \n', '2-Elfo\n', '3-Semi Elfo\n', '4-Semi Orco\n')
rselect = int(input('Elegir Raza: '))
if rselect == 1:
    race = 'Humano'
elif rselect == 2:
    race = 'Elfo'
elif rselect == 3:
    race = 'Semi Elfo'
elif rselect == 4:
    race = 'Semi Orco'


lvl = int(input('Nivel de comienzo: '))


print('Estadisticas:')
str = randint(3, 20)
dex = randint(3, 20)
int = randint(3, 20)
cha = randint(3, 20)



print(" Fuerza: ",str, "\n","Destreza: ",dex, "\n","Inteligencia: ",int, "\n","Sabiduria: ",cha, "\n","\n")

personaje_1 = personaje(Name,race,lvl,str,dex,int,cha)

print("Comienza la Aventura!","\n","\n")

print("Te encontrabas recostado contra el tronco de un viejo árbol, antes de que pudieras dormirte una siesta un grito desgarrador te llamó poderosamente la atención","\n")

print(f"'{personaje_1.nombre}! Ayuda por favor!'\n")

print(' 1-Voy corriendo a ayudar \n', '2-Me duermo una siesta, que se las arregle\n', '3-Me voy al bar, aca no paso nada\n', '4-Espero un rato voy cuando sea seguro\n')
choice1 = (input('Que haces?: '))

if choice1 == "1":
    print("Corriste desesperadamente en la dirección de los gritos, al llegar al lugar te encuentras con la imagen de tu compañero de equipo Jose peleando con un goblin\n")

    print(f"'{personaje_1.nombre} dame una mano con el monstruo'   tu amigo te pide ayuda\n")
    print(f"'{personaje_1.raza} Si te das la vuelta te dejo vivir!' El Goblin te habla, su daga está ensangrentada\n")

    print(' 1-Ayudo a Jose \n', '2-Me voy al bar, aca no paso nada\n', '3-Jose me cae re mal, ayudo al goblin\n')
    choice12 = (input('Que haces?: '))

    if choice12 == "1":
        atk = 0
        while atk < 12:
            atk = personaje_1.atacar()
            if atk  <= 12:
                print("Mi ataque fallo") 
            else:
                print("Junto a Jose lograste derrotar al goblin y los dos se fueron al bar")
    if choice12 == "2":
        print(f"'{personaje_1.nombre} no me abandones!,{personaje_1.raza} traidor!'\n Abandonaste a Jose a su suerte...")
    
    if choice12 == "3":
        print("Decidiste unirte al goblin\n 1-Le tiro una piedra a Jose \n 2-Le lanzo a Jose uno de mis cuchillos")
        choice123 = (input('Que haces?: '))
        if choice123 =="1":
            print("Encontras una roca enorme y decidis tirarsela a Jose")
            if personaje_1.fuerza <= 12:
                print("Intentas levantarla pero tu fuerza no es suficiente... \n Te tardaste mucho y Jose los mato a los dos")
            else:
                print("Con tu gran fuerza logras levantar la piedra sin problemas y arrojarsela a Jose en la cabeza... \n Vos y el goblin se fueron al bar con la plata de Jose")
        if choice123 =="2":
            print("Recuerdas que llevas varios cuchillos colgados en tu cinturón y le lanzas uno a Jose")
            if personaje_1.destreza <= 12:
                print("Tu destreza no es suficiente y tu lanzamiento falla miserablemente... \n Te tardaste mucho y Jose los mato a los dos")
            else:
                print("Con mucha destreza logras un lanzamiento perfecto... \n Vos y el goblin se fueron al bar con la plata de Jose")



elif choice1 == "2":
    print("Tu aventura termina antes de que pueda comenzar, durante tu siesta alguien te asesina")

elif choice1 == "3":
    print("Despues de varios tragos el barman te dice que pagues por que va a cerrar\n 1-Le pagas pero te quedas sin plata \n 2-'Si crees en dios entoces que te page el'\n 3- Tratas de convencerlo de que te fie \n 4-Le haces un dibujito de Batman" )
    choice32 = (input('Que haces?: '))
    if choice32 == "1":
        print("Te volviste a casa caminando y sin sueldo...")
    if choice32 == "2":
        print("El barman no se toma muy bien, te ataca y una batalla legendaria comienza...")
        atk = 0
        while atk < 12:
            atk = personaje_1.atacar()
            if atk  <= 12:
                print("Los litros de alcohol que llevas encima no te dejan pelear, el Barman te derrota y se lleva tu sueldo") 
            else:
                print("Le ganaste al Barman, te fuiste a casa en remis y pediste un lomito")
    if choice32 == "3":
        if personaje_1.carisma <= 12:
            print("Tu carisma no es suficiente, las palabras no salen como las piensas y terminas pagando")
        else:
            print("De alguna manera tu gran carisma consigue convencer al enojado barman y logras irte sin pagar")
    
    if choice32 == "4":
        Imprimir.batman()

elif choice1 == "4":
    print("Cuando los gritos y sonidos de batalla se detienen te acercas a ver que pasó \n Econtras el cuerpo de Jose, tu amigo\n \n 1-Sepulto su cuerpo \n 2-Me llevo la bolsa de oro")
    choice42 = (input('Que haces?: '))
    if choice42 == "1":
        print("Despues de un funeral improvisado te volves a tu casa, sad")
    if choice42 == "2":
        print("Lejos de desaprovechar una buena oportunidad, recordas que Jose habia cobrado hace poco, despues de una corta investigacion \n encontras una bolsa de oro, te vas al bar")