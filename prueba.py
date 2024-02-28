import tkinter as tk
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles

#Autores: Juan Manuel Duque Giraldo && Kevin Santiago Buitron

#Abstraccion: Para el programa sera necesario que existan almenos 4 entradas del usuario, 3 conjuntos y operaciones, ademas de 2 botones, para realizar la operacion y dibujar el diagrama
            #Ademas las operaciones entre conjuntos son metodos simples de implementar, aunque sea sin utilizar los metodos predefinidos por python, estos metodos se pueden implementar
            #Mediante recorridos de listas, la parte mas compleja sera la de darle estructura a las operaciones combinadas entre conjuntos

#Descomposicion: Los metodos de operaciones entre conjuntos implmentan parametros de 2 listas, es decir que siempre se realizan operaciones entre 2 conjuntos, ya que mediante el manejo de
            #las operaciones , no sera necesario crear metodos para hacer operaciones entre 3 conjuntos, para el manejo de la operacion se usa una pila, para realizar operaciones con
            #jerarquia, en orden de izquierda a derecha, se reconocen mediante comparacion de strings las operaciones y se realizan secuencialmente

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

        self.diagrama_venn_button = tk.Button(master, text="Mostrar Diagrama de Venn", command=self.mostrar_diagrama)
        self.diagrama_venn_button.pack()

        self.operacion_button = tk.Button(master, text="Realizar Operación", command=self.operacion)
        self.operacion_button.pack()

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

    #Metodo para dar manejo a la solicitud de una operacion ingresada por el usuario
    def operacion(self):
        #Obtener la operacion ingresada
        operacion =list((self.operacion_entry.get().split()))
        diccionario_conjuntos={"A":list(self.coonjuntoA_entry.get().split()),"B":list(self.coonjuntoB_entry.get().split()),"C":list(self.coonjuntoC_entry.get().split())}
        #Calcular el conjunto unversal para hacer ciertos calculos
        universal = self.calcular_universal_conjuntos(diccionario_conjuntos["A"], diccionario_conjuntos["B"], diccionario_conjuntos["C"])
        pila= []

        i=0
        #Desglosamos la operacion usando una pila
        while i < len(operacion):
            #Si el elemento es un operando o conjunto se guarda en una pila
            if(operacion[i] in ("A", "B", "C")):
                pila.append(diccionario_conjuntos[operacion[i]])
            #Si el elemento es un operador se debe llamar al metodo de operacion y guardar el resultado final en la pila nuevamente
            if(operacion[i] in ("union", "interseccion", "diferencia")):
                operador=operacion[i]
                i+=1
                pila.append(diccionario_conjuntos[operacion[i]])
                conjunto1=pila.pop()
                conjunto2=pila.pop()
                aux= self.definir_operacion(operador, conjunto1, conjunto2)
                pila.append(aux)
            #Si el operando es el complemento se hace un proceso distinto
            if(operacion [i] == "complemento"):
                conjunto=pila.pop()
                aux= self.complemento_conjuntos(conjunto, universal)
                pila.append(aux)
            i+=1
        resultado=", ".join(pila.pop())
        self.resultado_label.config(text=f"Resultado: {resultado}")

    #Metodo que permite mostrar el diagrama de Venn
    def mostrar_diagrama(self):
        diccionario_conjuntos={"A":set(self.coonjuntoA_entry.get().split()),"B":set(self.coonjuntoB_entry.get().split()),"C":set(self.coonjuntoC_entry.get().split())}

        #Define la forma del diagrama de Venn, 2 conjunto o 3
        if len(diccionario_conjuntos) == 2:
            venn2(subsets=[set(diccionario_conjuntos[col])for col in diccionario_conjuntos])
            plt.title("Diagrama de Venn 2 conjuntos")
            venn2_circles(subsets=[set(diccionario_conjuntos[col])for col in diccionario_conjuntos], linestyle='solid')
        elif len(diccionario_conjuntos) == 3:
            venn3(subsets=[set(diccionario_conjuntos[col])for col in diccionario_conjuntos])
            plt.title("Diagrama de Venn 3 conjuntos")
            venn3_circles(subsets=[set(diccionario_conjuntos[col])for col in diccionario_conjuntos], linestyle='solid')
        
        plt.show()

    #Redirige la operacion hacia el metodo definido
    def definir_operacion(self, operacion, conjunto1, conjunto2):
        resultado= list()
        if operacion==self.operaciones[0]:
            resultado= self.union_conjuntos(conjunto1,conjunto2)
        if operacion==self.operaciones[1]:
            resultado= self.interseccion_conjuntos(conjunto1, conjunto2)
        if operacion==self.operaciones[2]:
            resultado= self.diferencia_conjuntos(conjunto1, conjunto2)
        return resultado
    
    #Metodo que calcula la union de 2 conjuntos, retorna una lista
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
    
    #Metodo que calcula la interseccion de 2 conjuntos, retorna una lista
    @staticmethod
    def interseccion_conjuntos(conjunto1, conjunto2):
        interseccion = list()
        for elemento in conjunto1:
            if elemento in conjunto2:
                interseccion.append(elemento)
        return interseccion
    
    #Metodo que calcula la diferencia entre 2 conjuntos, retorna una lista
    @staticmethod
    def diferencia_conjuntos(conjunto1, conjunto2):
        diferencia = list()
        for elemento in conjunto1:
            if elemento not in conjunto2:
                diferencia.append(elemento)
        return diferencia
    
    #Metodo que calcula el complemento de un conjunto dado, retorna una lista
    @staticmethod
    def complemento_conjuntos(conjunto, universo):
        complemento=list()
        for elemento in universo:
            if elemento not in conjunto:
                complemento.append(elemento)
        return complemento
    
    #Metodo que permite calcular el conjunto universal
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

