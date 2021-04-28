#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Calculos_CL(): #Creamos la clase Calculos_CL
   
   #---------------------------Creación de  constructor ---------------------
    def __init__(self, litros, Km, precio): #Definimos el parametro edad , nombre y ocupacion
        self.litros = litros # Definimos que el atributo edad, sera la edad asignada
        self.Km = Km # Definimos que el atributo nombre, sera el nombre asig
        self.precio = precio #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        
 #---------------------------Creación de  métodos---------------------
    def informar(self):
        Datos = ("Ha repostado {}, ha trascurido {} Km, el precio del combistible es {}") #Mensaje
        print(Datos.format(self.litros, self.Km, self.precio)) #Usamos FORMAT

    def calculoConsomo(self):
        mensaje = "Su consumo es:"
        elCalculo = self.litros/self.Km*100
        #print(elCalculo)
        print("{} {}".format(mensaje, elCalculo))

    def calculooste(self):
        costeKM = (self.litros/self.Km*100)*self.precio/100
        mensaje1 = "El coste por Km es:"
        #print(costeKM)
        print("{} {}".format(mensaje1, costeKM))
    
#--------------------Atributos contructor (variables)
Fiat = Calculos_CL(50, 700, 1.2) #Instancia


#------------------------Llamamos a lod métodos-----------------

# -------------------Llamada al metodo informat()-----------------
#Calculos_CL.informar(Fiat)
Fiat.informar()

# -------------------Llamada al metodo calculoConsomo()-----------------
#Calculos_CL.calculoConsomo(Fiat)
Fiat.calculoConsomo()

# -------------------Llamada al metodo calculoCoste()-----------------
#Calculos_CL.calculoCoste(Fiat)
Fiat.calculooste()

