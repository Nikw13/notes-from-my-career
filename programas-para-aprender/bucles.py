"""
ESTRUCTURAS REPETITIVAS EN PYTHON
---------------------------------
Este documento explica todo lo relacionado con los bucles (estructuras repetitivas) en Python,
incluyendo `while`, `for`, bucles con sentinela, bucles con contador y conceptos clave.

Las estructuras repetitivas permiten ejecutar un bloque de código varias veces.
En Python existen principalmente dos tipos de bucles: `while` y `for`.

---------------------------------
1. BUCLE WHILE
---------------------------------
El bucle `while` ejecuta un bloque de código MIENTRAS una condición sea verdadera.
Es ideal para:
- Bucles con sentinela
- Bucles que dependen de una condición dinámica
- Repeticiones donde NO sabemos cuántas veces se ejecutará el ciclo

EJEMPLO 1: BUCLE CON SENTINELA
---------------------------------
Un sentinela es un valor especial que DETIENE el bucle.
"""

# Bucle con sentinela
numero_sentinela = 23
numero_usuario = int(input("Ingrese un número: "))

while numero_usuario != numero_sentinela:
    numero_usuario = int(input("Número incorrecto, ingrese otro número: "))

print("Número correcto!!")

"""
---------------------------------
2. BUCLE CON CONTADOR
---------------------------------
Este tipo de bucle utiliza una variable que se incrementa o decrementa
en cada iteración. Es útil cuando sabemos cuántas veces queremos repetir algo.

IMPORTANTE: Python NO tiene operadores ++ o --.
Para incrementar se usa: contador += 1

También se muestra el uso de f-strings, que permiten insertar variables
dentro de una cadena usando llaves { }.
"""

# Bucle con contador
contador = 0

while contador <= 15:
    print(f"Estoy en la vuelta: {contador}")
    contador += 1

"""
---------------------------------
3. BUCLE FOR
---------------------------------
El bucle `for` recorre elementos de una secuencia:
- rangos de números (range)
- listas
- cadenas

Es ideal cuando sí sabemos cuántas veces queremos repetir algo.

EJEMPLO 1: Recorrer rango simple
---------------------------------
"""

for i in range(5):
    print(i)

"""
EJEMPLO 2: Rango con inicio y fin
---------------------------------
range(1, 6) genera: 1, 2, 3, 4, 5
"""

for i in range(1, 6):
    print(i)

"""
EJEMPLO 3: Rango con saltos
---------------------------------
range(inicio, fin, paso)
"""

for i in range(0, 20, 2):
    print(i)

"""
---------------------------------
4. RESUMEN GENERAL
---------------------------------
- `while`: Repite mientras la condición sea verdadera.
- `for`: Repite por cada elemento de una secuencia.
- Sentinela: valor que detiene un bucle.
- Contador: variable que aumenta o disminuye en cada iteración.
- f-strings: permiten insertar variables dentro de texto.
---------------------------------
FIN DEL DOCUMENTO
"""
