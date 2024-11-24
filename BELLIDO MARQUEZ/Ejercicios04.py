### Estructura iterativa for

## hacer un programa mostrar por pantalla los numeros áres del 0 al 10:
for num in range(0, 11, 2):
    print(num)
    
    
    
    
    
    ## Hacer un programa que permita ingresar nombres a una lista, utilizando funciones:

#Inicializamos la lista vacia
nombres = []

#funcion ingreso nombre
def ingreso(l):
    for i in range(0, l):
        m = input("Ingresar Nombre de la posicion {0} : ".format(i))
        nombres.append(m)

#Preguntamos de cuantos elementos conforman la lista
l = int(input("De cuantos elementos crearemos la lista de nombres : "))

ingreso(l)
print("\n la lista completa de Nombres es :\n",nombres)






## Metodo2: Hacer un programa que de una lista de numeros imprima la posicion del numero 9, utilizando funcion 'enumerate'

#lista de numeros
lista = [2, 4, 5, 7, 8, 19, 3, 4]

#utilizo la funcion 'enumerate' qe devuelve una tupla
#tupla de 2 elementos de una lista (posicion, contenido)
for i,m in enumerate(lista):
    if m == 9:
        break
else:
## Usamos 'for' conjuntamente con 'else'
    #ponemos negativa la posicion
    i = -1
    print('No se encontro el numero 9')

if i >=0:
    print(i)
    
    
    
    
    
    
    
    
    ## Hacer un programa que lea la lista de obras de Mario Vargas Llosa e indique el orden de los libros

#Lista de Libros de Mario Vargas Llosa
obras_mvll = ["La ciudad y los perros", "La casa verde", "Pantaleon y las visitadoras"]
#Lista Orden de los libros
orden = ["primer", "segundo", "tercer"]

#Utilizamos enumerate
for i, libro in enumerate(obras_mvll):
    print("\nEl " + orden[i] + " libro de Mario Vargas Llosa es: " + libro)
    
    
    
    
    
    
    
    
    
    
    
    ## Hacer un programa que realice invitaciones de una lista de nombres

for f in ["Joel", "Naty", "Jehu", "Angeles", "Maryori", "Lucita", "Mirella", "Cesar"]:
    invitation = "Hola " + f + ". ¡Por favor, ven a mi fiesta el sabado!"
    print (invitation)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ## Hacer un programa que sume los elementos de una lista, utilizar funciones y for

#solicita usar for y funciones, NO SE PUEDE USAR funcion 'sum'
def mysum(xs):
    """ Suma todos los numeros de la lista xs, y devuelve el total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

#add test like these to you test siute ...
print(mysum([1, 2, 3, 4]))        # ==>> 10
print(mysum([1.25, 2.5, 1.75]))     # ==>> 5.5
print(mysum([1, -2, 3]))          # ==>> 2
print(mysum([1, 2, 3, 4]))     # ==>> 10
print(mysum(range(11)))       # ==>> 55
print(mysum([]))               # ==>> 0














## Hacer un programa que sume los elementos de una lista, usamos funcion sum

m = [1, 2, 3, 4]
sum(m)










## Hacer un programa que imprima los multiplos hasta el numero 10 de cualquier numero

#Creamos la funcion multiplos
def multiplos(n):
    for i in range(1, 11):
        print(n * i, end="  ")
    print()

#Llamamos a la funcion con el numero de multiplo deseado
m = int(input("Ingrese un numero: "))
print("\nLos multiplos de ", m, "son: ")
multiplos(m)













## Ejemplo de for anidado: Creacion de tablas

for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 2):
            print(i, j, k)

















## Hacer un programa que permita hallar la raiz enesima de un numero que se ingresara por el teclado

numero = float(input("Ingrese un numero: "))

for n in range(2, 101):
    print("la raiz {0}-esima de {1} es {2}".format(n, numero, numero**(1/n)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






#creo la lista de validacion
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sim = ['?', '!', '$', '%', '&', '/', '~','°']

#funcion
def validar(nomap):
    for x in nomap:
        if x in num:
            print('Nombre no valido!!!')
        elif x in sim:
            print('Nombre no valido!!!')
        else:
            print('Nombre Correcto')

#ingresar nombre
nom = input('Ingrese su nombre: ')

#Llamar a la funcion
validar(nom)

#ingresar nombre
apell = input('Ingrese su apellido: ')

#llamar a la funcion
validar(apell)
