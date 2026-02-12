import random

# ===== INICIO DEL JUEGO =====
print("=== AVENTURA DEL REINO DIGITAL ===\n")

nombre = input("Ingresa tu nombre de jugador: ")

print("\nElige tu clase:")
print("1. Guerrero ️  (Bonus +10)")
print("2. Mago      (Bonus +5)")
print("3. Arquero     (Bonus +7)")

clase_opcion = input("Selecciona una opción (1-3): ")

if clase_opcion == "1":
    clase = "Guerrero"
    bonus_clase = 10
elif clase_opcion == "2":
    clase = "Mago"
    bonus_clase = 5
elif clase_opcion == "3":
    clase = "Arquero"
    bonus_clase = 7
else:
    clase = "Aventurero"
    bonus_clase = 0

print(f"\nBienvenido {nombre}, eres un {clase}.\n")

inventario = []
total_puntos = 0
jugando = True

# ===== CICLO PRINCIPAL =====
while jugando:
    print("\n¿Qué deseas hacer?")
    print("1. Recolectar objeto")
    print("2. Consultar inventario")
    print("3. Finalizar partida")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        valor = random.randint(1, 100)

        # Evento especial frecuencia (40%)
        evento = random.randint(1, 10)

        if evento <= 4:
            print("\n ¡Evento especial! Encontraste un cofre misterioso ")
            bonus_evento = random.randint(20, 60)
            print(f"El cofre añade +{bonus_evento} puntos extra.")
            valor += bonus_evento

        # Clasificación del objeto
        if valor > 95:
            print(f" ¡OBJETO LEGENDARIO! Valor final: {valor}")
        elif valor > 70:
            print(f"Objeto épico encontrado. Valor final: {valor}")
        elif valor > 40:
            print(f"Objeto común. Valor final: {valor}")
        else:
            print(f"Objeto débil... Valor final: {valor}")

        inventario.append(valor)
        total_puntos += valor

    elif opcion == "2":
        if len(inventario) == 0:
            print("\nTu inventario está vacío.")
        else:
            print("\n===== INVENTARIO =====")
            for i, objeto in enumerate(inventario, 1):
                print(f"Objeto {i}: Valor {objeto}")
            print(f"\nPuntaje acumulado actual: {total_puntos}")

    elif opcion == "3":
        jugando = False

    else:
        print("Opción inválida. Intenta nuevamente.")

# ===== RESULTADOS FINALES =====
total_puntos += bonus_clase

print("\n===== RESULTADOS FINALES =====")
print(f"Jugador: {nombre}")
print(f"Clase: {clase}")
print(f"Objetos recolectados: {len(inventario)}")
print(f"Bonus de clase: {bonus_clase}")
print(f"Puntaje total final: {total_puntos}")

# Sistema de rango final
if total_puntos > 500:
    rango = " Maestro Supremo del Reino"
elif total_puntos > 300:
    rango = "Héroe del Reino"
elif total_puntos > 150:
    rango = "️ Aventurero Experto"
else:
    rango = " Novato del Reino"

print(f"Rango obtenido: {rango}")

print("\nGracias por jugar.")