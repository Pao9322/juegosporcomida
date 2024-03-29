#clase perosnaje
class Personaje():
#constructor  (considera parámetros y valores asignados a atributos de instancia)
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

 # Propiedad para obtener el estado del personaje
    @property
    def estado (self):
        return (
            f"Nombre:{self.nombre}",
            f"Nivel: {self.nivel}",
            f"Experiencia: {self.experiencia}"
        )
    
# Setter para actualizar el estado del personaje con la experiencia ganada o perdida
    @estado.setter 
    def estado(self, exp: int):
        tmp_exp = self.experiencia + exp

# Manejo de nivel al ganar o perder experiencia
        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1
            else:
                tmp_exp = 0

        self.experiencia = tmp_exp

# Método para comparar personajes por nivel (menor que)
    def __lt__(self, other):
        return self.nivel < other.nivel 

# Método para comparar personajes por nivel (mayor que)
    def __gt__(self, other):
        return self.nivel > other.nivel 

# Método para comparar personajes por nivel (igual a)    
    def __eq__(self, other):
        return self.nivel == other.nivel 

# Método para obtener la probabilidad de ganar contra otro personaje    
    def get_probabilidad_ganar(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

# Método estático para mostrar un diálogo de opciones y obtener la elección del usuario
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(input(
            f"\n Con tu nivel actual, tienes {probabilidad_ganar * 100} %"
            "de probabilidades de ganarle al Orco.\n"
            "\n Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\n"
            " Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
            "\n ¿Qué deseas hacer?\n"
            "1. Atacar\n"
            "2. Huir\n"
        )
    )

        