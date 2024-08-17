import tkinter as tk
from tkinter import messagebox
from login import *


TARIFA_BASE = 50
acumulador_Ingresos = 0
precio_accesorio_1 = 95
precio_accesorio_2 = 150
precio_accesorio_3 = 55
precio_accesorio_4 = 230
precio_accesorio_5 = 150
MAX_MASCOTAS = 10
contador_mascotas = 0
acumulador_nombres = ""
class VeterinariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" /.::Sistema de Gestión de la Veterinaria::.\ ")
        
        self.nombre_var = tk.StringVar()
        self.tipo_var = tk.StringVar()
        self.peso_var = tk.StringVar()
        self.procedimiento_var = tk.IntVar()
        self.opc_var = tk.IntVar()
        self.opc2_var = tk.IntVar()
        self.cantidad_accesorios_var = tk.IntVar()
        
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        
        tk.Label(self.root, text="Nombre de la mascota:", font=label_font, fg="blue").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.nombre_var, font=entry_font).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Tipo de mascota:", font=label_font, fg="blue").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.tipo_var, font=entry_font).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Peso de la mascota (kg):", font=label_font, fg="blue").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.peso_var, font=entry_font).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Procedimientos disponibles:", font=label_font, fg="green").grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        tk.Radiobutton(self.root, text="Cirugías y/o procesos", variable=self.procedimiento_var, value=1, font=entry_font).grid(row=4, column=0, sticky="w", padx=10)
        tk.Radiobutton(self.root, text="Vacunación", variable=self.procedimiento_var, value=2, font=entry_font).grid(row=5, column=0, sticky="w", padx=10)
        tk.Radiobutton(self.root, text="Consulta", variable=self.procedimiento_var, value=3, font=entry_font).grid(row=6, column=0, sticky="w", padx=10)
        tk.Radiobutton(self.root, text="Accesorios", variable=self.procedimiento_var, value=4, font=entry_font).grid(row=7, column=0, sticky="w", padx=10)

        tk.Button(self.root, text="Elegir Procedimiento", command=self.elegir_procedimiento, font=label_font, bg="lightgrey").grid(row=8, column=0, columnspan=2, pady=5)
        self.procedimiento_frame = tk.Frame(self.root)
        self.procedimiento_frame.grid(row=9, column=0, columnspan=2)

        tk.Button(self.root, text="Registrar", command=self.registrar_mascota, font=label_font, bg="lightgrey").grid(row=10, column=0, columnspan=2, pady=5)

    def elegir_procedimiento(self):
        for widget in self.procedimiento_frame.winfo_children():
            widget.destroy()
        
        if self.procedimiento_var.get() == 1:
            tk.Label(self.procedimiento_frame, text="Cirugías y procesos disponibles:", font=("Arial", 12, "bold"), fg="red").grid(row=0, column=0, columnspan=2)
            tk.Radiobutton(self.procedimiento_frame, text="Esterilización", variable=self.opc_var, value=1, font=("Arial", 12)).grid(row=1, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Baño para eliminar bichos", variable=self.opc_var, value=2, font=("Arial", 12)).grid(row=2, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Eutanasia", variable=self.opc_var, value=3, font=("Arial", 12)).grid(row=3, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Parto", variable=self.opc_var, value=4, font=("Arial", 12)).grid(row=4, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Tratamiento de huesos rotos", variable=self.opc_var, value=5, font=("Arial", 12)).grid(row=5, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Prótesis", variable=self.opc_var, value=6, font=("Arial", 12)).grid(row=6, column=0, sticky="w")
        
        elif self.procedimiento_var.get() == 2:
            tk.Label(self.procedimiento_frame, text="Vacunas Disponibles", font=("Arial", 12, "bold"), fg="red").grid(row=0, column=0, columnspan=2)
            tk.Radiobutton(self.procedimiento_frame, text="Rabia", variable=self.opc_var, value=4, font=("Arial", 12)).grid(row=4, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Parvovirus", variable=self.opc_var, value=5, font=("Arial", 12)).grid(row=5, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Pulgas", variable=self.opc_var, value=6, font=("Arial", 12)).grid(row=6, column=0, sticky="w")
        
        elif self.procedimiento_var.get() == 4:
            tk.Label(self.procedimiento_frame, text="Accesorios disponibles:", font=("Arial", 12, "bold"), fg="red").grid(row=0, column=0, columnspan=2)
            tk.Radiobutton(self.procedimiento_frame, text="Correa", variable=self.opc2_var, value=1, font=("Arial", 12)).grid(row=1, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Chaleco/ropa", variable=self.opc2_var, value=2, font=("Arial", 12)).grid(row=2, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Collar", variable=self.opc2_var, value=3, font=("Arial", 12)).grid(row=3, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Perfumes", variable=self.opc2_var, value=4, font=("Arial", 12)).grid(row=4, column=0, sticky="w")
            tk.Radiobutton(self.procedimiento_frame, text="Arenas", variable=self.opc2_var, value=5, font=("Arial", 12)).grid(row=5, column=0, sticky="w")
            tk.Label(self.procedimiento_frame, text="Cantidad:", font=("Arial", 12)).grid(row=6, column=0, sticky="w")
            tk.Entry(self.procedimiento_frame, textvariable=self.cantidad_accesorios_var, font=("Arial", 12)).grid(row=6, column=1, sticky="w")

    def registrar_mascota(self):
        global contador_mascotas, acumulador_Ingresos, acumulador_nombres
        nombre_mascota = self.nombre_var.get()
        tipo_mascota = self.tipo_var.get()
        peso_mascota = float(self.peso_var.get())
        costo_procedimiento = 0
        
        if self.procedimiento_var.get() == 1:
            if self.opc_var.get() == 1:
                costo_procedimiento = TARIFA_BASE * 10
            elif self.opc_var.get() == 2:
                costo_procedimiento = TARIFA_BASE * 6
            elif self.opc_var.get() == 3:
                costo_procedimiento = TARIFA_BASE * 13
            elif self.opc_var.get() == 4:
                costo_procedimiento = TARIFA_BASE * 24
            elif self.opc_var.get() == 5:
                costo_procedimiento = TARIFA_BASE * 16
            elif self.opc_var.get() == 6:
                costo_procedimiento = TARIFA_BASE * 30 if self.opc2_var.get() == 1 else TARIFA_BASE * 18
        elif self.procedimiento_var.get() == 2:
            costo_procedimiento = TARIFA_BASE * 1.5
        elif self.procedimiento_var.get() == 3:
            costo_procedimiento = TARIFA_BASE
        elif self.procedimiento_var.get() == 4:
            if self.opc2_var.get() == 1:
                costo_procedimiento = precio_accesorio_1 * self.cantidad_accesorios_var.get()
            elif self.opc2_var.get() == 2:
                costo_procedimiento = precio_accesorio_2 * self.cantidad_accesorios_var.get()
            elif self.opc2_var.get() == 3:
                costo_procedimiento = precio_accesorio_3 * self.cantidad_accesorios_var.get()
            elif self.opc2_var.get() == 4:
                costo_procedimiento = precio_accesorio_4 * self.cantidad_accesorios_var.get()
            elif self.opc2_var.get() == 5:
                costo_procedimiento = precio_accesorio_5 * self.cantidad_accesorios_var.get()

        contador_mascotas += 1
        acumulador_Ingresos += costo_procedimiento
        acumulador_nombres += nombre_mascota + " "
        
        messagebox.showinfo("Registro Exitoso", f"El costo final del procedimiento para {nombre_mascota} es de $ {costo_procedimiento}")
    
    def mostrar_resultados(self):
        messagebox.showinfo("Resultados",
                            f"Total de mascotas registradas: {contador_mascotas}\n"
                            f"Ingresos totales: ${acumulador_Ingresos}\n"
                            f"Nombres de las mascotas ingresadas: {acumulador_nombres.strip()}")

root = tk.Tk()
app = VeterinariaApp(root)

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="Opciones", menu=filemenu)
filemenu.add_command(label="Mostrar resultados", command=app.mostrar_resultados)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

root.mainloop()