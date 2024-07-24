"""
Escriba un algoritmo que lea un número entero y determine si es par o impar. 
Si es par, que escriba todos los pares de manera descendiente desde sí mismo y 
hasta el cero. Si es impar, que escriba todos los impares de manera descendiente 
desde si sí mismo hasta el uno. Utilice la instrucción LEER NUMERO al inicio del 
programa para cargar un número en la variable NUMERO.
"""

def LEER_NUMERO():
    return int(input("Ingrese un número entero: "))

def main():
    NUMERO = LEER_NUMERO()

    if NUMERO % 2 == 0:
        for i in range(NUMERO, -1, -2):
            print(i)
    else:
        for i in range(NUMERO, 0, -2):
            print(i)
            
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