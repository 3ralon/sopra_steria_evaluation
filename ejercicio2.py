"""
Escriba un algoritmo que visualice una clasificación de 50 personas según 
edad y sexo. Deberá mostrar los siguientes resultados:
    a.	Cantidad de personas mayores de edad (18 años o más).
    b.	Cantidad de personas menores de edad.
    c.	Cantidad de personas masculinas mayores de edad.
    d.	Cantidad de personas femeninas menores de edad.
    e.	Porcentaje que representan las personas mayores de edad respecto al 
        total de personas.
    f.	Porcentaje que representan las mujeres respecto al total de personas.

Utilice la instrucción LEER PERSONAS al inicio del programa para cargar los 
datos de las 50 personas en un variable, PERSONAS, que actúa como un vector de 
50 posiciones. Cada elemento de PERSONAS es de un tipo estructurado que dispone 
dos campos: SEXO y EDAD.
"""

class Persona():
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

def LEER_PERSONAS(file=None):
    personas = []
    if not file:
        # input case
        for i in range(50):
            print(f"Datos persona {i+1}:")
            sexo = input(f"- sexo (M/F): ")
            edad = int(input("- edad: "))
            print()
            personas.append(Persona(sexo, edad))
    else:
        # csv file case
        with open(file, 'r') as f:
            next(f) # skip header
            for line in f:
                sexo, edad = line.split(',')
                personas.append(Persona(sexo.strip(), int(edad.strip())))
    return personas

def mayores_de_edad(personas):
    return [persona for persona in personas if persona.edad >= 18]

def menores_de_edad(personas):
    return [persona for persona in personas if persona.edad < 18]

def masculinos_mayores_de_edad(personas):
    return [persona for persona in mayores_de_edad(personas) if persona.sexo == 'M']

def femeninos_menores_de_edad(personas):
    return [persona for persona in menores_de_edad(personas) if persona.sexo == 'F']

def porcentaje_mayores_de_edad(personas):
    return len(mayores_de_edad(personas)) / len(personas) * 100

def porcentaje_mujeres(personas):
    return len([persona for persona in personas if persona.sexo == 'F']) / len(personas) * 100

def main():
    file = input("Ingrese el nombre del archivo csv con los datos de las personas (deje vacío para ingresarlos manualmente): ")
    if file:
        PERSONAS = LEER_PERSONAS(file)
    else:
        PERSONAS = LEER_PERSONAS()
    print(f"Cantidad de personas mayores de edad: {len(mayores_de_edad(PERSONAS))}")
    print(f"Cantidad de personas menores de edad: {len(menores_de_edad(PERSONAS))}", )
    print(f"Cantidad de personas masculinas mayores de edad: {len(masculinos_mayores_de_edad(PERSONAS))}")
    print(f"Cantidad de personas femeninas menores de edad: {len(femeninos_menores_de_edad(PERSONAS))}")
    print(f"Porcentaje que representan las personas mayores de edad respecto al total de personas: {round(porcentaje_mayores_de_edad(PERSONAS), 2)}%")
    print(f"Porcentaje que representan las mujeres respecto al total de personas: {round(porcentaje_mujeres(PERSONAS), 2)}%")

if __name__ == '__main__':
    import sys
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
        sys.exit(0)
