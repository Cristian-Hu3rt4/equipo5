import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import json
import os

ARCHIVO = "datos_nezahualcoyotl.json"

AZUL = "#0f2c61"
DORADO = "#c9a86a"
FONDO = "#eef2f7"
BLANCO = "#ffffff"
GRIS = "#64748b"
GRIS_SUAVE = "#e2e8f0"
GRIS_MAT = "#94a3b8"
INPUT_BG = "#f8fafc"
VERDE = "#22c55e"
VERDE_H = "#16a34a"
ROJO = "#f87171"
ROJO_H = "#ef4444"
AZUL_BTN = "#60a5fa"
AZUL_BTN_H = "#3b82f6"

def datos_iniciales():
    return {
        "alumnos": [
            {"id": "240101", "nombre": "Sofia Hernandez Ruiz", "grupo": "5° B"},
            {"id": "240102", "nombre": "Diego Castillo Lopez", "grupo": "5° B"},
            {"id": "240103", "nombre": "Valeria Mendoza Perez", "grupo": "5° B"},
            {"id": "240104", "nombre": "Emiliano Torres Garcia", "grupo": "5° B"},
            {"id": "240105", "nombre": "Renata Juarez Martinez", "grupo": "5° B"},
        ],
        "docentes": [
            {"id": "D001", "nombre": "Laura Martinez", "materia": "Español", "correo": "laura@nezahualcoyotl.edu.mx"},
            {"id": "D002", "nombre": "Carlos Gomez", "materia": "Matematicas", "correo": "carlos@nezahualcoyotl.edu.mx"},
        ],
        "asistencias": {},
        "incidencias": [],
        "justificantes": [],
        "reportes": [],
        "cartas": []
    }

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return datos_iniciales()
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
        base = datos_iniciales()
        for k in base:
            datos.setdefault(k, base[k])
        return datos
    except Exception:
        messagebox.showwarning("Datos", "No se pudo leer el archivo. Se inicio una base nueva.")
        return datos_iniciales()

datos = cargar_datos()

def guardar_datos():
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except OSError as e:
        messagebox.showerror("Error al guardar", str(e))

def hoy(): return datetime.now().strftime("%Y-%m-%d")
def fecha_bonita(fecha):
    try: return datetime.strptime(fecha, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError: return fecha

root = tk.Tk()
root.title("Escuela Primaria Nezahualcoyotl | Sistema de Gestion Academica")
root.geometry("1280x720")
root.minsize(950, 620)
root.configure(bg=FONDO)
try: root.tk.call("tk", "scaling", 1.25)
except Exception: pass

style = ttk.Style()
try: style.theme_use("clam")
except tk.TclError: pass
style.configure("Treeview", font=("Segoe UI", 10), rowheight=34, background=BLANCO, fieldbackground=BLANCO, borderwidth=0)
style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#f1f5f9", foreground=AZUL, borderwidth=0)
style.configure("TCombobox", font=("Segoe UI", 10), padding=6)

pantalla_login = tk.Frame(root, bg=FONDO)
pantalla_director_login = tk.Frame(root, bg=AZUL)
aplicacion = tk.Frame(root, bg=FONDO)

def limpiar(frame):
    for w in frame.winfo_children(): w.destroy()

def titulo(parent, texto, subtitulo=""):
    tk.Label(parent, text=texto, bg=BLANCO, fg=AZUL, font=("Segoe UI", 19, "bold")).pack(anchor="w", padx=24, pady=(18, 2))
    if subtitulo:
        tk.Label(parent, text=subtitulo, bg=BLANCO, fg=GRIS, font=("Segoe UI", 10)).pack(anchor="w", padx=24)
    tk.Frame(parent, bg=GRIS_SUAVE, height=1).pack(fill="x", padx=24, pady=(10, 12))

def boton(parent, texto, comando, color=AZUL, fg=BLANCO, padx=16):
    return tk.Button(parent, text=texto, command=comando, bg=color, fg=fg, activebackground=DORADO, activeforeground=AZUL, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", padx=padx, pady=9, bd=0)

def entrada_estilo(parent, placeholder=""):
    e = tk.Entry(parent, font=("Segoe UI", 10), bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1)
    e.pack(fill="x", ipady=8)
    if placeholder: e.insert(0, placeholder)
    return e

def label_campo(parent, texto):
    tk.Label(parent, text=texto, bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10, 4))

def crear_pastilla(canvas, x1, y1, x2, y2, radio, color):
    canvas.create_rectangle(x1+radio, y1, x2-radio, y2, fill=color, outline=color)
    canvas.create_oval(x1, y1, x1+radio*2, y2, fill=color, outline=color)
    canvas.create_oval(x2-radio*2, y1, x2, y2, fill=color, outline=color)

def boton_pastilla(parent, texto, comando, color, hover, bg_padre=BLANCO):
    w, h = 122, 32
    c = tk.Canvas(parent, width=w, height=h, bg=bg_padre, highlightthickness=0, cursor="hand2")
    def pintar(col):
        c.delete("all")
        crear_pastilla(c, 1, 2, w-1, h, 15, col)
        c.create_text(w//2, h//2+1, text=texto, fill="white", font=("Segoe UI", 8, "bold"))
    pintar(color)
    c.bind("<Button-1>", lambda e: comando())
    c.bind("<Enter>", lambda e: pintar(hover))
    c.bind("<Leave>", lambda e: pintar(color))
    return c

def badge_estado(parent, estado, bg_padre=BLANCO):
    mapa = {"Presente": ("#dcfce7", "#166534", "●  Presente"), "Falta": ("#fee2e2", "#991b1b", "●  Falta"), "Justificada": ("#dbeafe", "#1e40af", "●  Justificada"), "Retardo": ("#fef3c7", "#92400e", "●  Retardo")}
    fondo, letra, texto = mapa.get(estado, ("#f1f5f9", GRIS, "○  Sin registrar"))
    w, h = 118, 28
    c = tk.Canvas(parent, width=w, height=h, bg=bg_padre, highlightthickness=0)
    crear_pastilla(c, 0, 0, w, h, 14, fondo)
    c.create_text(w//2, h//2, text=texto, fill=letra, font=("Segoe UI", 8, "bold"))
    return c

def crear_tabla(parent, columnas, anchos=None):
    marco = tk.Frame(parent, bg=BLANCO)
    marco.pack(fill="both", expand=True, padx=20, pady=10)
    tabla = ttk.Treeview(marco, columns=columnas, show="headings")
    for i, col in enumerate(columnas):
        tabla.heading(col, text=col)
        tabla.column(col, width=anchos[i] if anchos else 130, anchor="center")
    scroll = ttk.Scrollbar(marco, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scroll.set)
    tabla.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")
    return tabla

def crear_scroll(parent):
    canvas = tk.Canvas(parent, bg=BLANCO, highlightthickness=0)
    scroll = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas, bg=BLANCO)
    canvas.configure(yscrollcommand=scroll.set)
    canvas.pack(side="left", fill="both", expand=True, padx=24, pady=8)
    scroll.pack(side="right", fill="y", padx=(0, 8))
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    return frame

def cambiar_pantalla(frame):
    for f in (pantalla_login, pantalla_director_login, aplicacion):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

def entrada_login(parent, nombre, valor="", password=False):
    tk.Label(parent, text=nombre, bg=BLANCO, fg=GRIS, font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(8, 4))
    e = tk.Entry(parent, font=("Segoe UI", 11), bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1, show="*" if password else "")
    e.pack(fill="x", ipady=10); e.insert(0, valor); return e

pantalla_login.columnconfigure(0, weight=1); pantalla_login.rowconfigure(0, weight=1)
tarjeta = tk.Frame(pantalla_login, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1)
tarjeta.grid(row=0, column=0, padx=28, pady=28, sticky="nsew"); tarjeta.columnconfigure(1, weight=1)
lateral = tk.Frame(tarjeta, bg=AZUL, width=340); lateral.grid(row=0, column=0, sticky="nsew"); lateral.grid_propagate(False)
tk.Label(lateral, text="◆", bg=AZUL, fg=DORADO, font=("Segoe UI", 52, "bold")).pack(pady=(70, 10))
tk.Label(lateral, text="ESCUELA PRIMARIA\nNEZAHUALCOYOTL", bg=AZUL, fg=BLANCO, font=("Segoe UI", 17, "bold"), justify="center").pack()
tk.Label(lateral, text="Sistema de Gestion Academica", bg=AZUL, fg="#cbd5e1", font=("Segoe UI", 10)).pack(pady=15)
form_login = tk.Frame(tarjeta, bg=BLANCO); form_login.grid(row=0, column=1, sticky="nsew", padx=38, pady=38)
tk.Label(form_login, text="Bienvenido de nuevo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 22, "bold")).pack(anchor="w")
tk.Label(form_login, text="Acceso para docentes", bg=BLANCO, fg=GRIS, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 20))
usuario_doc = entrada_login(form_login, "USUARIO", "docente.lmartinez")
clave_doc = entrada_login(form_login, "CONTRASENA", "12345678", True)
def entrar_docente():
    if usuario_doc.get().strip() and clave_doc.get(): abrir_app("docente", "Listas")
    else: messagebox.showwarning("Acceso", "Completa usuario y contrasena.")
boton(form_login, "Ingresar al Sistema", entrar_docente).pack(fill="x", pady=(22, 10))
boton(form_login, "Acceso de Direccion", lambda: cambiar_pantalla(pantalla_director_login), color=BLANCO, fg=AZUL).pack(anchor="w")

caja_dir = tk.Frame(pantalla_director_login, bg=BLANCO, highlightbackground=DORADO, highlightthickness=2)
caja_dir.pack(expand=True, fill="both", padx=38, pady=38)
tk.Label(caja_dir, text="◆", bg=BLANCO, fg=DORADO, font=("Segoe UI", 32, "bold")).pack(pady=(25, 5))
tk.Label(caja_dir, text="ESCUELA NEZAHUALCOYOTL", bg=BLANCO, fg=AZUL, font=("Segoe UI", 15, "bold")).pack()
tk.Label(caja_dir, text="PANEL DIRECTIVO", bg=AZUL, fg=BLANCO, font=("Segoe UI", 9, "bold"), padx=15, pady=5).pack(pady=10)
form_dir = tk.Frame(caja_dir, bg=BLANCO); form_dir.pack(fill="x", padx=45, pady=5)
nombre_dir = entrada_login(form_dir, "NOMBRE DE USUARIO", "Dir. Alejandro Torres")
correo_dir = entrada_login(form_dir, "CORREO INSTITUCIONAL", "direccion@nezahualcoyotl.edu.mx")
clave_dir = entrada_login(form_dir, "CONTRASENA DIRECTIVA", "12345678", True)
def entrar_director():
    if nombre_dir.get().strip() and correo_dir.get().strip() and clave_dir.get(): abrir_app("director", "Resumen")
    else: messagebox.showwarning("Acceso", "Completa todos los campos.")
boton(form_dir, "Acceder como Director", entrar_director).pack(fill="x", pady=(20, 8))
boton(form_dir, "Volver al acceso docente", lambda: cambiar_pantalla(pantalla_login), color=BLANCO, fg=GRIS).pack()

encabezado = tk.Frame(aplicacion, bg=AZUL, height=72); encabezado.pack(fill="x"); encabezado.pack_propagate(False)
tk.Label(encabezado, text="◆  ESCUELA PRIMARIA NEZAHUALCOYOTL", bg=AZUL, fg=BLANCO, font=("Segoe UI", 13, "bold")).pack(side="left", padx=22)
tk.Label(encabezado, text=datetime.now().strftime("%d/%m/%Y"), bg=AZUL, fg="#cbd5e1", font=("Segoe UI", 9)).pack(side="right", padx=20)
area = tk.Frame(aplicacion, bg=FONDO); area.pack(fill="both", expand=True, padx=14, pady=14)
area.columnconfigure(1, weight=1); area.rowconfigure(0, weight=1)
menu = tk.Frame(area, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1, width=200)
menu.grid(row=0, column=0, sticky="ns", padx=(0, 12)); menu.grid_propagate(False)
contenido = tk.Frame(area, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1)
contenido.grid(row=0, column=1, sticky="nsew"); contenido.columnconfigure(0, weight=1); contenido.rowconfigure(0, weight=1)
rol_actual = "docente"

def abrir_app(rol, seccion):
    global rol_actual; rol_actual = rol; cambiar_pantalla(aplicacion); mostrar_seccion(seccion)
def cerrar_sesion():
    guardar_datos(); cambiar_pantalla(pantalla_login)
def construir_menu(seccion):
    limpiar(menu)
    tk.Label(menu, text="MENU PRINCIPAL", bg=BLANCO, fg=GRIS, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=14, pady=(16, 10))
    if rol_actual == "docente":
        opciones = [("Listas", "●  Pasar lista"), ("Alumnos", "●  Alumnos"), ("Incidencias", "●  Incidencias"), ("Justificantes", "●  Justificantes"), ("Reportes", "●  Reportes")]
    else:
        # --- MENU DEL DIRECTOR CON EL APARTADO NUEVO ---
        opciones = [("Resumen", "●  Resumen general"), ("Alumnos y Docentes", "●  Alumnos y Docentes"), ("Asistencias", "●  Asistencias"), ("Incidencias", "●  Incidencias"), ("Justificantes", "●  Justificantes"), ("Reportes", "●  Reportes"), ("Cartas", "●  Cartas compromiso")]
    for nombre, texto in opciones:
        boton(menu, texto, lambda n=nombre: mostrar_seccion(n), color=AZUL if nombre == seccion else BLANCO, fg=BLANCO if nombre == seccion else AZUL).pack(fill="x", padx=8, pady=3)
    tk.Frame(menu, bg=GRIS_SUAVE, height=1).pack(fill="x", padx=10, pady=12)
    boton(menu, "Cerrar sesion", cerrar_sesion, color="#fee2e2", fg="#991b1b").pack(fill="x", padx=8, pady=5)
def mostrar_seccion(seccion):
    construir_menu(seccion); limpiar(contenido)
    if rol_actual == "docente":
        vistas = {"Listas": vista_listas, "Alumnos": vista_alumnos, "Incidencias": vista_incidencias, "Justificantes": vista_justificantes, "Reportes": vista_reportes}
    else:
        vistas = {"Resumen": vista_resumen, "Alumnos y Docentes": vista_alumnos_docentes_director, "Asistencias": vista_asistencias_director, "Incidencias": vista_incidencias, "Justificantes": vista_justificantes, "Reportes": vista_reportes, "Cartas": vista_cartas}
    vistas.get(seccion, vista_listas)(contenido)

def fila_alumno(lista_frame, fila, matricula, nombre, extra_texto, extra_es_estado, marcar_fn, mostrar_estado=True):
    card = tk.Frame(lista_frame, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1)
    card.grid(row=fila, column=0, columnspan=6, sticky="ew", pady=6, padx=2)
    card.columnconfigure(1, weight=1)
    tk.Label(card, text=matricula, bg=BLANCO, fg=GRIS_MAT, font=("Segoe UI", 9)).grid(row=0, column=0, padx=14, pady=16, sticky="w")
    tk.Label(card, text=nombre, bg=BLANCO, fg=AZUL, font=("Segoe UI", 11, "bold"), anchor="w").grid(row=0, column=1, padx=10, pady=16, sticky="w")
    if mostrar_estado:
        badge_estado(card, extra_texto, BLANCO).grid(row=0, column=2, padx=10, pady=16)
    else:
        tk.Label(card, text=extra_texto, bg=BLANCO, fg=GRIS, font=("Segoe UI", 10)).grid(row=0, column=2, padx=10, pady=16)
    boton_pastilla(card, "✓ Asistencia", lambda: marcar_fn(matricula, "Presente"), VERDE, VERDE_H, BLANCO).grid(row=0, column=3, padx=5, pady=14)
    boton_pastilla(card, "✕ Inasistencia", lambda: marcar_fn(matricula, "Falta"), ROJO, ROJO_H, BLANCO).grid(row=0, column=4, padx=5, pady=14)
    boton_pastilla(card, "◐ Justificar", lambda: marcar_fn(matricula, "Justificada"), AZUL_BTN, AZUL_BTN_H, BLANCO).grid(row=0, column=5, padx=5, pady=14)
    return card

def vista_listas(parent):
    titulo(parent, "Control de asistencia", "Marca asistencia, inasistencia o justificante directamente en cada alumno.")
    barra = tk.Frame(parent, bg=BLANCO); barra.pack(fill="x", padx=24, pady=(0, 6))
    tk.Label(barra, text="Fecha:", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(side="left")
    fecha = tk.Entry(barra, width=13, font=("Segoe UI", 10), bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); fecha.insert(0, hoy()); fecha.pack(side="left", padx=8, ipady=6)
    tk.Label(barra, text="Grupo:", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(side="left", padx=(14, 4))
    grupo = ttk.Combobox(barra, width=10, values=["5° A", "5° B", "5° C"]); grupo.set("5° B"); grupo.pack(side="left")
    tk.Button(barra, text="↻  Actualizar", command=lambda: actualizar(), bg="#eef2f7", fg=AZUL, font=("Segoe UI", 9, "bold"), relief="flat", cursor="hand2", padx=14, pady=7).pack(side="right")
    lista_frame = crear_scroll(parent)
    def marcar(matricula, estado):
        dia = fecha.get().strip()
        try: datetime.strptime(dia, "%Y-%m-%d")
        except ValueError: messagebox.showerror("Fecha incorrecta", "Usa el formato AAAA-MM-DD."); return
        datos["asistencias"].setdefault(dia, {}); datos["asistencias"][dia][matricula] = estado; guardar_datos(); actualizar()
    def actualizar():
        for w in lista_frame.winfo_children(): w.destroy()
        lista_frame.columnconfigure(1, weight=1)
        for txt, col in [("MATRICULA", 0), ("NOMBRE DEL ALUMNO", 1), ("ESTADO", 2)]:
            tk.Label(lista_frame, text=txt, bg=BLANCO, fg=GRIS, font=("Segoe UI", 8, "bold")).grid(row=0, column=col, sticky="w", padx=10, pady=(0, 8))
        dia = fecha.get().strip(); fila = 1
        for a in datos["alumnos"]:
            if a["grupo"] != grupo.get(): continue
            estado = datos["asistencias"].get(dia, {}).get(a["id"], "Sin registrar")
            fila_alumno(lista_frame, fila, a["id"], a["nombre"], estado, True, marcar); fila += 1
    actualizar()

def vista_alumnos(parent):
    titulo(parent, "Registro de alumnos", "Agrega alumnos y controla su asistencia desde aquí.")
    lista_frame = crear_scroll(parent)
    def marcar(matricula, estado):
        dia = hoy(); datos["asistencias"].setdefault(dia, {}); datos["asistencias"][dia][matricula] = estado; guardar_datos(); actualizar(); messagebox.showinfo("Listo", f"Se registro: {estado}")
    def actualizar():
        for w in lista_frame.winfo_children(): w.destroy()
        lista_frame.columnconfigure(1, weight=1)
        for col, txt in enumerate(["MATRICULA", "NOMBRE DEL ALUMNO", "GRUPO"]):
            tk.Label(lista_frame, text=txt, bg=BLANCO, fg=GRIS, font=("Segoe UI", 8, "bold")).grid(row=0, column=col, sticky="w", padx=10, pady=(0, 8))
        for i, a in enumerate(datos["alumnos"], start=1):
            fila_alumno(lista_frame, i, a["id"], a["nombre"], a["grupo"], False, marcar, mostrar_estado=False)
    def agregar():
        v = tk.Toplevel(root); v.title("Agregar alumno"); v.geometry("380x300"); v.configure(bg=BLANCO); v.transient(root); v.grab_set()
        tk.Label(v, text="Nombre completo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20, pady=(20, 4))
        nombre = tk.Entry(v); nombre.pack(fill="x", padx=20, ipady=6)
        tk.Label(v, text="Matricula", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20, pady=(12, 4))
        matricula = tk.Entry(v); matricula.pack(fill="x", padx=20, ipady=6)
        tk.Label(v, text="Grupo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20, pady=(12, 4))
        grupo = ttk.Combobox(v, values=["5° A", "5° B", "5° C"]); grupo.set("5° B"); grupo.pack(fill="x", padx=20)
        def guardar():
            n = nombre.get().strip(); m = matricula.get().strip()
            if not n or not m: messagebox.showwarning("Datos incompletos", "Escribe nombre y matricula.", parent=v); return
            if any(a["id"] == m for a in datos["alumnos"]): messagebox.showerror("Matricula repetida", "Esa matricula ya existe.", parent=v); return
            datos["alumnos"].append({"id": m, "nombre": n, "grupo": grupo.get()}); guardar_datos(); actualizar(); v.destroy()
        boton(v, "Guardar alumno", guardar).pack(pady=18)
    boton(parent, "+ Agregar alumno", agregar).pack(anchor="w", padx=24, pady=5)
    actualizar()

# ============================================================
# APARTADO NUEVO DEL DIRECTOR - AGREGAR ALUMNOS Y DOCENTES
# ============================================================
def vista_alumnos_docentes_director(parent):
    titulo(parent, "Alumnos y Docentes", "Solo Dirección puede agregar, ver y eliminar alumnos y docentes.")
    contenedor = tk.Frame(parent, bg=BLANCO)
    contenedor.pack(fill="both", expand=True, padx=20, pady=5)
    contenedor.columnconfigure(0, weight=1)
    contenedor.columnconfigure(1, weight=1)

    # --- IZQUIERDA: ALUMNOS ---
    col_a = tk.Frame(contenedor, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1)
    col_a.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=5)
    tk.Label(col_a, text="👧  AGREGAR ALUMNO NUEVO", bg=BLANCO, fg=AZUL, font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=16, pady=(14, 4))
    tk.Label(col_a, text="Se agrega a la lista general y a Pasar Lista.", bg=BLANCO, fg=GRIS, font=("Segoe UI", 9)).pack(anchor="w", padx=16)
    form_a = tk.Frame(col_a, bg=BLANCO); form_a.pack(fill="x", padx=16, pady=8)
    tk.Label(form_a, text="Nombre completo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_nombre_a = tk.Entry(form_a, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); e_nombre_a.pack(fill="x", ipady=7, pady=(2, 8))
    tk.Label(form_a, text="Matricula", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_mat_a = tk.Entry(form_a, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); e_mat_a.pack(fill="x", ipady=7, pady=(2, 8))
    tk.Label(form_a, text="Grupo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_grupo_a = ttk.Combobox(form_a, values=["5° A", "5° B", "5° C"]); e_grupo_a.set("5° B"); e_grupo_a.pack(fill="x", pady=(2, 8))
    tabla_a = ttk.Treeview(col_a, columns=("Matricula", "Nombre", "Grupo"), show="headings", height=8)
    for c in ("Matricula", "Nombre", "Grupo"): tabla_a.heading(c, text=c)
    tabla_a.column("Matricula", width=90, anchor="center"); tabla_a.column("Nombre", width=200, anchor="w"); tabla_a.column("Grupo", width=70, anchor="center")
    tabla_a.pack(fill="both", expand=True, padx=12, pady=6)
    def actualizar_alumnos():
        tabla_a.delete(*tabla_a.get_children())
        for a in datos["alumnos"]: tabla_a.insert("", "end", values=(a["id"], a["nombre"], a["grupo"]))
    def guardar_alumno():
        n = e_nombre_a.get().strip(); m = e_mat_a.get().strip(); g = e_grupo_a.get().strip()
        if not n or not m: messagebox.showwarning("Datos incompletos", "Escribe nombre y matricula."); return
        if any(a["id"] == m for a in datos["alumnos"]): messagebox.showerror("Matricula repetida", "Esa matricula ya existe."); return
        datos["alumnos"].append({"id": m, "nombre": n, "grupo": g}); guardar_datos(); actualizar_alumnos()
        e_nombre_a.delete(0, "end"); e_mat_a.delete(0, "end")
        messagebox.showinfo("Alumno agregado", f"{n} se agrego correctamente.")
    def borrar_alumno():
        sel = tabla_a.selection()
        if not sel: messagebox.showwarning("Selecciona", "Selecciona un alumno para borrar."); return
        mat = tabla_a.item(sel[0], "values")[0]
        datos["alumnos"] = [a for a in datos["alumnos"] if a["id"] != mat]; guardar_datos(); actualizar_alumnos(); messagebox.showinfo("Eliminado", "Alumno eliminado.")
    btns_a = tk.Frame(col_a, bg=BLANCO); btns_a.pack(fill="x", padx=12, pady=(0, 12))
    boton(btns_a, "＋ Agregar Alumno", guardar_alumno, color=VERDE).pack(side="left", fill="x", expand=True, padx=(0, 4))
    boton(btns_a, "🗑 Borrar", borrar_alumno, color="#fee2e2", fg="#991b1b").pack(side="left", padx=4)

    # --- DERECHA: DOCENTES ---
    col_d = tk.Frame(contenedor, bg=BLANCO, highlightbackground=GRIS_SUAVE, highlightthickness=1)
    col_d.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=5)
    tk.Label(col_d, text="👨‍🏫  AGREGAR DOCENTE NUEVO", bg=BLANCO, fg=AZUL, font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=16, pady=(14, 4))
    tk.Label(col_d, text="Registra docentes para que aparezcan en el sistema.", bg=BLANCO, fg=GRIS, font=("Segoe UI", 9)).pack(anchor="w", padx=16)
    form_d = tk.Frame(col_d, bg=BLANCO); form_d.pack(fill="x", padx=16, pady=8)
    tk.Label(form_d, text="Nombre completo", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_nombre_d = tk.Entry(form_d, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); e_nombre_d.pack(fill="x", ipady=7, pady=(2, 8))
    tk.Label(form_d, text="Materia", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_materia_d = ttk.Combobox(form_d, values=["Español", "Matematicas", "Ciencias Naturales", "Historia", "Geografia", "Educacion Fisica", "Ingles", "Artes"]); e_materia_d.set("Matematicas"); e_materia_d.pack(fill="x", pady=(2, 8))
    tk.Label(form_d, text="Correo institucional", bg=BLANCO, fg=AZUL, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    e_correo_d = tk.Entry(form_d, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); e_correo_d.pack(fill="x", ipady=7, pady=(2, 8))
    tabla_d = ttk.Treeview(col_d, columns=("Nombre", "Materia", "Correo"), show="headings", height=8)
    for c in ("Nombre", "Materia", "Correo"): tabla_d.heading(c, text=c)
    tabla_d.column("Nombre", width=160, anchor="w"); tabla_d.column("Materia", width=110, anchor="center"); tabla_d.column("Correo", width=180, anchor="w")
    tabla_d.pack(fill="both", expand=True, padx=12, pady=6)
    def actualizar_docentes():
        tabla_d.delete(*tabla_d.get_children())
        for d in datos.get("docentes", []): tabla_d.insert("", "end", values=(d["nombre"], d["materia"], d["correo"]))
    def guardar_docente():
        n = e_nombre_d.get().strip(); mat = e_materia_d.get().strip(); cor = e_correo_d.get().strip()
        if not n or not mat: messagebox.showwarning("Datos incompletos", "Escribe nombre y materia."); return
        nuevo_id = f"D{len(datos.get('docentes', []))+1:03d}"
        datos.setdefault("docentes", []).append({"id": nuevo_id, "nombre": n, "materia": mat, "correo": cor}); guardar_datos(); actualizar_docentes()
        e_nombre_d.delete(0, "end"); e_correo_d.delete(0, "end")
        messagebox.showinfo("Docente agregado", f"{n} se agrego correctamente.")
    def borrar_docente():
        sel = tabla_d.selection()
        if not sel: messagebox.showwarning("Selecciona", "Selecciona un docente para borrar."); return
        nombre_borrar = tabla_d.item(sel[0], "values")[0]
        datos["docentes"] = [d for d in datos.get("docentes", []) if d["nombre"] != nombre_borrar]; guardar_datos(); actualizar_docentes(); messagebox.showinfo("Eliminado", "Docente eliminado.")
    btns_d = tk.Frame(col_d, bg=BLANCO); btns_d.pack(fill="x", padx=12, pady=(0, 12))
    boton(btns_d, "＋ Agregar Docente", guardar_docente, color=AZUL_BTN).pack(side="left", fill="x", expand=True, padx=(0, 4))
    boton(btns_d, "🗑 Borrar", borrar_docente, color="#fee2e2", fg="#991b1b").pack(side="left", padx=4)
    actualizar_alumnos(); actualizar_docentes()

def vista_incidencias(parent):
    titulo(parent, "Registro de incidencias", "Registra conductas, retardos o conflictos y consúltalos abajo.")
    form = tk.Frame(parent, bg=BLANCO); form.pack(fill="x", padx=24)
    label_campo(form, "Alumno / matricula")
    alumno = ttk.Combobox(form, width=40, values=[a["id"] + " - " + a["nombre"] for a in datos["alumnos"]]); alumno.pack(fill="x", ipady=4)
    label_campo(form, "Tipo de incidencia")
    tipo = ttk.Combobox(form, values=["Conducta", "Retardo", "Falta", "Conflicto", "Academica", "Otra"], state="readonly"); tipo.set("Conducta"); tipo.pack(fill="x", ipady=4)
    label_campo(form, "Descripcion")
    desc = tk.Text(form, height=3, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); desc.pack(fill="x", pady=2)
    def guardar():
        sel = alumno.get().strip(); d = desc.get("1.0", "end").strip()
        if not sel or not d: messagebox.showwarning("Datos incompletos", "Selecciona un alumno y escribe la descripcion."); return
        datos["incidencias"].append({"fecha": hoy(), "matricula": sel.split(" - ", 1)[0], "alumno": sel, "tipo": tipo.get(), "descripcion": d}); guardar_datos(); desc.delete("1.0", "end"); actualizar(); messagebox.showinfo("Incidencia guardada", "El registro se guardo correctamente.")
    boton(form, "Guardar incidencia", guardar).pack(anchor="e", pady=12)
    tabla = crear_tabla(parent, ("Fecha", "Alumno", "Tipo", "Descripcion"), [100, 210, 110, 350])
    def actualizar():
        tabla.delete(*tabla.get_children())
        for r in reversed(datos["incidencias"]): tabla.insert("", "end", values=(fecha_bonita(r["fecha"]), r["alumno"], r["tipo"], r["descripcion"]))
    actualizar()

def vista_justificantes(parent):
    titulo(parent, "Justificantes de faltas", "Al guardar, la falta pasa automáticamente a Justificada.")
    form = tk.Frame(parent, bg=BLANCO); form.pack(fill="x", padx=24)
    label_campo(form, "Matricula"); matricula = entrada_estilo(form)
    label_campo(form, "Fecha de la falta (AAAA-MM-DD)"); fecha = entrada_estilo(form, hoy())
    label_campo(form, "Motivo"); motivo = tk.Text(form, height=3, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); motivo.pack(fill="x")
    tabla = crear_tabla(parent, ("Registro", "Matricula", "Fecha de falta", "Motivo"), [90, 120, 150, 350])
    def actualizar():
        tabla.delete(*tabla.get_children())
        for i, r in enumerate(reversed(datos["justificantes"]), 1): tabla.insert("", "end", values=(i, r["matricula"], fecha_bonita(r["fecha"]), r["motivo"]))
    def guardar():
        m = matricula.get().strip(); f = fecha.get().strip(); mot = motivo.get("1.0", "end").strip()
        if not any(a["id"] == m for a in datos["alumnos"]): messagebox.showwarning("Matricula", "Escribe una matricula que exista."); return
        try: datetime.strptime(f, "%Y-%m-%d")
        except ValueError: messagebox.showerror("Fecha", "Usa el formato AAAA-MM-DD."); return
        if not mot: messagebox.showwarning("Motivo", "Escribe el motivo."); return
        datos["justificantes"].append({"matricula": m, "fecha": f, "motivo": mot})
        if f in datos["asistencias"] and m in datos["asistencias"][f]: datos["asistencias"][f][m] = "Justificada"
        guardar_datos(); motivo.delete("1.0", "end"); actualizar(); messagebox.showinfo("Justificante", "Justificante registrado correctamente.")
    boton(form, "Guardar justificante", guardar).pack(anchor="e", pady=12)
    actualizar()

def vista_reportes(parent):
    titulo(parent, "Reportes escolares", "Crea reportes y expórtalos a TXT para imprimir.")
    form = tk.Frame(parent, bg=BLANCO); form.pack(fill="x", padx=24)
    label_campo(form, "Titulo del reporte"); titulo_reporte = entrada_estilo(form)
    label_campo(form, "Contenido"); contenido_reporte = tk.Text(form, height=4, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); contenido_reporte.pack(fill="x")
    tabla = crear_tabla(parent, ("Fecha", "Titulo", "Responsable", "Contenido"), [100, 200, 130, 350])
    def actualizar():
        tabla.delete(*tabla.get_children())
        for r in reversed(datos["reportes"]): tabla.insert("", "end", values=(fecha_bonita(r["fecha"]), r["titulo"], r["responsable"], r["contenido"]))
    def crear():
        t = titulo_reporte.get().strip(); c = contenido_reporte.get("1.0", "end").strip()
        if not t or not c: messagebox.showwarning("Reporte", "Escribe titulo y contenido."); return
        datos["reportes"].append({"fecha": hoy(), "titulo": t, "responsable": "Direccion" if rol_actual == "director" else "Docente", "contenido": c}); guardar_datos(); titulo_reporte.delete(0, "end"); contenido_reporte.delete("1.0", "end"); actualizar(); messagebox.showinfo("Reporte", "Reporte guardado correctamente.")
    botones = tk.Frame(form, bg=BLANCO); botones.pack(fill="x", pady=10)
    boton(botones, "Guardar reporte", crear).pack(side="left")
    def exportar():
        sel = tabla.selection()
        if sel:
            v = tabla.item(sel[0], "values"); texto = f"REPORTE ESCOLAR\nEscuela Primaria Nezahualcoyotl\n\nFecha: {v[0]}\nTitulo: {v[1]}\nResponsable: {v[2]}\n\n{v[3]}\n"
        else:
            texto = "REPORTES ESCOLARES\n\n" + "".join([f"Fecha: {r['fecha']}\nTitulo: {r['titulo']}\nResponsable: {r['responsable']}\n{r['contenido']}\n\n" + "-"*40 + "\n" for r in datos["reportes"]])
        ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")], title="Guardar reporte")
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f: f.write(texto)
            messagebox.showinfo("Exportacion", "Reporte exportado.")
    boton(botones, "Exportar reporte", exportar, color="#eef2f7", fg=AZUL).pack(side="left", padx=8)
    actualizar()

def vista_resumen(parent):
    titulo(parent, "Resumen general de Direccion", "Vista rápida de asistencia, incidencias y reportes de hoy.")
    total = len(datos["alumnos"])
    presentes = sum(1 for a in datos["alumnos"] if datos["asistencias"].get(hoy(), {}).get(a["id"]) in ("Presente", "Retardo"))
    porcentaje = round(presentes * 100 / total) if total else 0
    tarjetas = tk.Frame(parent, bg=BLANCO); tarjetas.pack(fill="x", padx=18, pady=10)
    for nombre, valor, color in [("ALUMNOS REGISTRADOS", str(total), AZUL), ("DOCENTES", str(len(datos.get("docentes", []))), AZUL_BTN), ("ASISTENCIAS DE HOY", f"{porcentaje}%", "#16a34a"), ("INCIDENCIAS", str(len(datos["incidencias"])), "#dc2626"), ("REPORTES", str(len(datos["reportes"])), DORADO)]:
        c = tk.Frame(tarjetas, bg="#f8fafc", highlightbackground=GRIS_SUAVE, highlightthickness=1); c.pack(side="left", fill="both", expand=True, padx=5)
        tk.Frame(c, bg=color, height=4).pack(fill="x")
        tk.Label(c, text=nombre, bg="#f8fafc", fg=GRIS, font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(c, text=valor, bg="#f8fafc", fg=AZUL, font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=10, pady=(0, 10))
    tk.Label(parent, text="Asistencia de hoy por estado", bg=BLANCO, fg=AZUL, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=20, pady=(12, 0))
    grafica = tk.Canvas(parent, bg=BLANCO, height=240, highlightthickness=0); grafica.pack(fill="x", padx=20, pady=10)
    estados = ["Presente", "Retardo", "Falta", "Justificada"]; colores = ["#16a34a", "#d97706", "#dc2626", "#2563eb"]
    registros = datos["asistencias"].get(hoy(), {}); conteos = [sum(1 for v in registros.values() if v == e) for e in estados]; maximo = max(conteos + [1])
    def dibujar(event=None):
        grafica.delete("all"); ancho = max(grafica.winfo_width(), 400); grafica.create_line(35, 190, ancho-15, 190, fill="#cbd5e1"); espacio = (ancho-70)/len(estados)
        for i, estado in enumerate(estados):
            x = 40 + i*espacio; alto = conteos[i]/maximo*125
            grafica.create_rectangle(x+10, 185-alto, x+espacio-15, 185, fill=colores[i], outline="")
            grafica.create_text(x+espacio/2, 175-alto, text=str(conteos[i]), fill=AZUL, font=("Segoe UI", 10, "bold"))
            grafica.create_text(x+espacio/2, 205, text=estado, fill=GRIS, font=("Segoe UI", 8))
    grafica.bind("<Configure>", dibujar); dibujar()
    tk.Label(parent, text="Los datos de la grafica se calculan con la asistencia registrada para hoy.", bg=BLANCO, fg=GRIS, font=("Segoe UI", 9)).pack(anchor="w", padx=20, pady=5)
    boton(parent, "Ver reportes realizados", lambda: mostrar_seccion("Reportes")).pack(anchor="w", padx=20, pady=8)

def vista_asistencias_director(parent):
    titulo(parent, "Consulta global de asistencias", "Consulta el estado de todos los alumnos por fecha.")
    barra = tk.Frame(parent, bg=BLANCO); barra.pack(fill="x", padx=24)
    tk.Label(barra, text="Fecha (AAAA-MM-DD):", bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).pack(side="left")
    fecha = tk.Entry(barra, width=14, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1); fecha.insert(0, hoy()); fecha.pack(side="left", padx=8, ipady=6)
    tabla = crear_tabla(parent, ("Matricula", "Alumno", "Grupo", "Estado"), [110, 300, 100, 150])
    def actualizar():
        tabla.delete(*tabla.get_children()); dia = fecha.get().strip(); regs = datos["asistencias"].get(dia, {})
        for a in datos["alumnos"]: tabla.insert("", "end", values=(a["id"], a["nombre"], a["grupo"], regs.get(a["id"], "Sin registrar")))
    boton(barra, "Consultar", actualizar).pack(side="left", padx=8)
    actualizar()

def vista_cartas(parent):
    titulo(parent, "Crear carta compromiso", "Llena los datos y se genera el archivo para imprimir.")
    form = tk.Frame(parent, bg=BLANCO); form.pack(fill="x", padx=24, pady=5)
    campos = {}
    for i, (nombre, txt) in enumerate([("alumno", "Nombre del alumno"), ("tutor", "Nombre del padre, madre o tutor"), ("grupo", "Grupo"), ("motivo", "Motivo de la carta")]):
        tk.Label(form, text=txt, bg=BLANCO, fg=AZUL, font=("Segoe UI", 10, "bold")).grid(row=i, column=0, sticky="w", pady=7)
        campo = tk.Text(form, height=4, width=40, bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1) if nombre == "motivo" else tk.Entry(form, font=("Segoe UI", 10), bg=INPUT_BG, relief="flat", highlightbackground="#cbd5e1", highlightthickness=1)
        campo.grid(row=i, column=1, sticky="ew", padx=10, pady=5); campos[nombre] = campo
    form.columnconfigure(1, weight=1)
    def valor(n):
        c = campos[n]; return c.get("1.0", "end").strip() if n == "motivo" else c.get().strip()
    def crear():
        alumno, tutor, grupo, motivo = valor("alumno"), valor("tutor"), valor("grupo"), valor("motivo")
        if not all([alumno, tutor, grupo, motivo]): messagebox.showwarning("Carta compromiso", "Completa todos los campos."); return
        texto = f"ESCUELA PRIMARIA NEZAHUALCOYOTL\nCARTA COMPROMISO\n\nFecha: {fecha_bonita(hoy())}\n\nAlumno(a): {alumno}\nPadre, madre o tutor: {tutor}\nGrupo: {grupo}\n\nMOTIVO Y ACUERDOS\n{motivo}\n\nPor medio de la presente, la familia y el alumno se comprometen a dar seguimiento a los acuerdos establecidos y mantener comunicacion con la escuela.\n\nFirma del padre, madre o tutor: ____________________\n\nFirma del alumno(a): _______________________________\n\nFirma de Direccion: ________________________________\n\nSello de la escuela: ________________________________\n"
        datos["cartas"].append({"fecha": hoy(), "alumno": alumno, "tutor": tutor, "grupo": grupo, "motivo": motivo, "texto": texto}); guardar_datos()
        ruta = filedialog.asksaveasfilename(title="Guardar carta compromiso", defaultextension=".txt", initialfile="carta_compromiso.txt", filetypes=[("Archivo de texto", "*.txt")])
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f: f.write(texto)
            messagebox.showinfo("Carta creada", "La carta se guardo correctamente.\nPuedes abrir el archivo e imprimirlo.")
        else: messagebox.showinfo("Carta guardada", "La carta quedo registrada en el sistema.")
        actualizar()
    boton(form, "Crear y guardar carta", crear).grid(row=4, column=1, sticky="e", pady=12)
    tk.Label(parent, text="Cartas registradas", bg=BLANCO, fg=AZUL, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=24, pady=(10, 0))
    tabla = crear_tabla(parent, ("Fecha", "Alumno", "Tutor", "Grupo", "Motivo"), [100, 180, 180, 80, 250])
    def actualizar():
        tabla.delete(*tabla.get_children())
        for c in reversed(datos["cartas"]): tabla.insert("", "end", values=(fecha_bonita(c["fecha"]), c["alumno"], c["tutor"], c["grupo"], c["motivo"]))
    actualizar()

cambiar_pantalla(pantalla_login)
root.mainloop()