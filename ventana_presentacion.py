import tkinter as tk
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado

class VentanaPresentacion:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Oculta la ventana principal al iniciar

        self.splash = tk.Toplevel(self.root)
        self.splash.geometry("1250x680+50+10")
        self.splash.overrideredirect(True)  # Sin bordes

        # Cargar la imagen de fondo
        self.imagen_fondo = Image.open("C:/Users/usuario/OneDrive/Escritorio/SAGI-NUEVO/img.jpg")
        self.imagen_fondo = self.imagen_fondo.resize((1250, 680), Image.LANCZOS)  # Ajusta el tamaño de la imagen al tamaño de la ventana
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

        # Label para la imagen de fondo
        label_fondo = tk.Label(self.splash, image=self.fondo)
        label_fondo.place(relwidth=1, relheight=1)  # Ajusta al tamaño de la ventana

        # Título de la ventana de presentación
        titulo = tk.Label(self.splash, text="Sistema de Gestión de Inscripción", font=("Arial", 24, "bold"), bg="LightBlue")
        titulo.pack(pady=20)

        mensaje = tk.Label(self.splash, text="Bienvenido al Sistema", font=("Arial", 16), bg="LightBlue")
        mensaje.pack(pady=10)

        # Botón para iniciar la aplicación
        boton_iniciar = tk.Button(self.splash, text="Iniciar", font=("Arial", 14), command=self.iniciar_app)
        boton_iniciar.pack(pady=20)

        # Vincula el cierre de la ventana splash con el cierre completo del programa
        self.splash.protocol("WM_DELETE_WINDOW", self.cerrar_todo)

    def iniciar_app(self):
        self.splash.destroy()  # Cierra la ventana de presentación
        self.root.after(200, self.root.deiconify)  # Muestra la ventana principal después de 200 ms

    def cerrar_todo(self):
        self.splash.destroy()  # Destruye la ventana de presentación
        self.root.quit()  # Cierra la aplicación completa

# Ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Ajusta el tamaño de la ventana principal si es necesario
    app = VentanaPresentacion(root)

    # Vincula el cierre de la ventana principal con el cierre completo del programa
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Destruye el root y cierra la aplicación
    root.mainloop()
