#Ejer 2
cateto1=float(input("ingesa cateto 1 : "))
print("cateto 1 es: "+str(cateto1))
cateto2=float(input("ingresa cateto 2: "))
print("cateto 2 es: "+str(cateto2))
hipo=((cateto1**2)+(cateto2**2))**1/2
print("la hipotenusa es: ",hipo)
#Ejer 7
minutos_1=int(input("ingresar minutos a transformar"))
hora_1=0
con__="False"
while con__=="False":
    if(minutos_1>=60):
        minutos_1=minutos_1-60
        hora_1=hora_1+1
    else:
        con__="true"
print (la hora e)
#ejer 15

 #se pide a que hora salio 
hora_ini=int(input("ingresar a la hora que salio el ciclista: "))
minutos_ini=int(input("ingresar a los minutos que salio el ciclista: "))
segundos_ini=int(input("ingresar a los segundos que salio el ciclista: "))
  #se pide a que hora va a esta en la ciudad b
hora_tar=int(input("ingresar tiempo en hora que va a tardar(sin contar minutos o segundos): "))
minutos_tar=int(input("ingresar los minutos: "))
segundos_tar=int(input("ingresar los segundos: "))
  #sumo los tiempos  
segundos_to=segundos_ini+segundos_tar
minutos_to=minutos_ini+minutos_tar
hora_to=hora_ini+hora_tar
 #ahora los voy a pasar a hora minutos segundos 
con_="False"
while con_=="False":
    
    if (segundos_to>=60):
        segundos_to=segundos_to-60
        minutos_to=minutos_to+1
    elif(minutos_to>=60):
        minutos_to=minutos_to-60
        hora_to=hora_to+1
    else:
        con_="true"

print("llego a las ",hora_to,"horas ",minutos_to,"minutos y",segundos_to," segundos")


              
     
         

 
   

