import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

class ConjuntoOperacionesApp:
    def __init__(self, master):
        self.master = master
        master.title("Operaciones entre Conjuntos")

        self.label_1 = tk.Label(master, text="Conjunto 1:")
        self.label_1.pack()

        self.entry_1 = tk.Entry(master)
        self.entry_1.pack()

        self.label_2 = tk.Label(master, text="Conjunto 2:")
        self.label_2.pack()

        self.entry_2 = tk.Entry(master)
        self.entry_2.pack()

        self.union_button = tk.Button(master, text="Unión", command=self.union)
        self.union_button.pack()

        self.interseccion_button = tk.Button(master, text="Intersección", command=self.interseccion)
        self.interseccion_button.pack()

        self.diferenciaA_button = tk.Button(master, text="Diferencia A - B", command=self.diferenciaA)
        self.diferenciaA_button.pack()

        self.diferenciaB_button = tk.Button(master, text="Diferencia en B - A", command=self.diferenciaB)
        self.diferenciaB_button.pack()

        self.venn_button = tk.Button(master, text="Mostrar diagrama de Venn", command= self.venn)
        self.venn_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def union(self):
        conjunto1 = list(self.entry_1.get().split())
        conjunto2 = list(self.entry_2.get().split())
        resultado = self.union_conjuntos(conjunto1, conjunto2)
        self.result_label.config(text=f"Unión: {resultado}")

    def interseccion(self):
        conjunto1 = list(self.entry_1.get().split())
        conjunto2 = list(self.entry_2.get().split())
        resultado = self.interseccion_conjuntos(conjunto1, conjunto2)
        self.result_label.config(text=f"Intersección: {resultado}")

    def diferenciaA(self):
        conjunto1 = list(self.entry_1.get().split())
        conjunto2 = list(self.entry_2.get().split())
        resultado= self.diferencia_conjuntos(conjunto1, conjunto2)
        self.result_label.config(text=f"Diferencia: {resultado}")

    def diferenciaB(self):
        conjunto1 = list(self.entry_1.get().split())
        conjunto2 = list(self.entry_2.get().split())
        resultado = self.diferencia_conjuntos(conjunto2, conjunto1)
        self.result_label.config(text=f"Diferencia: {resultado}")

    def venn(self):
        conjunto1 = set(self.entry_1.get().split())
        conjunto2 = set(self.entry_2.get().split())
        venn2([conjunto1, conjunto2],(conjunto1, conjunto2))
        plt.show()

    @staticmethod
    def union_conjuntos(conjunto1, conjunto2):
        union = []
        for elemento in conjunto1:
            if elemento not in union:
                union.append(elemento)
        for elemento in conjunto2:
            if elemento not in union:
                union.append(elemento)
        resultado=", ".join(union)
        return resultado

    @staticmethod
    def interseccion_conjuntos(conjunto1, conjunto2):
        interseccion = []
        for elemento in conjunto1:
            if elemento in conjunto2:
                interseccion.append(elemento)
        resultado= ", ".join(interseccion)
        return interseccion

    @staticmethod
    def diferencia_conjuntos(conjunto1, conjunto2):
        diferencia = []
        for elemento in conjunto1:
            if elemento not in conjunto2:
                diferencia.append(elemento)
        resultado= ", ".join(diferencia)
        return diferencia


root = tk.Tk()
app = ConjuntoOperacionesApp(root)
root.mainloop()
