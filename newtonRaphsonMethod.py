import math
from tkinter import messagebox
from sympy import Symbol
import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import END, ttk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from sympy.solvers import solve
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

# CREACION DE LA VENTANA PRINCIPAL--------------------------------
ventana = tk.Tk()
ventana.title("Newton-Raphson")
ventana.geometry("550x500")
ventana['bg'] = 'white'
# ----------------------------------------------------------------

# ÁREA DE MENUS---------------------------------------------------


def ejemplo1():
    txtxf1.delete(0, END)
    txtxf1.insert(0, "x**2+y**2-1")
    txf2.delete(0, END)
    txf2.insert(0, "y-x**2")
    tolerancia.set("0.00000000001")
    x0.set("1")
    y0.set("1")
    iteraciones.set("15")


def ejemplo2():
    txtxf1.delete(0, END)
    txtxf1.insert(0, "x+y")
    txf2.delete(0, END)
    txf2.insert(0, "x-y-8")
    tolerancia.set("0.00000001")
    x0.set("2.66")
    y0.set("0.18")
    iteraciones.set("10")


def ejemplo3():
    txtxf1.delete(0, END)
    txtxf1.insert(0, "x**3+y**3-1")
    txf2.delete(0, END)
    txf2.insert(0, "y-x**3")
    tolerancia.set("0.0000000000000001")
    x0.set("5")
    y0.set("5")
    iteraciones.set("25")


def ejemplo4():
    txtxf1.delete(0, END)
    txtxf1.insert(0, "sin(x)-(3*x/y)+1")
    txf2.delete(0, END)
    txf2.insert(0, "cos(y)-(5*x**2)*(y**2)+y")
    tolerancia.set("0.00000001")
    x0.set("1")
    y0.set("1")
    iteraciones.set("10")


barra_menus = tk.Menu()

# Crear el primer menú.
menu_ejemplo = tk.Menu(barra_menus, tearoff=False)

# Se agregan a la barra.
menu_ejemplo.add_command(label="Ejemplo 1", command=ejemplo1)
menu_ejemplo.add_command(label="Ejemplo 2", command=ejemplo2)
menu_ejemplo.add_command(label="Ejemplo 3", command=ejemplo3)
menu_ejemplo.add_command(label="Ejemplo 4", command=ejemplo4)

barra_menus.add_cascade(menu=menu_ejemplo, label="Ejemplos")
ventana.config(menu=barra_menus)
# ----------------------------------------------------------------

# AREA DE PESTAÑAS------------------------------------------------
# Incluimos el panel
pestana = ttk.Notebook(ventana)
pestana.pack(fill="both", expand="yes")

# Creamos pestanas
PGrafica = ttk.Frame(pestana)
marco = tk.LabelFrame(ventana, text="Newton-Raphson", bg="white")
marco.place(x=50, y=10, width=550, height=450)

# Agregamos las pestanas
pestana.add(marco, text="Calculadora")
pestana.add(PGrafica, text="Gráfica")
# ----------------------------------------------------------------

# FUNCION PARA BORRAR LOS DATOS DE LOS ENTRY Y TEXTO DE RESULTADOS


def borrarTodo(plot1, canvas):
    txtxf1.delete(0, tk.END)
    txf2.delete(0, tk.END)
    x0.set(0)
    y0.set(0)
    tolerancia.set(0)
    iteraciones.set(0)
    plot1.clear()
    canvas.draw()
    canvas.get_tk_widget().pack()
    resultado.configure(text="")
    resultado2.configure(text="")
# ----------------------------------------------------------------

# FUNCION PARA GRAFICAR-------------------------------------------


def graficar(f1, f2, px, py, plot1, canvas, xy0):
    # Limpiamos graficos anteriores
    plot1.clear()
    # Obtenemos las coordenadas del punto incial
    xinicial = xy0[0]
    yinicial = xy0[1]

    # Espacio de valores para los ejes
    ejes = np.linspace(0, 0, 5000)

    x = np.linspace(-20, 20, 5000)
    y = np.linspace(-20,20, 5000)
    sin = np.sin
    cos = np.cos
    sqrt = np.sqrt
    I = np.imag

    # Funciones de los ejes
    eje = x

    # Establecemos un simbolo
    xSymbol = Symbol('x')

    #Creamos listas donde guardaremos variables
    solucionesf1=list()
    solucionesf2=list()
    #hacemos una variable que guarde en string todas las soluciones
    nSolucionesF1=len(solve(f1,xSymbol))
    nSolucionesF2=len(solve(f1,xSymbol))


    #PARA LA FUNCION 1
    for i in range(nSolucionesF1):
        solucionesString=str(solve(f1,xSymbol))
        solucionesString=solucionesString.split(',')
        #Caso cuando solo hay una solucion, que elimine el corchete de inicio y final
        if (nSolucionesF1==1):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[1:]#no tocar
            solucionesString=solucionesString[:-1]#no tocar
            solucionesf1.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y llegue al ultimo elemento de la lista
        #Que elimine el ultimo corchete
        elif (nSolucionesF1!=1 and i==nSolucionesF1-1):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[:-1]#no tocar
            solucionesf1.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y entre al primer elemento de la lista
        #Que elimine el primer corchete
        elif(nSolucionesF1!=1 and i==0):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[1:]#no tocar
            solucionesf1.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y no sea el primer elemento de la lista o el ultimo
        #Que elimine el primer corchete  
        elif(nSolucionesF1!=1 and i!=0 and i!=nSolucionesF1-1):
            solucionesString=solucionesString[i]#no tocar
            solucionesf1.append(solucionesString)
    

    #Graficamos
    for i in range(nSolucionesF1):
        if(i==0):
            plot1.plot(eval(solucionesf1[0]),y,color="purple",label="f2")
        else:
            plot1.plot(eval(solucionesf1[1]),y,color="purple")


    #PARA LA FUNCION 2
    for i in range(nSolucionesF2):
        solucionesString=str(solve(f2,xSymbol))
        solucionesString=solucionesString.split(',')
        #Caso cuando solo hay una solucion, que elimine el corchete de inicio y final
        if (nSolucionesF2==1):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[1:]#no tocar
            solucionesString=solucionesString[:-1]#no tocar
            solucionesf2.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y llegue al ultimo elemento de la lista
        #Que elimine el ultimo corchete
        elif (nSolucionesF2!=1 and i==nSolucionesF2-1):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[:-1]#no tocar
            solucionesf2.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y entre al primer elemento de la lista
        #Que elimine el primer corchete
        elif(nSolucionesF2!=1 and i==0):
            solucionesString=solucionesString[i]
            solucionesString=solucionesString[1:]#no tocar
            solucionesf2.append(solucionesString)
        #Caso cuando haya mas de 2 soluciones y no sea el primer elemento de la lista o el ultimo
        #Que elimine el primer corchete  
        elif(nSolucionesF2!=1 and i!=0 and i!=nSolucionesF2-1):
            solucionesString=solucionesString[i]#no tocar
            solucionesf2.append(solucionesString)

    #Graficamos
    for i in range(nSolucionesF2):
        if(i==0):
            plot1.plot(eval(solucionesf2[0]),y,color="orange",label="f2")
        else:
            plot1.plot(eval(solucionesf2[1]),y,color="orange")


    # Graficamos el punto solucion
    plot1.plot(px, py, marker="o", color="blue", label="Punto solución")
    # Grafiquemos el punto inicial
    plot1.plot(xinicial, yinicial, marker="o",color="red", label="Punto inicial")
    # Graficamos los ejes
    plot1.plot(ejes, eje, color="green", label="Ejes X,Y")
    plot1.plot(eje, ejes, color="green")

    plot1.legend(loc='lower right')
    # Añadimos cuadricula
    plot1.set_xlim(-10, 10)
    plot1.set_ylim(-10, 10)

    plot1.grid()

    canvas.draw()
    canvas.get_tk_widget().pack()
# ----------------------------------------------------------------

# FUNCION PARA OBTENER LOS DATOS DE LOS ENTRY---------------------


def obtenerDatos(f1, f2, tolerancia, x0, y0, iteraciones):
    f1Obtenida = f1.get()
    f2Obtenida = f2.get()
    toleranciaObtenida = tolerancia.get()
    x0Obtenida = x0.get()
    y0Obtenida = y0.get()
    iteracionesObtenida = iteraciones.get()

    newton_raphson2(f1Obtenida, f2Obtenida, toleranciaObtenida,
                    (x0Obtenida, y0Obtenida), iteracionesObtenida)
# ----------------------------------------------------------------

# VALIDACION DE LOS ENTRY-----------------------------------------


def validacion(f1, f2, tolerancia, x0, y0, iteraciones):
    funcion1 = f1.get()
    funcion2 = f2.get()
    msg = ''

    if (len(funcion1) or len(funcion2)) == 0:
        msg = 'No se puede realizar el calculo si no hay funciones'
        messagebox.showinfo('message', msg)
    else:
        obtenerDatos(f1, f2, tolerancia, x0, y0, iteraciones)
# ----------------------------------------------------------------

# FUNCION PARA LIMPIAR LOS DATOS DE LA TABLA----------------------


def vaciar_tabla():

    filas = tbDatos.get_children()

    for fila in filas:
        tbDatos.delete(fila)
# ----------------------------------------------------------------

# FUNCION QUE REALIZA EL METODO NEWTON-RAPHSON--------------------


def newton_raphson2(f1, f2, tolerancia, xy0, iteraciones):
    # Limpiamos datos de tablas pasadas
    vaciar_tabla()
    funcion1 = f1
    funcion2 = f2

    # Definimos las variables
    x, y = sp.symbols('x y')

    df1 = sp.diff(f1, x)
    df2 = sp.diff(f1, y)
    df3 = sp.diff(f2, x)
    df4 = sp.diff(f2, y)

    # Transformamos las funciones a lambda para evaluarla
    f1 = sp.lambdify((x, y), f1)
    f2 = sp.lambdify((x, y), f2)

    df1 = sp.lambdify([x, y], df1)
    df2 = sp.lambdify([x, y], df2)
    df3 = sp.lambdify([x, y], df3)
    df4 = sp.lambdify([x, y], df4)

    # Asignamos el punto inicial
    xyi = xy0

    for i in range(iteraciones):

        xi, yi = xyi

        # Evaluamos el punto en la iteracion i
        f_1i = f1(xi, yi)
        f_2i = f2(xi, yi)
        f_i = np.array([f_1i, f_2i])

        df1_i = df1(xi, yi)
        df2_i = df2(xi, yi)
        df3_i = df3(xi, yi)
        df4_i = df4(xi, yi)

        # Calculamos el jacobiano evaluado en el punto xi
        jacobian = np.array([[df1_i, df2_i], [df3_i, df4_i]])

        # Calculamos el siguiente punto
        dx = np.linalg.solve(jacobian, f_i)
        xyi = xyi - dx

        err = math.sqrt(np.dot(dx, dx)) < tolerancia * max(max(abs(xyi)), 1.0)

        tbDatos.insert('', 'end', i, text='', values=(i, xyi, err, f_i, dx))
        resultado.configure(text="")
        resultado2.configure(text="")
        resultado.configure(text=xyi[0], state="normal")
        resultado2.configure(text=xyi[1], state="normal")
        px = xyi[0]
        py = xyi[1]

        # Evaluamos si es necesario continuar las iteraciones tomando en cuenta la tolerancia
        if err:
            # Mandamos a graficar
            graficar(funcion1, funcion2, px, py, plot1, canvas, xy0)
            return xyi
# ----------------------------------------------------------------


f1 = tk.StringVar()

lblf1 = tk.Label(marco, text="Función 1", bg="white").grid(column=0, row=0)
txtxf1 = tk.Entry(marco, textvariable=f1)
txtxf1.grid(column=1, row=0)

f2 = tk.StringVar()

lblf2 = tk.Label(marco, text="Función 2", bg="white").grid(column=5, row=0)
txf2 = tk.Entry(marco, textvariable=f2)
txf2.grid(column=6, row=0)

tolerancia = tk.DoubleVar()

lbltol = tk.Label(marco, text="Tolerancia", bg="white").grid(column=0, row=2)
txtrol = tk.Entry(marco, textvariable=tolerancia)
txtrol.grid(column=1, row=2)

x0 = tk.DoubleVar()

lblx0 = tk.Label(marco, text="x0", bg="white").grid(column=5, row=2)
txtx0 = tk.Entry(marco, textvariable=x0)
txtx0.grid(column=6, row=2)

y0 = tk.DoubleVar()

lbly0 = tk.Label(marco, text="y0", bg="white").grid(column=0, row=3)
txty0 = tk.Entry(marco, textvariable=y0)
txty0.grid(column=1, row=3)

iteraciones = tk.IntVar()

lbliter = tk.Label(marco, text="Iteraciones", bg="white").grid(column=5, row=3)
txtiter = tk.Entry(marco, textvariable=iteraciones)
txtiter.grid(column=6, row=3)


# La tabla de resultados

tbDatos = ttk.Treeview(marco)
tbDatos.grid(column=0, row=5, columnspan=10, padx=20, pady=10)
tbDatos["columns"] = ("Iteraciones", "x(i+1) = xi + δ", "error", "f(xi)", "δ")
tbDatos.column("#0", width=0, stretch="no")
tbDatos.column("Iteraciones", width=100, anchor="center")
tbDatos.column("x(i+1) = xi + δ", width=100, anchor="center")
tbDatos.column("error", width=100, anchor="center")
tbDatos.column("f(xi)", width=100, anchor="center")
tbDatos.column("δ", width=100, anchor="center")

tbDatos.heading("#0", text="")
tbDatos.heading("Iteraciones", text="Iteraciones", anchor="center")
tbDatos.heading("x(i+1) = xi + δ", text="x(i+1) = xi + δ", anchor="center")
tbDatos.heading("error", text="|x(i+1) - x(i)|", anchor="center")
tbDatos.heading("f(xi)", text="f(xi)", anchor="center")
tbDatos.heading("δ", text="δ", anchor="center")

txtResultado = tk.Label(
    marco, text="El resultado aproximado es:", bg="white").grid(column=0, row=6)

txtX = tk.Label(marco, text="X:", bg="white").grid(column=0, row=7)
resultado = tk.Label(marco, text="", bg="white")
resultado.grid(column=1, row=7)

txtY = tk.Label(marco, text="Y:", bg="white").grid(column=0, row=8)
resultado2 = tk.Label(marco, text="", bg="white")
resultado2.grid(column=1, row=8)

# Puntos para graficar
fig = Figure()
plot1 = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=PGrafica)
toolbar = NavigationToolbar2Tk(canvas, PGrafica)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
px = 0
py = 0

# Creamos el boton para calcular el resultado
btnCalcular = tk.Button(marco, text="Calcular", command=lambda: validacion(f1, f2, tolerancia, x0, y0, iteraciones), padx=15, bg="#A5F4F2", border=0)
btnCalcular.grid(column=1, row=4)

# Boton borrar todo
btnCalcular = tk.Button(marco, text="Borrar", command=lambda: borrarTodo(plot1, canvas), padx=15, bg="#F9AB89", border=0)
btnCalcular.grid(column=6, row=4)

ventana.mainloop()
