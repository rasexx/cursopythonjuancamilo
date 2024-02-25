payasos = int(input("¿Cuantos payasos enviaras?: "))
muñecas = int(input("¿Y cuantas muñecas?: "))
peso_payaso = 112
peso_muñeca = 75

peso_final = ((payasos*peso_payaso)+(muñecas*peso_muñeca))/100

print(f"El peso de este envio sera de {peso_final} Kg")