from datetime import datetime
from conexionBD import *
from login import * 
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class VeterinariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de la Veterinaria")

        # Variables
        self.nombre_mascota = tk.StringVar()
        self.tipo_mascota = tk.StringVar()
        self.peso_mascota = tk.DoubleVar()
        self.procedimiento = tk.IntVar()
        self.opcion_procedimiento = tk.IntVar()
        self.cantidad_accesorios = tk.IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        # Título
        title_label = tk.Label(self.root, text="Sistema de Gestión de la Veterinaria", font=("Arial", 18))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Registro de mascota
        tk.Label(self.root, text="Nombre de la Mascota:").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.nombre_mascota).grid(row=1, column=1)

        tk.Label(self.root, text="Tipo de Mascota:").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.tipo_mascota).grid(row=2, column=1)

        tk.Label(self.root, text="Peso de la Mascota (kg):").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.peso_mascota).grid(row=3, column=1)

        # Procedimientos
        tk.Label(self.root, text="Seleccione un Procedimiento:").grid(row=4, column=0, sticky=tk.W)
        procedimientos = ["Cirugías y/o procesos", "Vacunación", "Consulta", "Accesorios"]
        self.procedimiento_menu = ttk.Combobox(self.root, textvariable=self.procedimiento, values=procedimientos)
        self.procedimiento_menu.grid(row=4, column=1)
        self.procedimiento_menu.bind("<<ComboboxSelected>>", self.actualizar_opciones)

        # Opciones de procedimientos
        self.opciones_label = tk.Label(self.root, text="Opciones del Procedimiento:")
        self.opciones_label.grid(row=5, column=0, sticky=tk.W)

        self.opciones_menu = ttk.Combobox(self.root, textvariable=self.opcion_procedimiento)
        self.opciones_menu.grid(row=5, column=1)

        self.cantidad_label = tk.Label(self.root, text="Cantidad:")
        self.cantidad_label.grid(row=6, column=0, sticky=tk.W)

        self.cantidad_spinbox = tk.Spinbox(self.root, from_=1, to=10, textvariable=self.cantidad_accesorios)
        self.cantidad_spinbox.grid(row=6, column=1)

        # Botones
        tk.Button(self.root, text="Registrar Mascota", command=self.registrar_mascota).grid(row=7, column=0, pady=10)
        tk.Button(self.root, text="Agendar Cita", command=self.agendar_cita).grid(row=7, column=1, pady=10)

    def actualizar_opciones(self, event):
        procedimiento = self.procedimiento_menu.current() + 1
        if procedimiento == 1:
            opciones = ["Esterilización", "Baño para eliminar bichos", "Eutanasia", "Parto", "Tratamiento de huesos rotos", "Prótesis"]
        elif procedimiento == 4:
            opciones = ["Correa", "Chaleco/ropa", "Collar", "Perfumes", "Arenas"]
        else:
            opciones = []
        self.opciones_menu["values"] = opciones
        self.opciones_menu.set("")

        if procedimiento == 4:
            self.cantidad_label.grid(row=6, column=0, sticky=tk.W)
            self.cantidad_spinbox.grid(row=6, column=1)
        else:
            self.cantidad_label.grid_remove()
            self.cantidad_spinbox.grid_remove()

    def registrar_mascota(self):
        nombre = self.nombre_mascota.get()
        tipo = self.tipo_mascota.get()
        peso = self.peso_mascota.get()
        procedimiento = self.procedimiento_menu.current() + 1
        opcion = self.opciones_menu.current() + 1 if self.opciones_menu.get() else None
        cantidad = self.cantidad_accesorios.get()

        print(f"Mascota registrada: {nombre}, {tipo}, {peso}kg, Procedimiento: {procedimiento}, Opción: {opcion}, Cantidad: {cantidad}")
        self.limpiar_campos()

    def agendar_cita(self):
        nombre = self.nombre_mascota.get()
        fecha = simpledialog.askstring("Fecha de la cita", "Ingrese la fecha de la cita (YYYY-MM-DD):")
        hora = simpledialog.askstring("Hora de la cita", "Ingrese la hora de la cita (HH:MM:SS):")

        if fecha and hora:
            print(f"Cita agendada para {nombre} el {fecha} a las {hora}")
            self.limpiar_campos()
        else:
            print("Cita no agendada, falta información.")

    def limpiar_campos(self):
        self.nombre_mascota.set("")
        self.tipo_mascota.set("")
        self.peso_mascota.set(0)
        self.procedimiento.set(0)
        self.opcion_procedimiento.set(0)
        self.cantidad_accesorios.set(1)
        self.procedimiento_menu.set("")
        self.opciones_menu.set("")

# Código principal
if __name__ == "__main__":
    root = tk.Tk()
    app = VeterinariaApp(root)
    root.mainloop()
