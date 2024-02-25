print("\n\nRealizemos un calculo...\n\n")
capital = float(input("¿Que cantidad de dinero te gustaria invertir? COP: $"))
interes = float(input("\n\n¿Que porcentaje tiene la tasa de interes anual? %: "))
tiempo = float(input("\n\n¿Cuantos años dejaras el dinero generando intereses?: "))

expresion_porcentual = interes/100

retorno = float(capital*expresion_porcentual)*tiempo

print(f"\n\nLuego de {tiempo} años, tendras un retorno de ${retorno} COP.\n\n")