
#------------------Autor: Basiliо--------------------------------------
#-----------------Fecha  20210424---version v1-1-1 ----------------------------------


#--------------Declaración de funciones --------------------------------
def calculoConsomo(litros, kilomertosTrascutidos):
    consumo = litros/kilomertosTrascutidos*100
    return consumo

def costePorKilometro(consumo, precioCombustible):
    costeKM = consumo*precioCombustible/100
    return costeKM
    

#---------------------Inputs de los datos-------------------------------
litros = float(input("Indique los litros repostados: "))
kilomertosTrascutidos = int(input("indique los kilometros transcurridos: "))
precioCombustible = float(input("indique el precio de combustible: "))
elegirCaclculo = int(input("Para calcular el consumo, pulse 1, para calcular coste por kilometro, pulse 2 "))


#------------------Condicional eleccion de la funcion--------------------

if elegirCaclculo == 1:
        print("El consumo es: ", calculoConsomo(litros, kilomertosTrascutidos), "por cada 100 Km")


#----------v.1-1------LLAMADA A LA PRIMERA FUNCION costePorKilometro(calculoConsomo(litros, kilomertosTrascutidos), precioCombustible)--------------    
elif elegirCaclculo == 2:
     print("El coste por Kilometro es: ", costePorKilometro(calculoConsomo(litros, kilomertosTrascutidos), precioCombustible), "€")

#------------------------------v.1-1-1------------------------
else:
    print("El valor ingresado no es admitido, intentalo de nuevo")
    while elegirCaclculo != 1 or 2:
            elegirCaclculo = int(input("Para calcular el consumo, pulse 1, para calcular coste por kilometro, pulse 2 "))



      
