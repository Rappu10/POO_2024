import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from conexionbd import *

class ConexionBD:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1205',
                database='SistVeterinaria'
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def ejecutar_consulta(self, consulta, parametros):
        try:
            self.cursor.execute(consulta, parametros)
            self.conn.commit()
            print("Consulta ejecutada correctamente")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def ejecutar_consulta_select(self, consulta, parametros=None):
        try:
            self.cursor.execute(consulta, parametros)
            resultados = self.cursor.fetchall()
            return resultados
        except Error as e:
            print(f"Error al ejecutar la consulta SELECT: {e}")
            return []

    def cerrar(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos cerrada")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Sistema de Gestión de la Veterinaria")

        # Configuración para pantalla completa
        self.root.attributes('-fullscreen', True)

        # Configuración del diseño de la interfaz
        self.root.configure(background='lightblue')

        # Variables
        self.usuario = tk.StringVar()
        self.contrasena = tk.StringVar()

        # Creación de widgets
        self.create_widgets()

    def create_widgets(self):
        # Título
        title_label = tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 48), bg='lightblue', fg='blue')
        title_label.pack(pady=60)

        # Campo de usuario
        usuario_label = tk.Label(self.root, text="Usuario:", font=("Arial", 36), bg='lightblue', fg='red')
        usuario_label.pack(pady=20)
        usuario_entry = tk.Entry(self.root, textvariable=self.usuario, font=("Arial", 36), width=30)
        usuario_entry.pack()

        # Campo de contraseña
        contrasena_label = tk.Label(self.root, text="Contraseña:", font=("Arial", 36), bg='lightblue', fg='red')
        contrasena_label.pack(pady=20)
        contrasena_entry = tk.Entry(self.root, textvariable=self.contrasena, font=("Arial", 36), width=30, show='*')
        contrasena_entry.pack()

        # Botón de inicio de sesión
        login_button = tk.Button(self.root, text="Iniciar Sesión", font=("Arial", 36), command=self.iniciar_sesion)
        login_button.pack(pady=40)

        # Botón de salir
        exit_button = tk.Button(self.root, text="Salir", font=("Arial", 36), command=self.salir)
        exit_button.pack(pady=20)

    def iniciar_sesion(self):
        usuario = self.usuario.get()
        contrasena = self.contrasena.get()

        # Validación simple de usuario y contraseña
        if usuario == "admin" and contrasena == "admin":  # Puedes cambiar las credenciales aquí
            self.root.destroy()  # Cierra la ventana de inicio de sesión
            root = tk.Tk()  # Crea una nueva ventana para la aplicación principal
            app = VeterinariaApp(root)  # Inicia la aplicación principal
            root.attributes('-fullscreen', True)  # Maximiza la ventana automáticamente
            root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def salir(self):
        self.root.destroy()  # Cierra la ventana de inicio de sesión

class VeterinariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de la Veterinaria")
        self.root.attributes('-fullscreen', True)  # Maximiza la ventana automáticamente
        self.root.configure(background='lightblue')

        # Conexión a la base de datos
        self.db = ConexionBD()

        # Variables
        self.nombre_mascota = tk.StringVar()
        self.tipo_mascota = tk.StringVar()
        self.peso_mascota = tk.DoubleVar()
        self.procedimiento = tk.StringVar()
        self.opcion_procedimiento = tk.StringVar()
        self.cantidad_accesorios = tk.IntVar(value=1)
        self.mascota_info = ""

        self.create_widgets()

    def create_widgets(self):
        # Menú
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        menu_ver = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ver", menu=menu_ver)
        menu_ver.add_command(label="Ver Mascota Registrada", command=self.mostrar_info_mascota)

        # Título
        title_label = tk.Label(self.root, text="Sistema de Gestión de la Veterinaria", font=("Arial", 48), bg='lightblue', fg='blue')
        title_label.grid(row=0, column=0, columnspan=2, pady=40)

        # Registro de mascota
        tk.Label(self.root, text="Nombre de la Mascota:", font=("Arial", 36), bg='lightblue', fg='red').grid(row=1, column=0, sticky=tk.E, padx=20)
        tk.Entry(self.root, textvariable=self.nombre_mascota, font=("Arial", 36), width=20).grid(row=1, column=1, padx=20)

        tk.Label(self.root, text="Tipo de Mascota:", font=("Arial", 36), bg='lightblue', fg='red').grid(row=2, column=0, sticky=tk.E, padx=20)
        tk.Entry(self.root, textvariable=self.tipo_mascota, font=("Arial", 36), width=20).grid(row=2, column=1, padx=20)

        tk.Label(self.root, text="Peso de la Mascota (kg):", font=("Arial", 36), bg='lightblue', fg='red').grid(row=3, column=0, sticky=tk.E, padx=20)
        tk.Entry(self.root, textvariable=self.peso_mascota, font=("Arial", 36), width=20).grid(row=3, column=1, padx=20)

        # Procedimientos
        tk.Label(self.root, text="Seleccione un Procedimiento:", font=("Arial", 36), bg='lightblue', fg='red').grid(row=4, column=0, sticky=tk.E, padx=20)
        procedimientos = ["Cirugías y/o procesos", "Vacunación", "Consulta", "Accesorios"]
        self.procedimiento_menu = ttk.Combobox(self.root, textvariable=self.procedimiento, values=procedimientos, font=("Arial", 36), state="readonly", width=20)
        self.procedimiento_menu.grid(row=4, column=1, padx=20)
        self.procedimiento_menu.bind("<<ComboboxSelected>>", self.actualizar_opciones)

        # Opciones de procedimientos
        self.opciones_label = tk.Label(self.root, text="Opciones del Procedimiento:", font=("Arial", 36), bg='lightblue', fg='red')
        self.opciones_label.grid(row=5, column=0, sticky=tk.E, padx=20)

        self.opciones_menu = ttk.Combobox(self.root, textvariable=self.opcion_procedimiento, font=("Arial", 36), state="readonly", width=20)
        self.opciones_menu.grid(row=5, column=1, padx=20)

        self.cantidad_label = tk.Label(self.root, text="Cantidad:", font=("Arial", 36), bg='lightblue', fg='red')
        self.cantidad_label.grid(row=6, column=0, sticky=tk.E, padx=20)

        self.cantidad_spinbox = tk.Spinbox(self.root, from_=1, to=10, textvariable=self.cantidad_accesorios, font=("Arial", 36), width=5)
        self.cantidad_spinbox.grid(row=6, column=1, padx=20)

        # Botones
        tk.Button(self.root, text="Registrar Mascota", command=self.registrar_mascota, font=("Arial", 36), width=15).grid(row=7, column=0, pady=30)
        tk.Button(self.root, text="Agendar Cita", command=self.agendar_cita, font=("Arial", 36), width=15).grid(row=7, column=1, pady=30)

        # Botón de salir
        tk.Button(self.root, text="Salir", command=self.salir, font=("Arial", 36), width=15).grid(row=8, column=0, columnspan=2, pady=30)

        # Configuración de la grilla
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_rowconfigure(8, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def actualizar_opciones(self, event):
        procedimiento = self.procedimiento.get()
        if procedimiento == "Cirugías y/o procesos":
            opciones = ["Cirugía general", "Cirugía ortopédica", "Esterilización"]
        elif procedimiento == "Vacunación":
            opciones = ["Vacuna de parvovirus", "Vacuna quíntuple", "Vacuna de leptospirosis", "Vacuna de hepatitis"]
        elif procedimiento == "Consulta":
            opciones = ["Consulta general", "Consulta dermatológica", "Consulta odontológica", "Consulta de nutrición"]
        elif procedimiento == "Accesorios":
            opciones = ["Collares", "Correas", "Juguetes", "Camas", "Comederos y bebederos"]
        else:
            opciones = []
        self.opciones_menu['values'] = opciones

    def registrar_mascota(self):
        nombre = self.nombre_mascota.get()
        tipo = self.tipo_mascota.get()
        peso = self.peso_mascota.get()
        procedimiento = self.procedimiento.get()
        opcion = self.opcion_procedimiento.get()
        cantidad = self.cantidad_accesorios.get()

        # Validación
        if not nombre or not tipo or not peso or not procedimiento:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Inserción de datos en la base de datos
        consulta = """
        INSERT INTO Mascotas (nombre, tipo, peso) VALUES (%s, %s, %s)
        """
        parametros = (nombre, tipo, peso)
        self.db.ejecutar_consulta(consulta, parametros)

        if procedimiento == "Accesorios":
            consulta_accesorios = """
            INSERT INTO Registros (nombre_mascota, procedimiento, opcion_procedimiento, cantidad) VALUES (%s, %s, %s, %s)
            """
            parametros_accesorios = (nombre, procedimiento, opcion, cantidad)
            self.db.ejecutar_consulta(consulta_accesorios, parametros_accesorios)

        messagebox.showinfo("Éxito", f"Mascota registrada: {nombre}, {tipo}, {peso}kg\nProcedimiento: {procedimiento}, Opción: {opcion}, Cantidad: {cantidad}")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_mascota.set("")
        self.tipo_mascota.set("")
        self.peso_mascota.set(0.0)
        self.procedimiento.set("")
        self.opcion_procedimiento.set("")
        self.cantidad_accesorios.set(1)

    def agendar_cita(self):
        # Recupera las mascotas registradas
        consulta = "SELECT id, nombre FROM Mascotas"
        mascotas = self.db.ejecutar_consulta_select(consulta)

        if not mascotas:
            messagebox.showinfo("Información", "No hay mascotas registradas.")
            return

        # Muestra un cuadro de diálogo para seleccionar una mascota
        mascotas_dict = {f"{nombre}": id for id, nombre in mascotas}
        seleccion = simpledialog.askstring("Seleccionar Mascota", "Ingrese el nombre de la mascota:", initialvalue=list(mascotas_dict.keys())[0])
        if seleccion in mascotas_dict:
            mascota_id = mascotas_dict[seleccion]
            # Aquí puedes agregar la lógica para agendar la cita
            messagebox.showinfo("Cita Agendada", f"Cita agendada para la mascota: {seleccion} (ID: {mascota_id})")
        else:
            messagebox.showwarning("Advertencia", "Nombre de mascota no válido.")

    def mostrar_info_mascota(self):
        # Recupera las mascotas registradas
        consulta = "SELECT nombre, tipo, peso FROM Mascotas"
        mascotas = self.db.ejecutar_consulta_select(consulta)

        if not mascotas:
            messagebox.showinfo("Información", "No hay mascotas registradas.")
            return

        # Muestra la información de las mascotas
        mensaje = "Mascotas Registradas:\n\n"
        for nombre, tipo, peso in mascotas:
            mensaje += f"Nombre: {nombre}, Tipo: {tipo}, Peso: {peso}kg\n"

        messagebox.showinfo("Información de Mascotas", mensaje)

    def salir(self):
        self.db.cerrar()  # Cierra la conexión a la base de datos
        self.root.destroy()  # Cierra la ventana principal

def iniciar_sesion():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_sesion()
