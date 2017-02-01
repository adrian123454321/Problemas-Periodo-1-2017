lista=[]
cantidad=[]
print("1)ingrese un producto:")
print("2)mostrar producto:")
opciones = "si"
while opciones == "si":

	producto = int(input("ingrese una opcion :"))
	if producto == 1:
		dato = input("ingrese un producto :")
		lista.append(dato)	
		dato2 = int(input("ingrese cantidad :"))	
		cantidad.append(dato2)	
	elif producto == 2:
		for dato in (lista):
			print(dato,dato2)
		print(lista)	
	opciones = str(input("desea continuar? :"))