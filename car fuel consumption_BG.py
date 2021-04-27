
#------------------Autor: Всасил--------------------------------------
#-----------------Fecha  20210427---version v1- ----------------------------------


#--------------Declaración de funciones --------------------------------
def calculoConsomo(litros, kilomertosTrascutidos):
    consumo = litros/kilomertosTrascutidos*100
    return consumo

def costePorKilometro(consumo, precioCombustible):
    costeKM = consumo*precioCombustible/100
    return costeKM
    

#---------------------Inputs de los datos-------------------------------
litros = float(input("Колко литра си раредил?: "))
kilomertosTrascutidos = int(input("Колко километра си изминал: "))
precioCombustible = float(input("Каква е цента нагоривото за литър: "))
elegirCaclculo = int(input("Натисни едно за да изчислиш разхода за 100 Км, натисни 2 за да изчислиш стойността на километър: "))


#------------------Condicional eleccion de la funcion--------------------

if elegirCaclculo == 1:
        print("Разхода на гориво е: ", calculoConsomo(litros, kilomertosTrascutidos), "на 100 Km")


#----------v.1-1------LLAMADA A LA PRIMERA FUNCION costePorKilometro(calculoConsomo(litros, kilomertosTrascutidos), precioCombustible)--------------    
elif elegirCaclculo == 2:
     print("Стойността на иминат километър е: ", costePorKilometro(calculoConsomo(litros, kilomertosTrascutidos), precioCombustible), "Лв")

#------------------------------v.1-1-1------------------------
else:
    print("Това число не е валидно натисни 1 или 2 ")
    while elegirCaclculo != 1 or 2:
            elegirCaclculo = int(input("Натисни едно за да изчислиш разхода за 100 Км, натисни 2 за да изчислиш стойността на километър: "))



      
