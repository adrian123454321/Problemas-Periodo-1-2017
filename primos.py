a=0
numero=int(input("Ingrese numero\n"))
for i in range(1,numero+1):
 if(numero % i==0):
  a=a+1
if(a!=2):
 print("No es primo")
else:
 print("si es primo")