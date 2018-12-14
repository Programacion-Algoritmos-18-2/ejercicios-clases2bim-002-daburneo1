from paquete_archivos.miarchivo import MiArchivo 
from paquete_modelo.mimodelo import Persona
from paquete_modelo.mimodelo import OperacionesPersona

m = MiArchivo() #genero un objeto tipo MiArchivo
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)
suma_nota1 = 0
suma_nota2 = 0
lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
lista_personas = []
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5]) #Se crea un objeto tipo persona enviandole los parametros ya que el constructor de la clase esta esperando los parametros
    #suma_nota1 = suma_nota1 + p.obtener_nota1()
    #suma_nota2 = suma_nota2 + p.obtener_nota2()
    print(p)
    lista_personas.append(p)

#print(suma_nota1/len(lista))
#print(suma_nota2/len(lista))
operaciones = OperacionesPersona(lista_personas) #Se envia una lista de objetos persona

print("El promedio de las notas de Matematicas es: %s" % (operaciones.obtener_promedio_n1())) #Imprime el promedio n1
print("El promedio de las notas de Sociales es: %s" % (operaciones.obtener_promedio_n2())) #Imprime el promedio n2
print("Los estudiantes con promedio menor a 15 en Matematicas son: %s" % (operaciones.obtener_listado_n1())) #Imprime el nombre de los estudiantes con nota menor a 15 en n1
print("Los estudiantes con promedio menor a 15 en Sociales son: %s" % (operaciones.obtener_listado_n2())) #Imprime el nombre de los estudiantes con nota menor a 15 en n2
print("Los estudiantes cuyo nombre inicia con R o J son:")
print(operaciones.obtener_listado_personas("R","J")) #Envia los parametros a comparar 
