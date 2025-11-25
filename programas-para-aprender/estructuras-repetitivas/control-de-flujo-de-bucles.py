"""
CONTROLES DE FLUJO EN BUCLES – PYTHON
------------------------------------
Este documento complementa el estudio de estructuras repetitivas explicando cómo
modificar o controlar la ejecución de los bucles mediante las sentencias:
- break
- continue
- pass
- else en bucles

Es un documento pensado para estudio y práctica.

------------------------------------
1. INSTRUCCIÓN BREAK
------------------------------------
`break` se usa para **detener el bucle por completo**, sin importar si la condición
se siguió cumpliendo o si el for tenía más elementos.

Es útil cuando:
- se encuentra lo que se buscaba
- hay que interrumpir el ciclo por una condición especial
- se quiere salir del bucle antes de tiempo
"""

# Ejemplo: detener al encontrar un número negativo
numeros = [5, 8, 3, -2, 7]

for n in numeros:
    if n < 0:
        print(f"Número negativo encontrado: {n}. Saliendo del bucle.")
        break
    print(f"Número válido: {n}")

"""
------------------------------------
2. INSTRUCCIÓN CONTINUE
------------------------------------
`continue` NO detiene el bucle.
Lo que hace es **saltar la iteración actual** y pasar directamente a la siguiente.

Es útil para:
- saltar valores no deseados
- ignorar entradas inválidas
- omitir pasos según condiciones específicas
"""

# Ejemplo: imprimir solo números pares
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"Número par: {i}")

"""
------------------------------------
3. INSTRUCCIÓN PASS
------------------------------------
`pass` no hace nada.
Se utiliza como marcador cuando se necesita escribir algo sintácticamente, pero aún
no se ha decidido qué va a ir allí.

Útil para:
- dejar funciones vacías
- dejar bucles vacíos
- escribir código temporal que se completará después
"""

# Ejemplo: estructura pendiente
for i in range(5):
    pass  # Aquí se implementará lógica más adelante

"""
------------------------------------
4. ELSE EN BUCLES
------------------------------------
Poco conocido pero muy útil.
Tanto `for` como `while` pueden tener un `else`.

El `else` se ejecuta **solo si el bucle NO fue interrumpido con break**.

Sirve para:
- verificar búsquedas completas
- ejecutar un mensaje final limpio
- distinguir entre "encontré" / "no encontré"
"""

# Ejemplo: búsqueda en lista con else
lista = [4, 7, 9, 12]

for num in lista:
    if num == 5:
        print("Número encontrado!")
        break
else:
    print("El número 5 no está en la lista.")

"""
------------------------------------
5. RESUMEN GENERAL
------------------------------------
- break: detiene el bucle.
- continue: salta a la siguiente iteración.
- pass: no hace nada, se usa como marcador.
- else en bucles: se ejecuta si no hubo `break`.
------------------------------------
FIN DEL DOCUMENTO
"""
