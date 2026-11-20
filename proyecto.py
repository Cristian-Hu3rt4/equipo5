import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Escuela Primaria Nezahualcóyotl
# Una sola ventana principal: cada botón cambia de pantalla sin abrir varias raíces.
AZUL = "#0f2c61"
DORADO = "#c9a86a"
FONDO = "#f1f5f9"
BLANCO = "white"
GRIS = "#64748b"

root = tk.Tk()
root.title("Escuela Primaria Nezahualcóyotl | Sistema de Gestión Académica")
root.geometry("1200x720")
root.minsize(360, 560)
root.configure(bg=FONDO)


contenedor = tk.Frame(root, bg=FONDO)
contenedor.pack(fill="both", expand=True)
pantallas = {}

def mostrar(nombre):
    """Muestra una pantalla dentro de la ventana principal."""
    for pantalla in pantallas.values():
        pantalla.pack_forget()
    pantallas[nombre].pack(fill="both", expand=True)

def crear_pantalla(nombre, color=FONDO):
    frame = tk.Frame(contenedor, bg=color)
    pantallas[nombre] = frame
    return frame

def etiqueta(parent, texto, **kwargs):
    return tk.Label(parent, text=texto, **kwargs)

# -------------------- LOGIN DOCENTE --------------------
login_doc = crear_pantalla("login_doc", FONDO)
login_doc.columnconfigure(0, weight=1)
login_doc.rowconfigure(0, weight=1)

card_doc = tk.Frame(login_doc, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
card_doc.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
card_doc.columnconfigure(1, weight=1)
card_doc.rowconfigure(0, weight=1)

izq_doc = tk.Frame(card_doc, bg=AZUL, width=350)
izq_doc.grid(row=0, column=0, sticky="nsew")
izq_doc.grid_propagate(False)
etiqueta(izq_doc, "◆", bg=AZUL, fg=DORADO, font=("Segoe UI", 50, "bold")).pack(pady=(60, 10))
etiqueta(izq_doc, "ESCUELA PRIMARIA\nNEZAHUALCÓYOTL", bg=AZUL, fg=BLANCO,
         font=("Segoe UI", 16, "bold"), justify="center").pack()
etiqueta(izq_doc, "Sistema de Gestión Académica", bg=AZUL, fg="#94a3b8",
         font=("Segoe UI", 10)).pack(pady=15)
tk.Frame(izq_doc, bg=DORADO, height=3, width=80).pack(pady=20)

der_doc = tk.Frame(card_doc, bg=BLANCO)
der_doc.grid(row=0, column=1, sticky="nsew", padx=35, pady=30)
etiqueta(der_doc, "Bienvenido de nuevo", bg=BLANCO, fg=AZUL,
         font=("Segoe UI", 20, "bold")).pack(anchor="w")
etiqueta(der_doc, "Ingresa tus credenciales", bg=BLANCO, fg=GRIS,
         font=("Segoe UI", 10)).pack(anchor="w", pady=(2, 25))
etiqueta(der_doc, "USUARIO", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w")
entrada_usuario_doc = tk.Entry(der_doc, font=("Segoe UI", 11), bg="#f8fafc", relief="flat",
                               highlightbackground="#e2e8f0", highlightthickness=1)
entrada_usuario_doc.pack(fill="x", ipady=10, pady=(5, 15))
entrada_usuario_doc.insert(0, "docente.lmartinez")
etiqueta(der_doc, "CONTRASEÑA", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w")
entrada_clave_doc = tk.Entry(der_doc, font=("Segoe UI", 11), bg="#f8fafc", relief="flat",
                             show="•", highlightbackground="#e2e8f0", highlightthickness=1)
entrada_clave_doc.pack(fill="x", ipady=10, pady=(5, 5))
entrada_clave_doc.insert(0, "12345678")

def ingresar_docente():
    # Demo: aquí puedes conectar la validación real de usuario y contraseña.
    if entrada_usuario_doc.get().strip() and entrada_clave_doc.get():
        mostrar("docente")
    else:
        messagebox.showwarning("Datos incompletos", "Escribe tu usuario y contraseña.")

tk.Button(der_doc, text="Ingresar al Sistema", bg=AZUL, fg=BLANCO,
          font=("Segoe UI", 11, "bold"), relief="flat", pady=12,
          cursor="hand2", command=ingresar_docente).pack(fill="x", pady=(20, 10))
tk.Button(der_doc, text="Acceso de Dirección", bg=BLANCO, fg=AZUL,
          font=("Segoe UI", 9, "bold"), relief="flat", cursor="hand2",
          command=lambda: mostrar("login_dir")).pack(anchor="w", pady=4)

def ajustar_login_doc(event=None):
    if not login_doc.winfo_exists():
        return
    ancho = login_doc.winfo_width()
    if ancho < 700:
        izq_doc.grid_configure(row=0, column=0, columnspan=2)
        izq_doc.configure(height=180, width=max(ancho, 360))
        der_doc.grid_configure(row=1, column=0, columnspan=2)
    else:
        izq_doc.grid_configure(row=0, column=0, columnspan=1)
        izq_doc.configure(width=350, height=500)
        der_doc.grid_configure(row=0, column=1, columnspan=1)

login_doc.bind("<Configure>", lambda e: root.after_idle(ajustar_login_doc))

# -------------------- LOGIN DIRECTOR --------------------
login_dir = crear_pantalla("login_dir", AZUL)
marco_dir = tk.Frame(login_dir, bg=AZUL)
marco_dir.pack(expand=True, fill="both", padx=15, pady=15)
tarjeta_dir = tk.Frame(marco_dir, bg=BLANCO, highlightbackground=DORADO, highlightthickness=2)
tarjeta_dir.pack(expand=True, fill="both", padx=10, pady=10)
cab_dir = tk.Frame(tarjeta_dir, bg=BLANCO)
cab_dir.pack(fill="x", padx=30, pady=(30, 10))
etiqueta(cab_dir, "◆", bg=BLANCO, fg=DORADO, font=("Segoe UI", 28, "bold")).pack()
etiqueta(cab_dir, "ESCUELA NEZAHUALCÓYOTL", bg=BLANCO, fg=AZUL,
         font=("Segoe UI", 13, "bold")).pack()
tk.Label(cab_dir, text="PANEL DIRECTIVO", bg=AZUL, fg=BLANCO,
         font=("Segoe UI", 8, "bold"), padx=12, pady=3).pack(pady=8)
tk.Frame(cab_dir, bg="#e2e8f0", height=1).pack(fill="x", pady=15)
form_dir = tk.Frame(tarjeta_dir, bg=BLANCO)
form_dir.pack(fill="x", padx=30, pady=5)

def campo_director(label, valor, password=False):
    tk.Label(form_dir, text=label, bg=BLANCO, fg="#94a3b8",
             font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(12, 0))
    e = tk.Entry(form_dir, font=("Segoe UI", 11), bg="#f8fafc", relief="flat",
                 highlightbackground="#e2e8f0", highlightthickness=1,
                 show="•" if password else "")
    e.pack(fill="x", ipady=10, pady=(5, 0))
    e.insert(0, valor)
    return e

entrada_nombre_dir = campo_director("NOMBRE DE USUARIO", "Dir. Alejandro Torres")
entrada_correo_dir = campo_director("CORREO INSTITUCIONAL", "direccion@nezahualcoyotl.edu.mx")
entrada_clave_dir = campo_director("CONTRASEÑA DIRECTIVA", "12345678", True)
tk.Label(form_dir, text="Este acceso queda registrado en bitácora", bg=BLANCO,
         fg="#dc2626", font=("Segoe UI", 8)).pack(anchor="w", pady=10)

def ingresar_director():
    if (entrada_nombre_dir.get().strip() and entrada_correo_dir.get().strip()
            and entrada_clave_dir.get()):
        mostrar("director")
    else:
        messagebox.showwarning("Datos incompletos", "Completa todos los campos.")

tk.Button(form_dir, text="Acceder como Director", bg=AZUL, fg=BLANCO,
          font=("Segoe UI", 11, "bold"), relief="flat", pady=13,
          cursor="hand2", command=ingresar_director).pack(fill="x", pady=(20, 5))
tk.Button(form_dir, text="Volver al acceso docente", bg=BLANCO, fg=GRIS,
          font=("Segoe UI", 9), relief="flat", cursor="hand2",
          command=lambda: mostrar("login_doc")).pack(pady=5)
pie_dir = tk.Frame(tarjeta_dir, bg="#f8fafc")
pie_dir.pack(fill="x", side="bottom", ipady=10, pady=(20, 0))
tk.Label(pie_dir, text="Sistema validado por Dirección | 2025-2026",
         bg="#f8fafc", fg="#94a3b8", font=("Segoe UI", 8)).pack()

# -------------------- PANEL DIRECTOR --------------------
director = crear_pantalla("director", FONDO)
style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass
style.configure("Treeview", font=("Segoe UI", 10), rowheight=38,
                background=BLANCO, fieldbackground=BLANCO)
style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"),
                background="#f8fafc", foreground=AZUL)

header_dir = tk.Frame(director, bg=AZUL, height=80)
header_dir.pack(fill="x")
header_dir.pack_propagate(False)
izq_header = tk.Frame(header_dir, bg=AZUL)
izq_header.pack(side="left", padx=25, pady=10)
tk.Label(izq_header, text="◆", bg=AZUL, fg=DORADO,
         font=("Segoe UI", 26, "bold")).pack(side="left", padx=(0, 12))
info_header = tk.Frame(izq_header, bg=AZUL)
info_header.pack(side="left")
tk.Label(info_header, text="ESCUELA PRIMARIA NEZAHUALCÓYOTL", bg=AZUL,
         fg=BLANCO, font=("Segoe UI", 13, "bold")).pack(anchor="w")
tk.Label(info_header, text="DIRECTOR", bg=AZUL, fg=DORADO,
         font=("Segoe UI", 10, "bold")).pack(anchor="w")
derecha_header = tk.Frame(header_dir, bg=AZUL)
derecha_header.pack(side="right", padx=25)
tk.Label(derecha_header, text=f"Dir. Alejandro Torres\n{datetime.now().strftime('%d/%m/%Y')} | En línea",
         bg=AZUL, fg="#cbd5e1", font=("Segoe UI", 9), justify="right").pack()
tk.Label(derecha_header, text="● Sistema Activo", bg=AZUL,
         fg="#22c55e", font=("Segoe UI", 8, "bold")).pack(anchor="e")

cuerpo_dir = tk.Frame(director, bg=FONDO)
cuerpo_dir.pack(fill="both", expand=True, padx=15, pady=15)
cuerpo_dir.columnconfigure(0, weight=3)
cuerpo_dir.columnconfigure(1, weight=1)
cuerpo_dir.rowconfigure(0, weight=1)
panel_izq_dir = tk.Frame(cuerpo_dir, bg=FONDO)
panel_izq_dir.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
panel_izq_dir.columnconfigure(0, weight=1)

kpi_dir = tk.Frame(panel_izq_dir, bg=FONDO)
kpi_dir.pack(fill="x", pady=(0, 12))
for titulo, valor, color in [
    ("ASISTENCIA GLOBAL", "94.2%", "#16a34a"),
    ("GRUPOS", "6 activos", AZUL),
    ("ALERTAS", "3 reportes", "#dc2626")
]:
    c = tk.Frame(kpi_dir, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
    c.pack(side="left", fill="x", expand=True, padx=4)
    tk.Frame(c, bg=color, height=4).pack(fill="x")
    tk.Label(c, text=titulo, bg=BLANCO, fg="#94a3b8",
             font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=12, pady=(8, 0))
    tk.Label(c, text=valor, bg=BLANCO, fg=AZUL,
             font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=12, pady=(2, 10))

contenido_dir = tk.Frame(panel_izq_dir, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
contenido_dir.pack(fill="both", expand=True)
tit_dir = tk.Frame(contenido_dir, bg=BLANCO)
tit_dir.pack(fill="x", padx=20, pady=15)
tk.Label(tit_dir, text="Vista General de Grupos", bg=BLANCO, fg=AZUL,
         font=("Segoe UI", 13, "bold")).pack(side="left")
tk.Label(tit_dir, text="Ciclo 2025-2026", bg="#eef2ff", fg="#4338ca",
         font=("Segoe UI", 8, "bold"), padx=8, pady=3).pack(side="left", padx=10)
tabla_dir = ttk.Treeview(contenido_dir, columns=("Grupo", "Titular", "Alumnos", "Asist.", "Estatus"),
                         show="headings", height=10)
for col, ancho in [("Grupo", 90), ("Titular", 200), ("Alumnos", 80), ("Asist.", 80), ("Estatus", 100)]:
    tabla_dir.heading(col, text=col)
    tabla_dir.column(col, width=ancho, anchor="center")
for fila in [
    ("1° A", "Prof. Juárez", "31", "98%", "Excelente"),
    ("2° B", "Prof. Rivera", "30", "92%", "Bueno"),
    ("5° B", "Prof. Laura M.", "32", "96%", "Excelente"),
    ("6° A", "Prof. Torres", "29", "89%", "Atención")
]:
    tabla_dir.insert("", "end", values=fila)
tabla_dir.pack(fill="both", expand=True, padx=20, pady=(0, 20))

panel_der_dir = tk.Frame(cuerpo_dir, bg=BLANCO, highlightbackground="#e2e8f0",
                         highlightthickness=1, width=320)
panel_der_dir.grid(row=0, column=1, sticky="nsew")
panel_der_dir.grid_propagate(False)
tk.Label(panel_der_dir, text="HERRAMIENTAS DE DIRECCIÓN", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=20, pady=(20, 15))

def boton_herramienta(icono, titulo, descripcion, color=AZUL):
    marco = tk.Frame(panel_der_dir, bg=BLANCO, highlightbackground="#e2e8f0",
                     highlightthickness=1)
    marco.pack(fill="x", padx=15, pady=7)
    lado = tk.Frame(marco, bg=color, width=50, height=60)
    lado.pack(side="left", fill="y")
    lado.pack_propagate(False)
    tk.Label(lado, text=icono, bg=color, fg=BLANCO, font=("Segoe UI", 18)).pack(expand=True)
    texto = tk.Frame(marco, bg=BLANCO)
    texto.pack(side="left", fill="x", expand=True, padx=12, pady=10)
    tk.Label(texto, text=titulo, bg=BLANCO, fg="#0f172a",
             font=("Segoe UI", 11, "bold")).pack(anchor="w")
    tk.Label(texto, text=descripcion, bg=BLANCO, fg=GRIS,
             font=("Segoe UI", 8), wraplength=170, justify="left").pack(anchor="w", pady=(2, 0))
    return marco

boton_herramienta("◫", "ASISTENCIAS", "Consulta global por grupo, día y docente. Exporta a Excel.")
boton_herramienta("☰", "REPORTES", "Genera reportes mensuales y de supervisión para SEP.", "#1e40af")
boton_herramienta("✎", "CREAR CARTA COMPROMISO", "Redacta carta compromiso para padres por faltas o conducta.", DORADO)
tk.Frame(panel_der_dir, bg="#e2e8f0", height=1).pack(fill="x", padx=20, pady=15)
tk.Label(panel_der_dir, text="Acción rápida:", bg=BLANCO, fg=AZUL,
         font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20)
tk.Button(panel_der_dir, text="+ Nueva Carta Compromiso", bg=AZUL, fg=BLANCO,
          font=("Segoe UI", 11, "bold"), relief="flat", pady=12,
          command=lambda: messagebox.showinfo("Carta compromiso", "Aquí se abrirá el formulario de carta compromiso.")
          ).pack(fill="x", padx=15, pady=10)
tk.Label(panel_der_dir, text="Plantilla oficial con logo, firma\ny sello de la escuela.",
         bg=BLANCO, fg="#94a3b8", font=("Segoe UI", 8), justify="left").pack(anchor="w", padx=20)
tk.Label(panel_der_dir, text="Documentos generados quedan en\nbitácora de Dirección",
         bg="#f8fafc", fg=GRIS, font=("Segoe UI", 8), justify="center").pack(side="bottom", fill="x", ipady=12, pady=(10, 0))

def ajustar_director(event=None):
    ancho = director.winfo_width()
    if ancho < 800:
        panel_izq_dir.grid_configure(row=1, column=0, columnspan=2, padx=0, pady=(10, 0))
        panel_der_dir.grid_configure(row=0, column=0, columnspan=2, sticky="ew")
        panel_der_dir.configure(width=max(300, ancho - 30))
        cuerpo_dir.rowconfigure(0, weight=0)
        cuerpo_dir.rowconfigure(1, weight=1)
    else:
        panel_der_dir.grid_configure(row=0, column=1, columnspan=1, sticky="nsew")
        panel_der_dir.configure(width=320)
        panel_izq_dir.grid_configure(row=0, column=0, columnspan=1, padx=(0, 10), pady=0)
        cuerpo_dir.rowconfigure(0, weight=1)
        cuerpo_dir.rowconfigure(1, weight=0)

director.bind("<Configure>", lambda e: root.after_idle(ajustar_director))

# -------------------- PANEL DOCENTE --------------------
docente = crear_pantalla("docente", FONDO)
style.configure("Docente.Treeview", font=("Segoe UI", 10), rowheight=40,
                background=BLANCO, fieldbackground=BLANCO)
header_doc = tk.Frame(docente, bg=AZUL, height=70)
header_doc.pack(fill="x")
header_doc.pack_propagate(False)
tk.Label(header_doc, text="◆  ESCUELA PRIMARIA NEZAHUALCÓYOTL", bg=AZUL, fg=BLANCO,
         font=("Segoe UI", 13, "bold")).pack(side="left", padx=20)
tk.Label(header_doc, text=datetime.now().strftime("%d %b %Y"), bg=AZUL,
         fg="#cbd5e1", font=("Segoe UI", 9)).pack(side="right", padx=20)

kpi_doc = tk.Frame(docente, bg=FONDO)
kpi_doc.pack(fill="x", padx=12, pady=10)
tarjetas_kpi_doc = []
for titulo, valor, color in [
    ("MATRÍCULA", "32 alumnos", AZUL),
    ("ASISTENCIA", "96%", "#16a34a"),
    ("INCIDENCIAS", "2", "#dc2626"),
    ("GRUPO", "5° B", DORADO)
]:
    tarjeta = tk.Frame(kpi_doc, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
    tk.Frame(tarjeta, bg=color, height=4).pack(fill="x")
    interior = tk.Frame(tarjeta, bg=BLANCO)
    interior.pack(fill="x", padx=12, pady=8)
    tk.Label(interior, text=titulo, bg=BLANCO, fg=GRIS,
             font=("Segoe UI", 8, "bold")).pack(anchor="w")
    tk.Label(interior, text=valor, bg=BLANCO, fg="#0f172a",
             font=("Segoe UI", 14, "bold")).pack(anchor="w")
    tarjetas_kpi_doc.append(tarjeta)

datos_doc = tk.Frame(docente, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
datos_doc.pack(fill="x", padx=12, pady=5, ipady=6)
datos_doc.columnconfigure(0, weight=2)
datos_doc.columnconfigure(1, weight=1)
f_doc = tk.Frame(datos_doc, bg=BLANCO)
f_doc.grid(row=0, column=0, sticky="ew", padx=15, pady=5)
tk.Label(f_doc, text="DOCENTE TITULAR", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w")
entrada_titular = tk.Entry(f_doc, font=("Segoe UI", 11, "bold"), fg=AZUL, bg="#f8fafc", relief="flat")
entrada_titular.pack(fill="x", ipady=6, pady=(3, 0))
entrada_titular.insert(0, "Prof. Laura Martínez Gómez")
entrada_titular.config(state="readonly")
f_grupo = tk.Frame(datos_doc, bg=BLANCO)
f_grupo.grid(row=0, column=1, sticky="ew", padx=15, pady=5)
tk.Label(f_grupo, text="GRUPO ACTIVO", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w")
combo_grupo = ttk.Combobox(f_grupo, values=["5° - Grupo A", "5° - Grupo B", "5° - Grupo C"],
                           font=("Segoe UI", 10))
combo_grupo.pack(fill="x", pady=(3, 0), ipady=3)
combo_grupo.set("5° — Grupo B")

cuerpo_doc = tk.Frame(docente, bg=FONDO)
cuerpo_doc.pack(fill="both", expand=True, padx=12, pady=10)
cuerpo_doc.columnconfigure(1, weight=1)
cuerpo_doc.rowconfigure(0, weight=1)
menu_doc = tk.Frame(cuerpo_doc, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
menu_doc.grid(row=0, column=0, sticky="ns", padx=(0, 10))
contenido_doc = tk.Frame(cuerpo_doc, bg=BLANCO, highlightbackground="#e2e8f0", highlightthickness=1)
contenido_doc.grid(row=0, column=1, sticky="nsew")
contenido_doc.columnconfigure(0, weight=1)
contenido_doc.rowconfigure(1, weight=1)
tk.Label(menu_doc, text="MENÚ", bg=BLANCO, fg="#94a3b8",
         font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=15, pady=(15, 8))

def accion_menu_doc(nombre):
    messagebox.showinfo(nombre, f"Sección «{nombre}» seleccionada.")

botones_menu_doc = []
for i, texto in enumerate(["  ●  Listas", "  ▲  Incidencias", "  ■  Justificantes", "  ◆  Reportes"]):
    b = tk.Button(menu_doc, text=texto, bg=AZUL if i == 0 else BLANCO,
                  fg=BLANCO if i == 0 else "#334155",
                  font=("Segoe UI", 10, "bold" if i == 0 else ""),
                  anchor="w", padx=15, pady=12, relief="flat", bd=0,
                  command=lambda t=texto.strip(" ●▲■◆ "): accion_menu_doc(t))
    b.pack(fill="x", padx=8, pady=2)
    botones_menu_doc.append(b)

tit_doc = tk.Frame(contenido_doc, bg=BLANCO)
tit_doc.grid(row=0, column=0, sticky="ew", padx=15, pady=12)
tit_doc.columnconfigure(0, weight=1)
tk.Label(tit_doc, text="Control de Alumnos", bg=BLANCO, font=("Segoe UI", 14, "bold"),
         fg=AZUL).grid(row=0, column=0, sticky="w")
tk.Button(tit_doc, text="+ Agregar", bg=AZUL, fg=BLANCO, font=("Segoe UI", 9, "bold"),
          padx=12, pady=5, relief="flat",
          command=lambda: messagebox.showinfo("Agregar alumno", "Aquí se abrirá el formulario para agregar alumnos.")
          ).grid(row=0, column=1, sticky="e")
cols_doc = ("#", "Nombre", "Matrícula", "Asist.", "Estado")
tabla_doc = ttk.Treeview(contenido_doc, columns=cols_doc, show="headings")
for col, ancho in zip(cols_doc, [40, 260, 90, 90, 90]):
    tabla_doc.heading(col, text=col)
    tabla_doc.column(col, width=ancho, anchor="w" if col == "Nombre" else "center")
for i, fila in enumerate([
    ("01", "Sofía Hernández Ruiz", "240101", "Presente", "OK"),
    ("02", "Diego Castillo López", "240102", "Presente", "OK"),
    ("03", "Valeria Mendoza P.", "240103", "Retardo", "Revisar"),
    ("04", "Emiliano Torres G.", "240104", "Presente", "OK"),
    ("05", "Renata Juárez M.", "240105", "Ausente", "Justificar")
]):
    tabla_doc.insert("", "end", values=fila, tags=("par" if i % 2 == 0 else "impar",))
tabla_doc.tag_configure("par", background="#fff")
tabla_doc.tag_configure("impar", background="#f8fafc")
tabla_doc.grid(row=1, column=0, sticky="nsew", padx=(15, 0), pady=(0, 15))
scroll_doc = ttk.Scrollbar(contenido_doc, orient="vertical", command=tabla_doc.yview)
tabla_doc.configure(yscrollcommand=scroll_doc.set)
scroll_doc.grid(row=1, column=1, sticky="ns", pady=(0, 15), padx=(0, 15))

def ajustar_docente(event=None):
    ancho = docente.winfo_width()
    if ancho < 850:
        menu_doc.grid_configure(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=(0, 10))
        contenido_doc.grid_configure(row=1, column=0, columnspan=2, sticky="nsew")
        cuerpo_doc.rowconfigure(0, weight=0)
        cuerpo_doc.rowconfigure(1, weight=1)
        for b in botones_menu_doc:
            b.pack_forget()
            b.pack(side="left", fill="x", expand=True, padx=3, pady=4)
        for i, tarjeta in enumerate(tarjetas_kpi_doc):
            tarjeta.pack_forget()
            tarjeta.grid(row=i // 2, column=i % 2, sticky="ew", padx=4, pady=4)
        kpi_doc.columnconfigure(0, weight=1)
        kpi_doc.columnconfigure(1, weight=1)
    else:
        menu_doc.grid_configure(row=0, column=0, columnspan=1, sticky="ns", padx=(0, 10), pady=0)
        contenido_doc.grid_configure(row=0, column=1, columnspan=1, sticky="nsew")
        cuerpo_doc.rowconfigure(0, weight=1)
        cuerpo_doc.rowconfigure(1, weight=0)
        for b in botones_menu_doc:
            b.pack_forget()
            b.pack(fill="x", padx=8, pady=2)
        for tarjeta in tarjetas_kpi_doc:
            tarjeta.grid_forget()
            tarjeta.pack(side="left", fill="x", expand=True, padx=4)
docente.bind("<Configure>", lambda e: root.after_idle(ajustar_docente))

# Botones para salir/cambiar de perfil, conservando el diseño principal.
tk.Button(header_doc, text="Cerrar sesión", bg=AZUL, fg="#cbd5e1",
          activebackground=AZUL, activeforeground=BLANCO, relief="flat",
          cursor="hand2", command=lambda: mostrar("login_doc")).pack(side="right", padx=10)
tk.Button(derecha_header, text="Cerrar sesión", bg=AZUL, fg="#cbd5e1",
          activebackground=AZUL, activeforeground=BLANCO, relief="flat",
          cursor="hand2", command=lambda: mostrar("login_dir")).pack(anchor="e", pady=(2, 0))

# Inicio: aparece primero el acceso docente.
mostrar("login_doc")
root.mainloop()