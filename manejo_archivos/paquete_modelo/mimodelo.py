"""
    creación de clases
"""

class Persona(object):
    
    def __init__(self, n, ape, ed, cod, n1, n2):
        self.nombre = n 
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_edad(self, ed):
        self.edad = int(ed)

    def obtener_edad(self):
        return self.edad
    
    def agregar_codigo(self, cod):
        self.codigo = int(cod)

    def obtener_codigo(self):
        return self.codigo

    def agregar_apellido(self, ape):
        self.apellido = ape
    
    def obtener_apellido(self):
        return self.apellido

    def agregar_nota1(self, n1):
        self.nota1 = n1
    
    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self, n2):
        self.nota1 = n2
    
    def obtener_nota2(self):
        return self.nota2
    
    def __str__(self): #equivalente al toString en java, para visualizar los metodos como tal
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido, self.edad, self.codigo, self.nota1, self.nota2)


class OperacionesPersona(object):
    
    def __init__(self, listado):

        self.listado_personas = listado

    def agregar_lista_personas(self, lista):
        
        self.listado_personas = lista
    
    def obtener_lista_personas(self):
        
        return self.listado_personas

    def obtener_promedio_n1(self):
        
        suma = 0
        for l in self.obtener_lista_personas():
            suma = suma + l.obtener_nota1()


        promedio1 = suma/len(self.obtener_lista_personas())

        return promedio1
    
    def obtener_promedio_n2(self):
        
        suma = 0
        for l in self.obtener_lista_personas():
            suma = suma + l.obtener_nota2()

        promedio2 = suma/len(self.obtener_lista_personas())

        return promedio2

#Listado menores de 15 nota 1
#Listado menores de 15 nota 2
#Listado menores de 15 nombre empiece con R o J

    def obtener_listado_n1(self):

        cadena = "" #se crea una cadena vacia
        for l in self.obtener_lista_personas(): #for para recorrer la lista
            if (l.obtener_nota1() < 15): #condicion para comparar si la nota1 de la lista es menor a 15
                cadena = "%s %s" % (l.obtener_nombre(), l.obtener_apellido()) #formateo de cadenas para presentar llamando a los metodos, solo si cumple la condicon

        return cadena #retorna la cadena

    def obtener_listado_n2(self):

        cadena = "" #se crea una cadena vacia
        for l in self.obtener_lista_personas(): #for para recorrer la lista
            if (l.obtener_nota2() < 15): #condicion para comparar si la nota1 de la lista es menor a 15
                cadena = "%s %s" % (l.obtener_nombre(), l.obtener_apellido()) #formateo de cadenas para presentar llamando a los metodos, solo si cumple la condicon

        return cadena #retorna la cadena

    def obtener_listado_personas(self,a,b): #metoodo para oobtener los nombres que empiezan con r o j
        cadena = "" #cadena vacia
        for l in self.obtener_lista_personas(): #recorrer la lista 
            if(l.obtener_nombre()[0:1] == a or l.obtener_nombre()[0:1] == b): #condicion para identificar la primera letra de los nombres y compararlos con los paremetros recibidos
                cadena = "%s %s \n" % (cadena, l.obtener_nombre()) #alacenar en la cadena

        return cadena #retornar la  cadena


    def __str__ (self):

        cadena = "" 
        for n in self.listado_personas:
            cadena = "%s%s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena
