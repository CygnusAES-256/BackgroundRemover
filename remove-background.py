import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from rembg import remove

def procesamiento():
    print("If you don't have GPU drivers, the script will throw an error :(")
    root = tk.Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title = "Select an image", filetypes = [("Images", "*.png *.jpg *.jpeg *.webp *.bmp"), ("All extensions", "*.*")])

    if not ruta:
        print("No image selected")
        return
    print(f"Image: {ruta}")

    imagen_original = Image.open(ruta)
    imagen_procesada = remove(imagen_original)
    nombre_archivo = os.path.basename(ruta)
    nombre_base, _ = os.path.splitext(nombre_archivo)
    carpeta_guardado = filedialog.askdirectory(title = "Select a directory to save processed image")
    salida = os.path.join(carpeta_guardado, f"{nombre_base}_no_background.png")

    print("Please wait")
    imagen_procesada.save(salida)
    print(f"Image saved in:\n{salida}")

if __name__ == "__main__":
    procesamiento()