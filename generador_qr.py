import tkinter as tk
from tkinter import messagebox
import qrcode
import os
from tkinter import PhotoImage

def generar_qr():
    enlace = entrada_url.get().strip()
    if not enlace:
        messagebox.showerror("Error", "Por favor, introduce un enlace o texto válido.")
        return

    try:
        # Configuración del código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2, # Borde más fino para el código
        )
        qr.add_data(enlace)
        qr.make(fit=True)

        # Usamos colores más vivos para el QR (negro sobre blanco es más estándar)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Guardado en el Escritorio
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        ruta_salida = os.path.join(ruta_escritorio, "codigo_qr_generado.png")
        img.save(ruta_salida)
        
        etiqueta_estado.config(text="¡Código QR creado en tu Escritorio!", fg="#2ecc71") # Color verde neón
        messagebox.showinfo("¡Éxito!", f"Código QR guardado en:\n{ruta_salida}")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el QR:\n{e}")

# Ventana principal - Estilo Moderno
ventana = tk.Tk()
ventana.title("Generador Rápido de QR")
ventana.geometry("500x420")
ventana.resizable(False, False) # Evitamos que cambien el tamaño para mantener el diseño

# Colores de la interfaz (Fondo oscuro y acentos)
color_fondo = "#1a1a2e" # Azul muy oscuro
color_texto = "#e6e6e6" # Blanco suave
color_acento_azul = "#00adb5" # Cian brillante
color_acento_verde = "#2ecc71" # Verde neón (para estado)
color_entrada = "#393e46" # Gris oscuro para entradas

ventana.config(bg=color_fondo)

# Título Principal - Moderno y Grande
titulo = tk.Label(ventana, text="Generador de Códigos QR", font=("Arial", 16, "bold"), fg=color_acento_azul, bg=color_fondo)
titulo.pack(pady=30)

# Marco para la entrada y la instrucción (agrupado)
frame_entrada = tk.Frame(ventana, bg=color_fondo)
frame_entrada.pack(pady=10)

label_instruccion = tk.Label(frame_entrada, text="Pega tu enlace (Instagram, Facebook, Web...):", font=("Arial", 11), fg=color_texto, bg=color_fondo)
label_instruccion.pack(pady=5)

# Cuadro de entrada estilizado
entrada_url = tk.Entry(frame_entrada, font=("Arial", 12), width=45, fg="white", bg=color_entrada, relief="flat", insertbackground="white")
entrada_url.pack(pady=10)
entrada_url.insert(0, "https://www.instagram.com/")
entrada_url.focus_set() # Pone el cursor ahí

# Botón - Estilizado y Moderno con bordes redondeados (Tkinter flat)
boton_generar = tk.Button(ventana, text="> GENERAR QR <", font=("Arial", 12, "bold"), fg="white", bg=color_acento_azul, relief="flat", padx=30, pady=12, command=generar_qr)
boton_generar.pack(pady=25)

# Etiqueta de estado (oculta hasta generar)
etiqueta_estado = tk.Label(ventana, text="", font=("Arial", 10, "bold"), bg=color_fondo, fg=color_texto)
etiqueta_estado.pack(pady=15)

# Pie de página (Créditos)
pie = tk.Label(ventana, text="Creado por Alexis", font=("Arial", 9), fg="#6b7280", bg=color_fondo)
pie.pack(side=tk.BOTTOM, pady=10)

ventana.mainloop()