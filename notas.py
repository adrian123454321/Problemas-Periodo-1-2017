lista=[]
print("1)ingresar nota")
print("2)mostrar Notas")
print("3)salir")
opciones = "si"
while opciones == "si":

	notas = int(input("elija una opcion :"))
	if notas == 1:
		nota = int(input("ingrese una nota :"))
		lista.append(nota)
		notas = sum(lista)/len(lista)	
	elif notas == 2:
 		print (sum(lista))/(len(lista))
	elif notas == 3:
		print("adios")
	opciones = str(input("desea continuar? :"))



