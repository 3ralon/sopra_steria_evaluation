"""
Desarrolle un algoritmo para el cálculo del salario de un trabajador. 
El importe liquidado (sueldo) depende de una tarifa o precio por hora 
establecida y de un condicionante sobre las horas trabajadas: si la cantidad 
de horas trabajadas es mayor a 40 horas, la tarifa se incrementa en un 
50% para las horas extras. 

Calcular el sueldo recibido por el trabajador 
en base las horas trabajadas y la tarifa. Utilice las instrucciones 
LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para cargar los 
valores en las variables HORASTRABAJADAS y TARIFA.
"""

def LEER_HORASTRABAJADAS():
    return int(input("Ingrese la cantidad de horas trabajadas: "))

def LEER_TARIFA():
    return float(input("Ingrese la tarifa por hora: "))

def calcular_sueldo(horas_trabajadas, tarifa):
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        return tarifa * (40 + horas_extras*1.5)
    return horas_trabajadas * tarifa

def main():
    HORAS_TRABAJADAS = LEER_HORASTRABAJADAS()
    TARIFA = LEER_TARIFA()
    print(f"El sueldo del trabajador es: {calcular_sueldo(HORAS_TRABAJADAS, TARIFA)}")
    
if __name__ == "__main__":
    import sys
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
        sys.exit(0)