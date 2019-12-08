import patente
from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta


class App():

    def __init__(self):
        self.root = Tk()
        self.root.title('Gestion Estacionamiento')
        self.root.geometry("988x613+1638+155")
        self.root.minsize(1, 1)
        self.root.maxsize(2951, 870)
        self.root.resizable(1, 1)

        self.patente_add = StringVar()
        self.patente_search = StringVar()
        self.patente_search.trace('w', lambda name, index, mode: self.update_list())
        self.espacio_total = '100'
        self.espacio_libre = 100
        self.espacio_ocupado = 0

        self.Ingress_button = ttk.Button(self.root, text='Ingreso Patente', state='normal', command=self.Ingreso_Manual())
        self.Entry_add = ttk.Entry(self.root, textvariable=self.patente_add, width=5)
        self.Egress_button = ttk.Button(self.root, text='Egreso Patente Seleccionada', command=self.Egreso_Manual())
        self.search_label = ttk.Label(self.root, text='Buscar Pantente')
        self.search_Entry = ttk.Entry(self.root, textvariable=self.patente_search, width=5)
        self.listBox = ttk.Listbox(self.root)
        self.total_space_Label = ttk.Label(self.root, text='Total de espacios:')
        self.Free_space_Label = ttk.Label(self.root, text='Espacios Libres:')
        self.Occu_Space_Label = ttk.Label(self.root, text='Espacios Ocupados:')
        self.totals_Label = ttk.Label(self.root, textvariable=self.espacio_total)
        self.frees_Label = ttk.Label(self.root, text=self.espacio_libre)
        self.occus_Label = ttk.Label(self.root, text=self.espacio_ocupado)
        self.Notif_space_Label = ttk.Label(self.root, text='Hay Espacio Libre', fg='green')
        self.listBox.place(relx=0.466, rely=0.131, relheight=0.842, relwidth=0.52)
        self.search_label.place(relx=0.486, rely=0.065, height=31, width=129)
        self.Ingress_button.place(relx=0.081, rely=0.114, height=51, width=81)
        self.Egress_button.place(relx=0.081, rely=0.277, height=51, width=81)
        self.Entry_add.place(relx=0.02, rely=0.212, height=33, relwidth=0.229)
        self.search_Entry.place(relx=0.678, rely=0.065, height=33, relwidth=0.229)
        self.total_space_Label.place(relx=0.02, rely=0.44, height=31, width=159)
        self.Free_space_Label.place(relx=0.02, rely=0.522, height=41, width=159)
        self.Occu_Space_Label.place(relx=0.03, rely=0.62, height=41, width=139)
        self.totals_Label.place(relx=0.243, rely=0.457, height=21, width=39)
        self.frees_Label.place(relx=0.243, rely=0.538, height=21, width=39)
        self.occus_Label.place(relx=0.243, rely=0.636, height=21, width=39)

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
            self.listBox.insert(END, unaPatente.toStringLite())
            self.espacio_libre -= 1
            self.espacio_ocupado += 1

    def Egreso_Manual(self):
        print(self.lista_patentes.curselection()[0])
        self.lista_patentes.delete(self.lista_patentes.curselection()[0])

    def update_list(self):
        search_term = self.patente_search.get()
        lista = []
        for item in self.lista_patentes:
            lista.append(item)
        self.lista_patentes.delete(0, END)
        for item in lista:
            if search_term.lower() in item.lower():
                self.lista_patentes.insert(END, item)

    def update_labels(self):
        self.frees_Label.configure(text=self.espacio_libre)
        self.occus_Label.configure(text=self.espacio_ocupado)
        if self.espacio_ocupado >= 100:
            self.Notif_space_Label.configure(fg='red')
            self.Ingress_button.configure(state='disabled')
        else:
            self.Ingress_button.configure(state='normal')


def aplic():
    ap = App()
    return 0


aplic()
