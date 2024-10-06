import random
from abc import ABC, abstractmethod

class Clima:
    def __init__(self):
        self.condiciones = ["Soleado", "Lluvioso", "Nublado", "Tormentoso"]
        self.temperatura = 20
        self.actualizar()

    def actualizar(self):
        self.condicion_actual = random.choice(self.condiciones)
        self.temperatura += random.randint(-5, 5)
        self.temperatura = max(min(self.temperatura, 40), 0)

    def __str__(self):
        return f"Clima: {self.condicion_actual}, Temperatura: {self.temperatura}°C"

class Animal(ABC):
    def __init__(self, edad, peso, raza):
        self.edad = edad
        self.peso = peso
        self.raza = raza
        self.salud = "buena"
        self.estado_animo = "feliz"
        self.energia = 100
        self.hambre = 0

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def producir(self):
        pass

    def comer(self):
        self.peso += 0.5
        self.energia += 10
        self.hambre -= 20
        print(f"{self.__class__.__name__} ha comido.")

    def beber(self):
        self.hambre -= 5
        print(f"{self.__class__.__name__} ha bebido agua.")

    def dormir(self):
        self.energia = min(100, self.energia + 30)
        print(f"{self.__class__.__name__} ha dormido y recuperado energía.")

    def enfermar(self):
        if random.random() < 0.1:
            self.salud = "mala"
            print(f"{self.__class__.__name__} se ha enfermado.")

    def tratar(self):
        if self.salud == "mala":
            self.salud = "buena"
            print(f"{self.__class__.__name__} ha sido tratado y está mejor.")

    def afectar_por_clima(self, clima):
        if clima.condicion_actual == "Lluvioso":
            self.estado_animo = "triste"
        elif clima.condicion_actual == "Soleado":
            self.estado_animo = "feliz"
        elif clima.condicion_actual == "Tormentoso":
            self.salud = "mala"
        
        if clima.temperatura > 30:
            self.energia -= 10
        elif clima.temperatura < 10:
            self.hambre += 10

class Vaca(Animal):
    def hacer_sonido(self):
        return "La vaca muge: ¡Muuu!"

    def producir(self):
        return random.randint(20, 30) if self.salud != "mala" else 0

class Gallina(Animal):
    def hacer_sonido(self):
        return "La gallina cacarea: ¡Coc-coc-coc!"

    def producir(self):
        return random.randint(1, 3) if self.salud != "mala" else 0

class Oveja(Animal):
    def hacer_sonido(self):
        return "La oveja bala: ¡Beee!"

    def producir(self):
        return random.randint(2, 5) if self.salud != "mala" else 0

class Caballo(Animal):
    def hacer_sonido(self):
        return "El caballo relincha: ¡Hiiii!"

    def producir(self):
        return "Montar" if self.salud != "mala" else "No disponible"

class Cerdo(Animal):
    def hacer_sonido(self):
        return "El cerdo gruñe: ¡Oink oink!"

    def producir(self):
        return self.peso * 0.6 if self.salud != "mala" else 0

class Granja:
    def __init__(self):
        self.animales = []
        self.clima = Clima()

    def agregar_animal(self, animal):
        self.animales.append(animal)
        print(f"Se ha agregado un {animal.__class__.__name__} a la granja.")

    def alimentar_animales(self):
        for animal in self.animales:
            animal.comer()

    def recolectar_productos(self):
        productos = {}
        for animal in self.animales:
            producto = animal.producir()
            if producto:
                tipo = animal.__class__.__name__
                if tipo not in productos:
                    productos[tipo] = 0
                productos[tipo] += producto
        return productos

    def tratar_enfermos(self):
        for animal in self.animales:
            if animal.salud == "mala":
                animal.tratar()

    def mostrar_informacion(self):
        for animal in self.animales:
            print(f"\nTipo: {animal.__class__.__name__}")
            print(f"Edad: {animal.edad}")
            print(f"Peso: {animal.peso}")
            print(f"Raza: {animal.raza}")
            print(f"Salud: {animal.salud}")
            print(f"Estado de ánimo: {animal.estado_animo}")
            print(f"Nivel de energía: {animal.energia}")
            print(f"Nivel de hambre: {animal.hambre}")

    def interacciones_animales(self):
        if len(self.animales) > 1:
            animal1, animal2 = random.sample(self.animales, 2)
            if isinstance(animal1, Caballo) and isinstance(animal2, Oveja):
                print(f"El caballo está protegiendo a la oveja.")
                animal2.estado_animo = "feliz"
            elif isinstance(animal1, Vaca) and isinstance(animal2, Gallina):
                print(f"La vaca y la gallina están pastando juntas.")
                animal1.energia += 5
                animal2.energia += 5
            else:
                print(f"{animal1.__class__.__name__} y {animal2.__class__.__name__} están jugando juntos.")
                animal1.estado_animo = "feliz"
                animal2.estado_animo = "feliz"

    def simular_dia(self):
        print("\n--- Simulación de un día en la granja ---")
        self.clima.actualizar()
        print(self.clima)
        self.alimentar_animales()
        for animal in self.animales:
            animal.beber()
            animal.dormir()
            animal.enfermar()
            animal.afectar_por_clima(self.clima)
        self.interacciones_animales()
        productos = self.recolectar_productos()
        print("\nProductos recolectados:")
        for tipo, cantidad in productos.items():
            print(f"{tipo}: {cantidad}")
        self.tratar_enfermos()

def menu_principal():
    granja = Granja()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar animal")
        print("2. Mostrar información de los animales")
        print("3. Simular un día")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de animal (Vaca/Gallina/Oveja/Caballo/Cerdo): ")
            edad = int(input("Edad en años : "))
            peso = float(input("Peso en kg: "))
            raza = input("Raza: ")
            if tipo.lower() == "vaca":
                granja.agregar_animal(Vaca(edad, peso, raza))
            elif tipo.lower() == "gallina":
                granja.agregar_animal(Gallina(edad, peso, raza))
            elif tipo.lower() == "oveja":
                granja.agregar_animal(Oveja(edad, peso, raza))
            elif tipo.lower() == "caballo":
                granja.agregar_animal(Caballo(edad, peso, raza))
            elif tipo.lower() == "cerdo":
                granja.agregar_animal(Cerdo(edad, peso, raza))
            else:
                print("Tipo de animal no reconocido.")
        elif opcion == "2":
            granja.mostrar_informacion()
        elif opcion == "3":
            granja.simular_dia()
        elif opcion == "4":
            print("Gracias por usar el simulador de granja. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()