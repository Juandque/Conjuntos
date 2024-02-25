import tkinter as tk

class prueba:
    operaciones = ["union","interseccion","diferencia","complemento","subconjunto", "disyunto","cardinalidad"]

    def __init__(self, master):
        self.master=master
        master.title("Operaciones entre Conjuntos")

        self.label_1 = tk.Label(master, text="Conjunto A:")
        self.label_1.pack()

        self.coonjuntoA_entry = tk.Entry(master)
        self.coonjuntoA_entry.pack()

        self.label_2 = tk.Label(master, text="Conjunto B:")
        self.label_2.pack()

        self.coonjuntoB_entry = tk.Entry(master)
        self.coonjuntoB_entry.pack()

        self.label_3 = tk.Label(master, text="Conjunto C:")
        self.label_3.pack()

        self.coonjuntoC_entry = tk.Entry(master)
        self.coonjuntoC_entry.pack()

        self.label_4 =tk.Label(master, text="Operacion:")
        self.label_4.pack()

        self.operacion_entry = tk.Entry(master)
        self.operacion_entry.pack()

        self.operacion_button = tk.Button(master, text="Realizar Operación", command=self.operacion)
        self.operacion_button.pack()

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

    def operacion(self):
        operacion =list((self.operacion_entry.get().split()))
        diccionario_conjuntos={"A":list(self.coonjuntoA_entry.get().split()),"B":list(self.coonjuntoB_entry.get().split()),"C":list(self.coonjuntoC_entry.get().split())}
        universal = self.calcular_universal_conjuntos(diccionario_conjuntos["A"], diccionario_conjuntos["B"], diccionario_conjuntos["C"])
        pila= []

        i=0
        while i < len(operacion):
            if(operacion[i] in ("A", "B", "C")):
                pila.append(diccionario_conjuntos[operacion[i]])
            if(operacion[i] in ("union", "interseccion", "diferencia")):
                operador=operacion[i]
                i+=1
                pila.append(diccionario_conjuntos[operacion[i]])
                conjunto1=pila.pop()
                conjunto2=pila.pop()
                aux= self.definir_operacion(operador, conjunto1, conjunto2)
                pila.append(aux)
            if(operacion [i] == "complemento"):
                conjunto=pila.pop()
                aux= self.complemento_conjuntos(conjunto, universal)
                pila.append(aux)
            i+=1
        resultado=", ".join(pila.pop())
        self.resultado_label.config(text=f"Resultado: {resultado}")


    def definir_operacion(self, operacion, conjunto1, conjunto2):
        resultado= list()
        if operacion==self.operaciones[0]:
            resultado= self.union_conjuntos(conjunto1,conjunto2)
        if operacion==self.operaciones[1]:
            resultado= self.interseccion_conjuntos(conjunto1, conjunto2)
        if operacion==self.operaciones[2]:
            resultado= self.diferencia_conjuntos(conjunto1, conjunto2)
        return resultado
    
    @staticmethod
    def union_conjuntos(conjunto1, conjunto2):
        union = list()
        for elemento in conjunto1:
            if elemento not in union:
                union.append(elemento)
        for elemento in conjunto2:
            if elemento not in union:
                union.append(elemento)
        return union
    
    @staticmethod
    def interseccion_conjuntos(conjunto1, conjunto2):
        interseccion = list()
        for elemento in conjunto1:
            if elemento in conjunto2:
                interseccion.append(elemento)
        return interseccion

    @staticmethod
    def diferencia_conjuntos(conjunto1, conjunto2):
        diferencia = list()
        for elemento in conjunto1:
            if elemento not in conjunto2:
                diferencia.append(elemento)
        return diferencia
    
    @staticmethod
    def complemento_conjuntos(conjunto, universo):
        complemento=list()
        for elemento in universo:
            if elemento not in conjunto:
                complemento.append(elemento)
        return complemento
    
    @staticmethod
    def calcular_universal_conjuntos(conjunto1, cojunto2, conjunto3):
        universal=list(conjunto1)
        for e in cojunto2:
            if e not in universal:
                universal.append(e)
        for e in conjunto3:
            if e not in universal:
                universal.append(e)
        return universal

    
root = tk.Tk()
app = prueba(root)
root.mainloop()

