import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

class ConjuntoOperacionesApp:
    def __init__(self, master):
        self.master = master
        master.title("Operaciones entre Conjuntos")

        self.conjunto_entries = []
        self.conjunto_labels = []

        for i in range(3):  # Puedes cambiar el rango para permitir más conjuntos
            label = tk.Label(master, text=f"Conjunto {i+1}:")
            label.pack()
            self.conjunto_labels.append(label)

            entry = tk.Entry(master)
            entry.pack()
            self.conjunto_entries.append(entry)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.operations_frame = tk.Frame(master)
        self.operations_frame.pack()

        self.add_button = tk.Button(self.operations_frame, text="Agregar Conjunto", command=self.add_conjunto)
        self.add_button.pack(side=tk.LEFT)

        self.venn_button = tk.Button(self.operations_frame, text="Mostrar diagrama de Venn", command=self.venn)
        self.venn_button.pack(side=tk.LEFT)

        self.operations_menu = tk.OptionMenu(master, tk.StringVar(master, "Seleccione una operación"), "Unión", "Intersección", "Diferencia", "Complemento", "Combinación", "Cardinalidad", "Subconjunto", "Disjuntos")
        self.operations_menu.pack()

        self.perform_button = tk.Button(master, text="Realizar Operación", command=self.perform_operation)
        self.perform_button.pack()

    def add_conjunto(self):
        if len(self.conjunto_entries) < 5:  # Limita el número de conjuntos a 5
            new_label = tk.Label(self.master, text=f"Conjunto {len(self.conjunto_entries) + 1}:")
            new_label.pack()
            self.conjunto_labels.append(new_label)

            new_entry = tk.Entry(self.master)
            new_entry.pack()
            self.conjunto_entries.append(new_entry)

    def union_conjuntos(self, conjuntos):
        return set().union(*conjuntos)

    def venn(self):
        conjuntos = [set(entry.get().split()) for entry in self.conjunto_entries if entry.get()]
        num_conjuntos = len(conjuntos)

        if num_conjuntos == 2:
            self.show_venn(conjuntos, "Unión")
        elif num_conjuntos == 3:
            self.show_venn(conjuntos, "Intersección")
        else:
            print("Solo se puede mostrar diagrama de Venn para 2 o 3 conjuntos.")
            return

    def perform_operation(self):
        operation = self.operations_menu.cget("text")
        if operation == "Seleccione una operación":
            self.result_label.config(text="Por favor, seleccione una operación.")
            return

        conjuntos = [set(entry.get().split()) for entry in self.conjunto_entries if entry.get()]
        result = ""
        
        if operation == "Unión":
            result = self.union_conjuntos(conjuntos)
            self.show_venn(conjuntos, "Unión")
        elif operation == "Intersección":
            result = self.interseccion_conjuntos(conjuntos)
            self.show_venn(conjuntos, "Intersección")
        elif operation == "Diferencia":
            result = self.diferencia_conjuntos(conjuntos[0], conjuntos[1])
            self.show_venn([conjuntos[0], conjuntos[1]], "Diferencia")
        elif operation == "Complemento":
            result = self.complemento_conjunto(conjuntos[0], conjuntos[1])
            self.show_venn([conjuntos[0], result], "Complemento")
        elif operation == "Combinación":
            result = self.combinacion_conjuntos(conjuntos)
            self.show_venn([result], "Combinación")
        elif operation == "Cardinalidad":
            result = self.cardinalidad_conjunto(conjuntos[0])
        elif operation == "Subconjunto":
            result = self.es_subconjunto(conjuntos[0], conjuntos[1])
        elif operation == "Disjuntos":
            result = self.son_disjuntos(conjuntos[0], conjuntos[1])

        self.result_label.config(text=result)

    def show_venn(self, conjuntos, operation):
        num_conjuntos = len(conjuntos)

        if num_conjuntos == 2:
            venn2(subsets=(conjuntos[0], conjuntos[1]), set_labels=[f"Conjunto {i+1}" for i in range(num_conjuntos)])
        elif num_conjuntos == 3:
            venn3(subsets=(conjuntos[0], conjuntos[1], conjuntos[2]), set_labels=[f"Conjunto {i+1}" for i in range(num_conjuntos)])
        else:
            print("Solo se puede mostrar diagrama de Venn para 2 o 3 conjuntos.")
            return

        plt.title(operation)
        plt.show()

    @staticmethod
    def interseccion_conjuntos(conjuntos):
        return set().intersection(*conjuntos)

    @staticmethod
    def diferencia_conjuntos(conjunto1, conjunto2):
        return conjunto1.difference(conjunto2)

    @staticmethod
    def complemento_conjunto(conjunto, conjunto_universal):
        return conjunto_universal.difference(conjunto)

    @staticmethod
    def combinacion_conjuntos(conjuntos):
        combinacion = set()
        for conjunto in conjuntos:
            combinacion.update(conjunto)
        return combinacion

    @staticmethod
    def cardinalidad_conjunto(conjunto):
        return f"Cardinalidad: {len(conjunto)}"

    @staticmethod
    def es_subconjunto(conjunto1, conjunto2):
        return conjunto1.issubset(conjunto2)

    @staticmethod
    def son_disjuntos(conjunto1, conjunto2):
        return conjunto1.isdisjoint(conjunto2)


root = tk.Tk()
app = ConjuntoOperacionesApp(root)
root.mainloop()
