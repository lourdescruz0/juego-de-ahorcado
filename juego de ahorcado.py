import tkinter as tk
import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "desarrollador", "juego", "computadora"]

def dibujar_muñeco(intentos_restantes):
    canvas.delete("all")
    # Coordenadas del soporte
    canvas.create_line(50, 200, 150, 200, fill="black", width=2)  # Base
    canvas.create_line(100, 50, 100, 200, fill="black", width=2)  # Poste
    canvas.create_line(100, 50, 150, 50, fill="black", width=2)  # Techo
    canvas.create_line(150, 50, 150, 75, fill="black", width=2)  # Soporte
    if intentos_restantes < 6:
        canvas.create_oval(135, 75, 165, 105, outline="black", width=2)  # Cabeza
    if intentos_restantes < 5:
        canvas.create_line(150, 105, 150, 150, fill="black", width=2)  # Cuerpo
    if intentos_restantes < 4:
        canvas.create_line(150, 120, 130, 140, fill="black", width=2)  # Brazo izquierdo
    if intentos_restantes < 3:
        canvas.create_line(150, 120, 170, 140, fill="black", width=2)  # Brazo derecho
    if intentos_restantes < 2:
        canvas.create_line(150, 150, 130, 180, fill="black", width=2)  # Pierna izquierda
    if intentos_restantes < 1:
        canvas.create_line(150, 150, 170, 180, fill="black", width=2)  # Pierna derecha

def actualizar_estado():
    estado = " ".join(palabra_oculta)
    estado_label.config(text=estado)
    intentos_label.config(text=f"Intentos restantes: {intentos}")
    letras_label.config(text=f"Letras adivinadas: {', '.join(letras_adivinadas)}")

def procesar_adivinanza():
    letra = entrada_letra.get().lower()
    
    if len(letra) != 1 or not letra.isalpha():
        resultado_label.config(text="Por favor, ingresa una sola letra.")
        return
    
    if letra in letras_adivinadas:
        resultado_label.config(text="Ya has adivinado esa letra.")
        return
    
    letras_adivinadas.append(letra)
    
    if letra in palabra:
        for index, char in enumerate(palabra):
            if char == letra:
                palabra_oculta[index] = letra
    else:
        global intentos
        intentos -= 1
        resultado_label.config(text="¡Esa letra no está en la palabra!")
    
    verificar_estado()

def procesar_adivinanza_completa():
    adivinanza = entrada_palabra.get().lower()
    
    if adivinanza == palabra:
        global palabra_oculta
        palabra_oculta = list(palabra)  # Completar la palabra oculta
        resultado_label.config(text="¡Felicidades, has ganado!")
        canvas.config(bg="green")
    else:
        global intentos
        intentos -= 1
        resultado_label.config(text=f"¡Esa no es la palabra! Te quedan {intentos} intentos.")
    
    verificar_estado()

def verificar_estado():
    if "_" not in palabra_oculta:
        if resultado_label.cget("text") == "":
            resultado_label.config(text="¡Felicidades, has ganado!")
            canvas.config(bg="green")
        desactivar_entradas()
    elif intentos <= 0:
        resultado_label.config(text=f"Perdiste. La palabra era '{palabra}'.")
        desactivar_entradas()
    
    dibujar_muñeco(intentos)
    actualizar_estado()

def desactivar_entradas():
    entrada_letra.config(state=tk.DISABLED)
    entrada_palabra.config(state=tk.DISABLED)

def reiniciar_juego():
    global palabra, palabra_oculta, intentos, letras_adivinadas
    palabra = random.choice(palabras)
    palabra_oculta = ["_" for _ in palabra]
    intentos = 6
    letras_adivinadas = []
    entrada_letra.config(state=tk.NORMAL)
    entrada_palabra.config(state=tk.NORMAL)
    entrada_letra.delete(0, tk.END)
    entrada_palabra.delete(0, tk.END)
    resultado_label.config(text="")
    canvas.config(bg="white")
    dibujar_muñeco(intentos)
    actualizar_estado()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")

# Crear canvas para dibujar el muñeco
canvas = tk.Canvas(ventana, width=200, height=250, bg="white")
canvas.pack(pady=10)

# Crear y organizar los elementos de la interfaz
estado_label = tk.Label(ventana, text="", font=("Helvetica", 16))
estado_label.pack(pady=5)

intentos_label = tk.Label(ventana, text="", font=("Helvetica", 12))
intentos_label.pack(pady=5)

letras_label = tk.Label(ventana, text="", font=("Helvetica", 12))
letras_label.pack(pady=5)

entrada_letra = tk.Entry(ventana, font=("Helvetica", 14))
entrada_letra.pack(pady=5)

entrada_palabra = tk.Entry(ventana, font=("Helvetica", 14))
entrada_palabra.pack(pady=5)

resultado_label = tk.Label(ventana, text="", font=("Helvetica", 14))
resultado_label.pack(pady=5)

adivinanza_button = tk.Button(ventana, text="Adivinar letra", command=procesar_adivinanza)
adivinanza_button.pack(pady=5)

adivinanza_completa_button = tk.Button(ventana, text="Adivinar palabra", command=procesar_adivinanza_completa)
adivinanza_completa_button.pack(pady=5)

reiniciar_button = tk.Button(ventana, text="Reiniciar juego", command=reiniciar_juego)
reiniciar_button.pack(pady=5)

# Inicializar el juego
reiniciar_juego()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
