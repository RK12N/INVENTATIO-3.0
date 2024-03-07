
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
import tkinter as tk
import mysql.connector
from tkinter import ttk
import pymysql
import os

pnt =Tk()
pnt.title("Registro de inventario de Tv")
#pnt.resizable(0,0)
wtotal = pnt.winfo_screenwidth()
htotal = pnt.winfo_screenheight()
wventana = 1100
hventana = 550
#pnt.config(background="LightSteelBlue1") 

connectio = pymysql.connect(
    host='localhost',
    user='root',
    password='basededatos',
    db='TELEVISIONES'
)

def validate_entry(text):
    return text.isdecimal()

def resize(event):
    if Btn_ingreso_de_datos.winfo_exists():
        Btn_ingreso_de_datos.place(relx=0.01,rely=0.45,relwidth=0.2,relheight=0.1)

    if Btn_Busqueda_de_datos.winfo_exists():
        Btn_Busqueda_de_datos.place(relx=0.40,rely=0.45,relwidth=0.2,relheight=0.1)

    if Btn_Actualizacion_de_datos.winfo_exists():
        Btn_Actualizacion_de_datos.place(relx=0.78,rely=0.45,relwidth=0.2,relheight=0.1)

pnt.bind("<Configure>",resize)

ID_SERIE = StringVar()
MARCA = StringVar()
MODELO = StringVar()
TECNOLOGIA = StringVar()
PULGADAS = StringVar()
RESOLUCION = StringVar()
SMART_TV = StringVar()
ROKU = StringVar()
CANTIDAD = StringVar()
PRECIO = StringVar()
PRECIO_VENTA = StringVar()
ID = StringVar()
CATEGORIA = StringVar()

class Ventana_ingreso_de_datos:
    
    def Ingresar_datos_a_mysql():
        if (ID_SERIE.get() =="" or MARCA.get() =="" or  MODELO.get()=="" 
            or TECNOLOGIA.get()=="" or PULGADAS.get()=="" or 
            RESOLUCION.get()=="" or SMART_TV.get()=="" or ROKU.get()=="" 
            or CANTIDAD.get()=="" or PRECIO.get()=="" or CATEGORIA.get()==""):
            messagebox.showinfo(message="Existen espacios vacios")
        else:
            cursor = connectio.cursor()
            A =float(PRECIO.get())
            b =A + 700
            cantidad_tv= float(CANTIDAD.get())
            precio_tv = float(PRECIO.get())
            total = cantidad_tv * precio_tv
            sql ="insert into INVENTARIOTV(ID_SERIE,MARCA,MODELO,TECNOLOGIA,PULGADAS,RESOLUCION,SMART_TV,ROKU,CANTIDAD,PRECIO,PRECIO_DE_VENTA,VALOR_TOTAL_MERCANCIA,CATEGORIA) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("SNTV00" + ID_SERIE.get(),MARCA.get(),MODELO.get(),TECNOLOGIA.get(),PULGADAS.get(),RESOLUCION.get(),SMART_TV.get(),ROKU.get(),CANTIDAD.get(),PRECIO.get(),b,total,CATEGORIA.get())
            cursor.execute(sql)
            connectio.commit()
            messagebox.showinfo(message="Elementos enviados",title="Estado de ingreso de datos")
            Ventana_ingreso_de_datos.limpiar(set)
            
    #eliminador de la infomacion dentro de los entry
    def limpiar(str):
        ID_SERIE_ENTRY.delete(0,END)
        MARCA_C.delete(0,END)
        MODELO_ENTRY.delete(0,END)
        TECNOLOGIA_BOX.delete(0,END)
        PULGADAS_ENTRY.delete(0,END)
        RESOLUCION_BOX.delete(0,END)
        SMART_TV_BOX.delete(0,END)
        ROKU_BOX.delete(0,END)
        CANTIDAD_ENTRY.delete(0,END)
        PRECIO_ENTRY.delete(0,END)
        CATEGORIA_BOX.delete(0,END)
        pass
    
    def ventana_de_ingreso():
        #pnt.config(background="LightSteelBlue1") 
        menu.Eliminar_botones()
        global LABEL_ID_SERIE
        global LABEL_MARCA
        global LABEL_MODELO
        global LABEL_TECNOLOGIA
        global LABEL_PULGADAS
        global LABEL_RESOLUCION
        global LABEL_SMART_TV
        global LABEL_ROKU
        global LABEL_CANTIDAD
        global LABEL_PRECIO
        global LABEL_CATEGORIA
        
        LABEL_ID_SERIE = Label(pnt,text="ID_SERIE: ",font=('Bahnschrift',10))
        #LABEL_ID_SERIE.place(x=50,y=30)
        LABEL_ID_SERIE.place(relx=0.035,rely=0.030,relwidth=0.060,relheight=0.040)

        LABEL_MARCA = Label(pnt,text="MARCA: ",font=('Bahnschrift',10))
        #LABEL_MARCA.place(x=50,y=90)
        LABEL_MARCA.place(relx=0.035,rely=0.120,relwidth=0.060,relheight=0.040)

        LABEL_MODELO = Label(pnt,text="MODELO: ",font=('Bahnschrift',10))
        #LABEL_MODELO.place(x=300,y=90)
        LABEL_MODELO.place(relx=0.320,rely=0.120,relwidth=0.060,relheight=0.040)

        LABEL_TECNOLOGIA = Label(pnt,text="TECNOLOGIA: ",font=('Bahnschrift',10))
        #LABEL_TECNOLOGIA.place(x=50,y=150)
        LABEL_TECNOLOGIA.place(relx=0.035,rely=0.210,relwidth=0.080,relheight=0.040)

        LABEL_PULGADAS = Label(pnt,text="PULGADAS: ",font=('Bahnschrift',10))
        #LABEL_PULGADAS.place(x=50,y=220)
        LABEL_PULGADAS.place(relx=0.035,rely=0.300,relwidth=0.080,relheight=0.040)

        LABEL_RESOLUCION = Label(pnt,text="RESOLUCION: ",font=('Bahnschrift',10))
        #LABEL_RESOLUCION.place(x=50,y=280)
        LABEL_RESOLUCION.place(relx=0.035,rely=0.390,relwidth=0.080,relheight=0.040)

        LABEL_SMART_TV = Label(pnt,text="SMART_TV: ",font=('Bahnschrift',10))
        #LABEL_SMART_TV.place(x=50,y=340)
        LABEL_SMART_TV.place(relx=0.035,rely=0.480,relwidth=0.080,relheight=0.040)

        LABEL_ROKU = Label(pnt,text="ROKU: ",font=('Bahnschrift',10))
        #LABEL_ROKU.place(x=300,y=340)
        LABEL_ROKU.place(relx=0.035,rely=0.570,relwidth=0.080,relheight=0.040)

        LABEL_CANTIDAD = Label(pnt,text="CANTIDAD: ",font=('Bahnschrift',10))
        #LABEL_CANTIDAD.place(x=50,y=400)
        LABEL_CANTIDAD.place(relx=0.035,rely=0.660,relwidth=0.080,relheight=0.040)

        LABEL_PRECIO = Label(pnt,text="PRECIO POR UNIDA: ",font=('Bahnschrift',10))
        #LABEL_PRECIO.place(x=300,y=400)
        LABEL_PRECIO.place(relx=0.035,rely=0.750,relwidth=0.120,relheight=0.040)

        LABEL_CATEGORIA = Label(pnt,text="CATEGORIA: ",font=('Bahnschrift',10))
        #LABEL_CATEGORIA.place(x=50,y=450)
        LABEL_CATEGORIA.place(relx=0.035,rely=0.840,relwidth=0.120,relheight=0.040)

        global ID_SERIE_ENTRY
        global MARCA_C
        global MODELO_ENTRY
        global TECNOLOGIA_BOX
        global PULGADAS_ENTRY
        global RESOLUCION_BOX
        global SMART_TV_BOX
        global ROKU_BOX
        global CANTIDAD_ENTRY
        global PRECIO_ENTRY 
        global CATEGORIA_BOX
        
        ID_SERIE_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=ID_SERIE,font=('Bahnschrift',10))
        ID_SERIE_ENTRY.place(relx=0.160,rely=0.030,relwidth=0.140,relheight=0.040)
        
        MARCA_C = ttk.Combobox(pnt,values =["ONN","TCL","HISENSE","RCA","LG","JVC","SPECTER","WESTINGHOUSE","SAMSUMG"],width=17,textvariable=MARCA,font=('Bahnschrift',10))
        #MARCA_C.place(x=150,y=90)
        MARCA_C.place(relx=0.160,rely=0.120,relwidth=0.140,relheight=0.040)

        MODELO_ENTRY = Entry(pnt,textvariable=MODELO,font=('Bahnschrift',10))
        #MODELO_ENTRY.place(x=370,y=90)
        MODELO_ENTRY.place(relx=0.400,rely=0.120,relwidth=0.140,relheight=0.040)

        TECNOLOGIA_BOX = ttk.Combobox(pnt,values=["LED","QLED","OLED"],width=17,textvariable=TECNOLOGIA,font=('Bahnschrift',10))
        #TECNOLOGIA_C.place(x=150,y=150)
        TECNOLOGIA_BOX.place(relx=0.160,rely=0.210,relwidth=0.140,relheight=0.040)

        PULGADAS_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=PULGADAS,font=('Bahnschrift',10))
        #PULGADAS_ENTRY.place(x=150,y=220)
        PULGADAS_ENTRY.place(relx=0.160,rely=0.300,relwidth=0.140,relheight=0.040)

        RESOLUCION_BOX = ttk.Combobox(pnt,values=["720P","1080P","2K","4K"],width=17,textvariable=RESOLUCION,font=('Bahnschrift',10))
        #RESOLUCION_C.place(x=150,y=280)
        RESOLUCION_BOX.place(relx=0.160,rely=0.390,relwidth=0.140,relheight=0.040)

        SMART_TV_BOX= ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=SMART_TV,font=('Bahnschrift',10))
        #SMART_TV_C.place(x=150,y=340)
        SMART_TV_BOX.place(relx=0.160,rely=0.480,relwidth=0.140,relheight=0.040)

        ROKU_BOX = ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=ROKU,font=('Bahnschrift',10))
        #ROKU_C.place(x=350,y=340)
        ROKU_BOX.place(relx=0.160,rely=0.570,relwidth=0.140,relheight=0.040)

        CANTIDAD_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=CANTIDAD,font=('Bahnschrift',10))
        #CANTIDAD_ENTRY.place(x=150,y=400)
        CANTIDAD_ENTRY.place(relx=0.160,rely=0.660,relwidth=0.140,relheight=0.040)

        PRECIO_ENTRY = Entry(pnt,textvariable=PRECIO,font=('Bahnschrift',10))
        #PRECIO_ENTRY.place(x=440,y=400)
        PRECIO_ENTRY.place(relx=0.160,rely=0.750,relwidth=0.140,relheight=0.040)

        CATEGORIA_BOX= ttk.Combobox(pnt,values=["TELEVISIONES","ABANICOS"],width=17,textvariable=CATEGORIA,font=('Bahnschrift',10))
        #CATEGORIA_C.place(x=150,y=450)
        CATEGORIA_BOX.place(relx=0.160,rely=0.840,relwidth=0.140,relheight=0.040)

        global botonenviar
        botonenviar = Button(pnt,text="ENVIAR",command=Ventana_ingreso_de_datos.Ingresar_datos_a_mysql)
        #botonenviar.place(x=440,y=450,width=100,height=50)
        botonenviar.place(relx=0.400,rely=0.930,relwidth=0.140,relheight=0.040)

        #para pase a otra pagina dentro del programa
        global menubar
        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=menu.eliminar_contenido_de_ingreso)
        menubar.add_cascade(label="Menu", menu=filemenu)
        
class ventana_de_actualizacion:
    def imprimirven():
        if (ID_SERIE_ENTRY_ven.get() =="" or MARCA_C_ven.get() =="" or MODELO_ENTRY_ven.get()==""
            or TECNOLOGIA_C_ven.get()=="" or PULGADAS_ENTRY_ven.get()=="" or RESOLUCION_C_ven.get()=="" 
            or SMART_TV_C_ven.get()=="" or ROKU_C_ven.get()=="" or CANTIDAD_ENTRY_ven.get()=="" or 
            PRECIO_ENTRY_ven.get()=="" or CATEGORIA_C_ven.get()==""):
            messagebox.showinfo(message="Existen espacios vacios")
            
        else:
            ID_SQL= ID_LABEL_ENTRY_ven.get()
            ID_SERIE_SQL=ID_SERIE_ENTRY_ven.get()
            MARCA_SQL = MARCA_C_ven.get()
            MODELO_SQL=MODELO_ENTRY_ven.get()
            TECNOLOGIA_SQL=TECNOLOGIA_C_ven.get()
            PULGADAS_SQL=PULGADAS_ENTRY_ven.get()
            RESOLUCION_SQL=RESOLUCION_C_ven.get()
            SMART_TV_SQL=SMART_TV_C_ven.get()
            ROKU_SQL=ROKU_C_ven.get()
            CANTIDAD_SQL=CANTIDAD_ENTRY_ven.get()
            PRECIO_SQL=PRECIO_ENTRY_ven.get()
            CATEGORIA_SQL = CATEGORIA_C_ven.get()
            cursor = connectio.cursor()
            A =float(PRECIO.get())
            b =A + 500
            cantidad_tv= float(CANTIDAD_ENTRY_ven.get())
            precio_tv = float(PRECIO_ENTRY_ven.get())
            total = cantidad_tv * precio_tv
            consulta ="UPDATE INVENTARIOTV SET ID_SERIE = %s,MARCA= %s,MODELO= %s,TECNOLOGIA= %s,PULGADAS= %s,RESOLUCION= %s,SMART_TV= %s,ROKU= %s,CANTIDAD= %s,PRECIO= %s,PRECIO_DE_VENTA= %s,VALOR_TOTAL_MERCANCIA= %s,CATEGORIA=%s WHERE ID=%s"
            valores = (ID_SERIE_SQL,MARCA_SQL,MODELO_SQL,TECNOLOGIA_SQL,PULGADAS_SQL,RESOLUCION_SQL,SMART_TV_SQL,ROKU_SQL,CANTIDAD_SQL,PRECIO_SQL,b,total,CATEGORIA_SQL,ID_SQL)
            cursor.execute(consulta,valores)
            connectio.commit()
            messagebox.showinfo(message="Elementos actualizados",title="Estado de ingreso de datos")
            ventana_de_actualizacion.limpiar_VEN()
            messagebox.showinfo(message="Advertencia",title="Es nesesario recargar la pagina")
            menu.eliminar_contenido_de_actualizacion()
            
    def ventana_de_tabla():
        menu.Eliminar_botones()
        global ID_LABEL_ENTRY_ven
        global ID_SERIE_ENTRY_ven
        global MARCA_C_ven
        global MODELO_ENTRY_ven
        global TECNOLOGIA_C_ven
        global PULGADAS_ENTRY_ven
        global RESOLUCION_C_ven
        global SMART_TV_C_ven
        global ROKU_C_ven
        global CANTIDAD_ENTRY_ven
        global PRECIO_ENTRY_ven
        global CATEGORIA_C_ven

        global LABEL_ID_SERIE_ven
        global LABEL_MARCA_ven
        global LABEL_MODELO_ven
        global LABEL_TECNOLOGIA_ven
        global LABEL_PULGADAS_ven
        global LABEL_RESOLUCION_ven
        global LABEL_SMART_TV_ven
        global LABEL_ROKU_ven
        global LABEL_CANTIDAD_ven
        global LABEL_PRECIO_ven
        global ID_LABEL_ven
        global LABEL_CATEGORIA_ven
        
        ventana_de_actualizacion.arbol_datos()

        LABEL_ID_SERIE_ven = Label(pnt,text="ID_SERIE: ",font=('Bahnschrift',10))
        #LABEL_ID_SERIE_ven.place(x=50,y=250)
        LABEL_ID_SERIE_ven.place(relx=0.025,rely=0.450,relwidth=0.140,relheight=0.040)

        LABEL_MARCA_ven = Label(pnt,text="MARCA: ",font=('Bahnschrift',10))
        #LABEL_MARCA_ven.place(x=445,y=250)
        LABEL_MARCA_ven.place(relx=0.360,rely=0.450,relwidth=0.140,relheight=0.040)

        LABEL_MODELO_ven = Label(pnt,text="MODELO: ",font=('Bahnschrift',10))
        #LABEL_MODELO_ven.place(x=780,y=250)
        LABEL_MODELO_ven.place(relx=0.675,rely=0.450,relwidth=0.140,relheight=0.040)
        
        LABEL_TECNOLOGIA_ven = Label(pnt,text="TECNOLOGIA: ",font=('Bahnschrift',10))
        #LABEL_TECNOLOGIA_ven.place(x=50,y=300)
        LABEL_TECNOLOGIA_ven.place(relx=0.020,rely=0.550,relwidth=0.140,relheight=0.040)

        LABEL_PULGADAS_ven = Label(pnt,text="PULGADAS: ",font=('Bahnschrift',10))
        #LABEL_PULGADAS_ven.place(x=420,y=300)
        LABEL_PULGADAS_ven.place(relx=0.350,rely=0.550,relwidth=0.140,relheight=0.040)

        LABEL_RESOLUCION_ven = Label(pnt,text="RESOLUCION: ",font=('Bahnschrift',10))
        #LABEL_RESOLUCION_ven.place(x=760,y=300)
        LABEL_RESOLUCION_ven.place(relx=0.665,rely=0.550,relwidth=0.140,relheight=0.040)

        LABEL_SMART_TV_ven= Label(pnt,text="SMART_TV: ",font=('Bahnschrift',10))
        #LABEL_SMART_TV_ven.place(x=50,y=350)
        LABEL_SMART_TV_ven.place(relx=0.025,rely=0.635,relwidth=0.140,relheight=0.040)

        LABEL_ROKU_ven= Label(pnt,text="ROKU: ",font=('Bahnschrift',10))
        #LABEL_ROKU_ven.place(x=450,y=350)
        LABEL_ROKU_ven.place(relx=0.360,rely=0.635,relwidth=0.140,relheight=0.040)
        
        LABEL_CANTIDAD_ven = Label(pnt,text="CANTIDAD: ",font=('Bahnschrift',10))
        #LABEL_CANTIDAD_ven.place(x=780,y=350)
        LABEL_CANTIDAD_ven.place(relx=0.675,rely=0.635,relwidth=0.140,relheight=0.040)

        LABEL_PRECIO_ven = Label(pnt,text="PRECIO POR UNIDAD: ",font=('Bahnschrift',10))
        #LABEL_PRECIO_ven.place(x=370,y=400)
        LABEL_PRECIO_ven.place(relx=0.325,rely=0.725,relwidth=0.140,relheight=0.040)

        LABEL_CATEGORIA_ven = Label(pnt,text="CATEGORIA: ",font=('Bahnschrift',10))
        #LABEL_CATEGORIA_ven.place(x=770,y=400)
        LABEL_CATEGORIA_ven.place(relx=0.670,rely=0.730,relwidth=0.140,relheight=0.040)
        
        ID_LABEL_ven= Label(pnt,text="ID SELECIONADO:",font=('Bahnschrift',10))
        #ID_LABEL_ven.place(x=100,y=400)
        ID_LABEL_ven.place(relx=0.005,rely=0.730,relwidth=0.140,relheight=0.040)

        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
        ID_LABEL_ENTRY_ven=Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=ID,font=('Bahnschrift',10))
        #ID_LABEL_ENTRY_ven.place(x=140,y=400)
        ID_LABEL_ENTRY_ven.place(relx=0.125,rely=0.730,relwidth=0.140,relheight=0.040)

        ID_SERIE_ENTRY_ven = Entry(pnt,textvariable=ID_SERIE,font=('Bahnschrift',10))
        #ID_SERIE_ENTRY_ven.place(x=140,y=250)
        ID_SERIE_ENTRY_ven.place(relx=0.125,rely=0.450,relwidth=0.140,relheight=0.040)

        MARCA_C_ven = ttk.Combobox(pnt,values =["ONN","TCL","HISENSE","RCA","LG","JVC","SPECTER","WESTINGHOUSE"],width=17,textvariable=MARCA,font=('Bahnschrift',10))
        #MARCA_C_ven.place(x=500,y=250)
        MARCA_C_ven.place(relx=0.460,rely=0.450,relwidth=0.140,relheight=0.040)
        
        MODELO_ENTRY_ven = Entry(pnt,textvariable=MODELO,font=('Bahnschrift',10))
        #MODELO_ENTRY_ven.place(x= 850,y=250)
        MODELO_ENTRY_ven.place(relx=0.780,rely=0.450,relwidth=0.140,relheight=0.040)

        TECNOLOGIA_C_ven = ttk.Combobox(pnt,values=["LED","QLED","OLED"],width=17,textvariable=TECNOLOGIA,font=('Bahnschrift',10))
        #TECNOLOGIA_C_ven.place(x=140,y=300)
        TECNOLOGIA_C_ven.place(relx=0.125,rely=0.550,relwidth=0.140,relheight=0.040)
        
        PULGADAS_ENTRY_ven = Entry(pnt,textvariable=PULGADAS,font=('Bahnschrift',10))
        #PULGADAS_ENTRY_ven.place(x=500,y=300)
        PULGADAS_ENTRY_ven.place(relx=0.460,rely=0.550,relwidth=0.140,relheight=0.040)

        RESOLUCION_C_ven = ttk.Combobox(pnt,values=["720P","1080P","2K","4K"],width=17,textvariable=RESOLUCION,font=('Bahnschrift',10))
        #RESOLUCION_C_ven.place(x=850,y=300)
        RESOLUCION_C_ven.place(relx=0.780,rely=0.550,relwidth=0.140,relheight=0.040)

        SMART_TV_C_ven= ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=SMART_TV,font=('Bahnschrift',10))
        #SMART_TV_C_ven.place(x=140,y=350)
        SMART_TV_C_ven.place(relx=0.125,rely=0.630,relwidth=0.140,relheight=0.040)
        
        ROKU_C_ven = ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=ROKU,font=('Bahnschrift',10))
        #ROKU_C_ven.place(x=500,y=350)
        ROKU_C_ven.place(relx=0.460,rely=0.630,relwidth=0.140,relheight=0.040)

        CANTIDAD_ENTRY_ven = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=CANTIDAD,font=('Bahnschrift',10))
        #CANTIDAD_ENTRY_ven.place(x=850,y=350)
        CANTIDAD_ENTRY_ven.place(relx=0.780,rely=0.630,relwidth=0.140,relheight=0.040)
        
        PRECIO_ENTRY_ven = Entry(pnt,textvariable=PRECIO,font=('Bahnschrift',10))
        #PRECIO_ENTRY_ven.place(x=500,y=400)
        PRECIO_ENTRY_ven.place(relx=0.460,rely=0.730,relwidth=0.140,relheight=0.040)

        CATEGORIA_C_ven= ttk.Combobox(pnt,values=["TELEVISIONES","ABANICOS"],width=17,textvariable=CATEGORIA,font=('Bahnschrift',10))
        #CATEGORIA_C_ven.place(x=850,y=400)
        CATEGORIA_C_ven.place(relx=0.780,rely=0.730,relwidth=0.140,relheight=0.040)
        
    def eliminar():
        ID_SQL= ID_LABEL_ENTRY_ven.get()
        alerta = messagebox.askyesno("Advertencia","Estas seguro de eliminar de la tabla la columna con el id= "+ ID_SQL)
        
        if alerta:
             cursor = connectio.cursor()
             consulta ="DELETE FROM INVENTARIOTV WHERE id = %s"
             valor = (ID_SQL)
             cursor.execute(consulta,valor)
             connectio.commit()
             messagebox.showinfo(message="Elemento eliminado",title="Estado de ingreso de datos")
             ventana_de_actualizacion.limpiar_VEN()
             messagebox.showinfo(message="Es nesesario aplicar los cambios regresando al menu")
             menu.eliminar_contenido_de_actualizacion()
        else:
            print("columna no eliminada")
            
    def limpiar_VEN():
        ID_LABEL_ENTRY_ven.config(state="normal")
        ID_LABEL_ENTRY_ven.delete(0,END)
        ID_SERIE_ENTRY_ven.delete(0,END)
        MARCA_C_ven.delete(0,END)
        MODELO_ENTRY_ven.delete(0,END)
        TECNOLOGIA_C_ven.delete(0,END)
        PULGADAS_ENTRY_ven.delete(0,END)
        RESOLUCION_C_ven.delete(0,END)
        SMART_TV_C_ven.delete(0,END)
        ROKU_C_ven.delete(0,END)
        CANTIDAD_ENTRY_ven.delete(0,END)
        PRECIO_ENTRY_ven.delete(0,END)
        CATEGORIA_C_ven.delete(0,END)

    def arbol_datos():
        global arbol
        arbol = ttk.Treeview(pnt)
        arbol['columns'] = ('columna1', 'columna2', 'columna3','columna4','columna5','columna6','columna7','columna8','columna9','columna10','columna11','columna12','columna13')
        a = 70
        arbol.heading("#0", text='ID')
        arbol.column("#0", anchor=CENTER, width=35)
        arbol.heading('columna1', text='ID_SKU')
        arbol.column('columna1', anchor=CENTER, width=80)
        arbol.heading('columna2', text='MARCA')
        arbol.column('columna2', anchor=CENTER, width=70)
        arbol.heading('columna3', text='MODELO')
        arbol.column('columna3', anchor=CENTER, width=a)
        arbol.heading('columna4', text='TECNOLOGIA')
        arbol.column('columna4', anchor=CENTER, width=90)
        arbol.heading('columna5', text='PULGADAS')
        arbol.column('columna5', anchor=CENTER, width=70)
        arbol.heading('columna6', text='RESOLUCION')
        arbol.column('columna6', anchor=CENTER, width=80)
        arbol.heading('columna7', text='SMART_TV')
        arbol.column('columna7', anchor=CENTER, width=a)
        arbol.heading('columna8', text='ROKU')
        arbol.column('columna8', anchor=CENTER, width=40)
        arbol.heading('columna9', text='CANTIDAD')
        arbol.column('columna9', anchor=CENTER, width=a)
        arbol.heading('columna10', text='PRECIO')
        arbol.column('columna10', anchor=CENTER, width=50)
        arbol.heading('columna11', text='PRECIO/DE/VENTA')
        arbol.column('columna11', anchor=CENTER, width=110)
        arbol.heading('columna12', text='VALOR/TOTAL')
        arbol.column('columna12', anchor=CENTER, width=90)
        arbol.heading('columna13', text='CATEGORIA')
        arbol.column('columna13', anchor=CENTER, width=90)

        arbol.place(relx=0.01,rely=0.01,relwidth=0.980,relheight=0.425)

        global botonenviarven
        botonenviarven = Button(pnt,text="Actualizar",command=ventana_de_actualizacion.imprimirven)
        botonenviarven.place(relx=0.300,rely=0.850,relwidth=0.140,relheight=0.040)

        global botoneliminar
        botoneliminar = Button(pnt,text="Eliminar",command=ventana_de_actualizacion.eliminar)
        botoneliminar.place(relx=0.675,rely=0.850,relwidth=0.140,relheight=0.040)


        def mostrar_datos(event):
            item = arbol.selection()[0]
            values = arbol.item(item, 'values')

            ID_LABEL_ENTRY_ven.delete(0, END)
            ID_LABEL_ENTRY_ven.insert(0, arbol.item(item, 'text'))
            
            ID_SERIE_ENTRY_ven.delete(0, END)
            ID_SERIE_ENTRY_ven.insert(0, values[0])

            MARCA_C_ven.delete(0, END)
            MARCA_C_ven.insert(0, values[1])

            MODELO_ENTRY_ven.delete(0, END)
            MODELO_ENTRY_ven.insert(0, values[2])

            TECNOLOGIA_C_ven.delete(0, END)
            TECNOLOGIA_C_ven.insert(0, values[3])

            PULGADAS_ENTRY_ven.delete(0, END)
            PULGADAS_ENTRY_ven.insert(0, values[4])

            RESOLUCION_C_ven.delete(0, END)
            RESOLUCION_C_ven.insert(0, values[5])

            SMART_TV_C_ven.delete(0, END)
            SMART_TV_C_ven.insert(0, values[6])

            ROKU_C_ven.delete(0, END)
            ROKU_C_ven.insert(0, values[7])

            CANTIDAD_ENTRY_ven.delete(0, END)
            CANTIDAD_ENTRY_ven.insert(0, values[8])

            PRECIO_ENTRY_ven.delete(0, END)
            PRECIO_ENTRY_ven.insert(0, values[9])

            CATEGORIA_C_ven.delete(0,END)
            CATEGORIA_C_ven.insert(0,values[12])      
        arbol.bind('<<TreeviewSelect>>', mostrar_datos)   
        
        
        #Consultar los datos de la base de datos
        cursor = connectio.cursor()
        cursor.execute("select * from INVENTARIOTV")
        registros = cursor.fetchall()
        for registro in registros:
            arbol.insert('', END, text=registro[0], values=(registro[1], registro[2], registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9],registro[10],registro[11],registro[12],registro[13]))
        global menubar
        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=menu.eliminar_contenido_de_actualizacion)
        menubar.add_cascade(label="Menu", menu=filemenu)
        
class venta_de_busqueda_mysql():
    
    def buscar_informacion():
        valor_busqueda = entry_busqueda.get()
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='basededatos',
            db='TELEVISIONES'
        )
        cursor = cnx.cursor()
        if valor_busqueda =="":
            messagebox.askokcancel("Espacio de busqueda vacio","Es nesesario Ingresar un paramentro para inicial la busqueda")
        else:
            #MENOR A MAYOR ASC
            #MAYOR A MENOR DESC
            query = "SELECT * FROM INVENTARIOTV WHERE RESOLUCION LIKE %s ORDER BY PRECIO DESC"
            cursor.execute(query, ('%' + valor_busqueda + '%',))
            resultados = cursor.fetchall()
            for i in arbol.get_children():
                arbol.delete(i)
            for resultado in resultados:
                arbol.insert("", END, text=resultado[0], values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[11]))
                cursor.close()
            cnx.close()
            
    def ventana_de_busqueda():
        menu.Eliminar_botones()
        global arbol
        global entry_busqueda
        global label_busqueda
        global boton_buscar
        label_busqueda = Label(pnt, text="Buscar Televisiones por ID:")
        label_busqueda.place(relx=0.425,rely=0.015,relwidth=0.140,relheight=0.040)
        entry_busqueda = Entry(pnt)
        entry_busqueda.place(relx=0.425,rely=0.060,relwidth=0.140,relheight=0.040)
        boton_buscar = Button(pnt, text="Buscar", command=venta_de_busqueda_mysql.buscar_informacion)
        boton_buscar.place(relx=0.450,rely=0.115,relwidth=0.100,relheight=0.040)
        
        columnas = ("ID_SERIE", "MARCA", "MODELO","TECNOLOGIA","PULGADAS","RESOLUCION","SMART_TV","ROKU","CANTIDAD","PRECIO_DE_VENTA")
        arbol = Treeview(pnt, columns=columnas, show="headings")
        for col in columnas:
            arbol.heading(col, text=col)
            arbol.column("ID_SERIE",width=80)
            arbol.column("MARCA",width=95)
            arbol.column("MODELO",width=70)
            arbol.column("TECNOLOGIA",width=90)
            arbol.column("PULGADAS",width=70)
            arbol.column("RESOLUCION",width=80)
            arbol.column("SMART_TV",width=70)
            arbol.column("ROKU",width=40)
            arbol.column("CANTIDAD",width=70)
            arbol.column("PRECIO_DE_VENTA",width=110)
        arbol.place(relx=0.01,rely=0.175,relwidth=0.980,relheight=0.425)
        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=menu.elimina_contenido_de_busqueda)
        menubar.add_cascade(label="Menu", menu=filemenu)

class menu:
    def eliminar_contenido_de_ingreso():
        menubar.destroy()

        ID_SERIE_ENTRY.delete(0,END)
        MARCA_C.delete(0,END)
        MODELO_ENTRY.delete(0,END)
        TECNOLOGIA_BOX.delete(0,END)
        PULGADAS_ENTRY.delete(0,END)
        RESOLUCION_BOX.delete(0,END)
        SMART_TV_BOX.delete(0,END)
        ROKU_BOX.delete(0,END)
        CANTIDAD_ENTRY.delete(0,END)
        PRECIO_ENTRY.delete(0,END)
        
        LABEL_ID_SERIE.destroy()
        LABEL_MARCA.destroy()
        LABEL_MODELO.destroy()
        LABEL_TECNOLOGIA.destroy()
        LABEL_PULGADAS.destroy()
        LABEL_RESOLUCION.destroy()
        LABEL_SMART_TV.destroy()
        LABEL_ROKU.destroy()
        LABEL_CANTIDAD.destroy()
        LABEL_PRECIO.destroy()
        LABEL_CATEGORIA.destroy()
        
        ID_SERIE_ENTRY.destroy()
        MARCA_C.destroy()
        MODELO_ENTRY.destroy()
        TECNOLOGIA_BOX.destroy()
        PULGADAS_ENTRY.destroy()
        RESOLUCION_BOX.destroy()
        SMART_TV_BOX.destroy()
        ROKU_BOX.destroy()
        CANTIDAD_ENTRY.destroy()
        PRECIO_ENTRY .destroy()
        CATEGORIA_BOX.destroy()
        botonenviar.destroy()
        menu.botones_principlaes(set)
        
    def eliminar_contenido_de_actualizacion():
        menubar.destroy()
        ID_LABEL_ENTRY_ven.config(state="normal")
        ID_LABEL_ENTRY_ven.delete(0,END)
        ID_SERIE_ENTRY_ven.delete(0,END)
        MARCA_C_ven.delete(0,END)
        MODELO_ENTRY_ven.delete(0,END)
        TECNOLOGIA_C_ven.delete(0,END)
        PULGADAS_ENTRY_ven.delete(0,END)
        RESOLUCION_C_ven.delete(0,END)
        SMART_TV_C_ven.delete(0,END)
        ROKU_C_ven.delete(0,END)
        CANTIDAD_ENTRY_ven.delete(0,END)
        PRECIO_ENTRY_ven.delete(0,END)
        CATEGORIA_C_ven.delete(0,END)
        ID_LABEL_ENTRY_ven.destroy()
        ID_SERIE_ENTRY_ven.destroy()
        MARCA_C_ven.destroy()
        MODELO_ENTRY_ven.destroy()
        TECNOLOGIA_C_ven.destroy()
        PULGADAS_ENTRY_ven.destroy()
        RESOLUCION_C_ven.destroy()
        SMART_TV_C_ven.destroy()
        ROKU_C_ven.destroy()
        CANTIDAD_ENTRY_ven.destroy()
        PRECIO_ENTRY_ven.destroy()
        LABEL_ID_SERIE_ven.destroy()
        LABEL_MARCA_ven.destroy()
        LABEL_MODELO_ven.destroy()
        LABEL_TECNOLOGIA_ven.destroy()
        LABEL_PULGADAS_ven.destroy()
        LABEL_RESOLUCION_ven.destroy()
        LABEL_SMART_TV_ven.destroy()
        LABEL_ROKU_ven.destroy()
        LABEL_CANTIDAD_ven.destroy()
        LABEL_PRECIO_ven.destroy()
        ID_LABEL_ven.destroy()
        CATEGORIA_C_ven.destroy()
        LABEL_CATEGORIA_ven.destroy()
        arbol.destroy()
        botonenviarven.destroy()
        botoneliminar.destroy()
        menu.botones_principlaes(set)
        
    def elimina_contenido_de_busqueda():
        label_busqueda.destroy()
        boton_buscar.destroy()
        entry_busqueda.destroy()
        arbol.destroy()
        menu.botones_principlaes(set)

    def botones_principlaes(set):
        global Btn_ingreso_de_datos
        global Btn_Busqueda_de_datos
        global Btn_Actualizacion_de_datos

        Btn_ingreso_de_datos = Button(pnt,text="Ingreso de TV",command=Ventana_ingreso_de_datos.ventana_de_ingreso)
        Btn_ingreso_de_datos.place(relx=0.01,rely=0.45,relwidth=0.2,relheight=0.1)
        #Btn_ingreso_de_datos.place(x=230,y=200,width=130,height=100)

        Btn_Actualizacion_de_datos = Button(pnt,text="Actualizacion de inventario de TV",command=ventana_de_actualizacion.ventana_de_tabla)
        Btn_Actualizacion_de_datos.place(relx=0.40,rely=0.45,relwidth=0.2,relheight=0.1)
        #Btn_Actualizacion_de_datos.place(x=450,y=200,width=200,height=100)

        Btn_Busqueda_de_datos = Button(pnt,text="Busqueda de TV",command=venta_de_busqueda_mysql.ventana_de_busqueda)
        Btn_Busqueda_de_datos.place(relx=0.78,rely=0.45,relwidth=0.2,relheight=0.1)
        #Btn_Busqueda_de_datos.place(x=700,y=200,width=125,height=100)

    def Eliminar_botones():
        Btn_ingreso_de_datos.destroy()
        Btn_Actualizacion_de_datos.destroy()
        Btn_Busqueda_de_datos.destroy()

pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

ventana_princiapl = menu()
ventana_princiapl.botones_principlaes()

pnt.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

pnt.mainloop()
