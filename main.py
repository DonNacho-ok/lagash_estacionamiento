import patente
from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta


class App():

    def __init__(self):
        self.root = Tk()
        self.root.title('Gestion Estacionamiento')
        self.root.geometry("988x632+271+133")
        self.root.minsize(120, 1)
        self.root.maxsize(2951, 870)
        self.root.resizable(1, 1)
        self.root.configure(background='#787878')

        self.patente_add = StringVar()
        self.patente_search = StringVar()
        self.espacio_total = '100'
        self.espacio_libre = 100
        self.espacio_ocupado = 0
        self.patente_egreso = StringVar()
        self.horas_estacionadas = IntVar()
        self.total_facturado = IntVar()
        self.lista_obj = []

        self.Ingress_button = ttk.Button(self.root, text='Ingreso Patente', state='normal', command=self.Ingreso_Manual)
        self.Entry_add = ttk.Entry(self.root, textvariable=self.patente_add, width=5)
        self.Egress_button = ttk.Button(self.root, text='Egreso Patente Seleccionada', command=self.Egreso_Manual)
        self.listBox = Listbox(self.root)
        self.total_space_Label = ttk.Label(self.root, text='Total de espacios:')
        self.Free_space_Label = ttk.Label(self.root, text='Espacios Libres:')
        self.Occu_Space_Label = ttk.Label(self.root, text='Espacios Ocupados:')
        self.totals_Label = ttk.Label(self.root, text=self.espacio_total)
        self.frees_Label = ttk.Label(self.root, text=self.espacio_libre)
        self.occus_Label = ttk.Label(self.root, text=self.espacio_ocupado)
        self.Notif_space_Label = ttk.Label(self.root, text='Hay Espacio Libre')
        self.show_patent_Label = ttk.Label(self.root, text='Patente Egresada:')
        self.show_hour_Label = ttk.Label(self.root, text='Horas estacionadas:')
        self.show_total_Label = ttk.Label(self.root, text='Total a pagar:')
        self.patent_Label = ttk.Label(self.root, textvariable=self.patente_egreso)
        self.hour_Label = ttk.Label(self.root, textvariable=self.horas_estacionadas)
        self.total_Label = ttk.Label(self.root, textvariable=self.total_facturado)

        self.listBox.place(relx=0.455, rely=0.016, relheight=0.959, relwidth=0.52)
        self.Entry_add.place(relx=0.02, rely=0.142,height=33, relwidth=0.229)
        self.Ingress_button.place(relx=0.081, rely=0.047, height=51, width=95)
        self.Egress_button.place(relx=0.263, rely=0.047, height=51, width=170)
        self.total_space_Label.place(relx=0.02, rely=0.237, height=31, width=159)
        self.Free_space_Label.place(relx=0.02, rely=0.316, height=41, width=159)
        self.Occu_Space_Label.place(relx=0.03, rely=0.396, height=41, width=139)
        self.totals_Label.place(relx=0.192, rely=0.237, height=31, width=44)
        self.frees_Label.place(relx=0.192, rely=0.316, height=31, width=44)
        self.occus_Label.place(relx=0.202, rely=0.411, height=21, width=34)
        self.Notif_space_Label.place(relx=0.04, rely=0.491, height=41, width=344)
        self.show_patent_Label.place(relx=0.01, rely=0.601, height=21, width=100)
        self.show_hour_Label.place(relx=0.01, rely=0.665, height=21, width=110)
        self.show_total_Label.place(relx=0.01, rely=0.728, height=21, width=74)
        self.patent_Label.place(relx=0.120, rely=0.601, height=21, width=44)
        self.hour_Label.place(relx=0.130, rely=0.665, height=21, width=65)
        self.total_Label.place(relx=0.101, rely=0.729, height=21, width=65)

        self.update_labels()
        self.root.mainloop()

    def Ingreso_Manual(self):
        error = False
        datetim = datetime.now()
        try:
            patent = self.patente_add.get()
        except:
            error = True
        if not error:
            unaPatente = patente.Patente(patent, datetim, '', 0)
            self.lista_obj.append(unaPatente)
            self.listBox.insert(END, unaPatente.toStringLite())
            self.espacio_libre -= 1
            self.espacio_ocupado += 1
            self.update_labels()

    def Egreso_Manual(self):
        indice = self.listBox.curselection()[0]
        self.lista_obj[indice].setFechaEgreso(datetime.now())
        diff = self.lista_obj[indice].getFechaEgreso() - self.lista_obj[indice].getFechaIngreso()
        total_segundos = diff.total_seconds()
        total_horas = ((total_segundos/60)/60)
        total_factu = total_horas * 115
        self.lista_obj[indice].setTotalFacturado(total_factu)
        self.patente_egreso.set(self.lista_obj[indice].getPatente())
        self.horas_estacionadas.set(total_horas)
        self.total_facturado.set(total_factu)
        self.lista_obj.pop(indice)
        self.listBox.delete(self.listBox.curselection()[0])
        self.espacio_libre += 1
        self.espacio_ocupado -= 1
        self.update_labels()

    def update_labels(self):
        self.frees_Label.configure(text=self.espacio_libre)
        self.occus_Label.configure(text=self.espacio_ocupado)
        if self.espacio_ocupado >= 100:
            self.Notif_space_Label.configure(text='No hay Mas espacios Libres', background='#787878', foreground='#ff0000', anchor=CENTER)
            self.Ingress_button.place_forget()
        else:
            self.Notif_space_Label.configure(text='Hay Espacios Libres', background='#787878', foreground='#00e81c', anchor=CENTER)
            self.Ingress_button.place(relx=0.081, rely=0.047, height=51, width=95)

def aplic():
    ap = App()
    return 0


aplic()
