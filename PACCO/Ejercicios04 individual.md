```python
### Estructura iterativa for

## hacer un programa mostrar por pantalla los numeros áres del 0 al 10:
for num in range(0, 11, 2):
    print(num)

```

    0
    2
    4
    6
    8
    10



```python
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

```

    De cuantos elementos crearemos la lista de nombres :  3
    Ingresar Nombre de la posicion 0 :  Juancito
    Ingresar Nombre de la posicion 1 :  Luisito
    Ingresar Nombre de la posicion 2 :  Marianita


    
     la lista completa de Nombres es :
     ['Juancito', 'Luisito', 'Marianita']



```python
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

```

    No se encontro el numero 9



```python
## Hacer un programa que lea la lista de obras de Mario Vargas Llosa e indique el orden de los libros

#Lista de Libros de Mario Vargas Llosa
obras_mvll = ["La ciudad y los perros", "La casa verde", "Pantaleon y las visitadoras"]
#Lista Orden de los libros
orden = ["primer", "segundo", "tercer"]

#Utilizamos enumerate
for i, libro in enumerate(obras_mvll):
    print("\nEl " + orden[i] + " libro de Mario Vargas Llosa es: " + libro)
    
```

    
    El primer libro de Mario Vargas Llosa es: La ciudad y los perros
    
    El segundo libro de Mario Vargas Llosa es: La casa verde
    
    El tercer libro de Mario Vargas Llosa es: Pantaleon y las visitadoras



```python
## Hacer un programa que realice invitaciones de una lista de nombres

for f in ["Joel", "Naty", "Jehu", "Angeles", "Maryori", "Lucita", "Mirella", "Cesar"]:
    invitation = "Hola " + f + ". ¡Por favor, ven a mi fiesta el sabado!"
    print (invitation)
```

    Hola Joel. ¡Por favor, ven a mi fiesta el sabado!
    Hola Naty. ¡Por favor, ven a mi fiesta el sabado!
    Hola Jehu. ¡Por favor, ven a mi fiesta el sabado!
    Hola Angeles. ¡Por favor, ven a mi fiesta el sabado!
    Hola Maryori. ¡Por favor, ven a mi fiesta el sabado!
    Hola Lucita. ¡Por favor, ven a mi fiesta el sabado!
    Hola Mirella. ¡Por favor, ven a mi fiesta el sabado!
    Hola Cesar. ¡Por favor, ven a mi fiesta el sabado!



```python
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

```

    10
    5.5
    2
    10
    55
    0



```python
## Hacer un programa que sume los elementos de una lista, usamos funcion sum

m = [1, 2, 3, 4]
sum(m)
```




    10




```python
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

```

    Ingrese un numero:  3


    
    Los multiplos de  3 son: 
    3  6  9  12  15  18  21  24  27  30  



```python
## Ejemplo de for anidado: Creacion de tablas

for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 2):
            print(i, j, k)

```

    0 0 0
    0 0 1
    0 1 0
    0 1 1
    0 2 0
    0 2 1
    0 3 0
    0 3 1
    1 0 0
    1 0 1
    1 1 0
    1 1 1
    1 2 0
    1 2 1
    1 3 0
    1 3 1
    2 0 0
    2 0 1
    2 1 0
    2 1 1
    2 2 0
    2 2 1
    2 3 0
    2 3 1
    3 0 0
    3 0 1
    3 1 0
    3 1 1
    3 2 0
    3 2 1
    3 3 0
    3 3 1



```python
## Hacer un programa que permita hallar la raiz enesima de un numero que se ingresara por el teclado

numero = float(input("Ingrese un numero: "))

for n in range(2, 101):
    print("la raiz {0}-esima de {1} es {2}".format(n, numero, numero**(1/n)))

```

    Ingrese un numero:  6


    la raiz 2-esima de 6.0 es 2.449489742783178
    la raiz 3-esima de 6.0 es 1.8171205928321397
    la raiz 4-esima de 6.0 es 1.5650845800732873
    la raiz 5-esima de 6.0 es 1.4309690811052556
    la raiz 6-esima de 6.0 es 1.3480061545972777
    la raiz 7-esima de 6.0 es 1.2917083420907467
    la raiz 8-esima de 6.0 es 1.2510334048590739
    la raiz 9-esima de 6.0 es 1.2202849358728105
    la raiz 10-esima de 6.0 es 1.1962311988513155
    la raiz 11-esima de 6.0 es 1.1769039562428527
    la raiz 12-esima de 6.0 es 1.1610366723739942
    la raiz 13-esima de 6.0 es 1.1477777154347986
    la raiz 14-esima de 6.0 es 1.1365334760097243
    la raiz 15-esima de 6.0 es 1.1268776101908264
    la raiz 16-esima de 6.0 es 1.1184960459738218
    la raiz 17-esima de 6.0 es 1.1111523342970424
    la raiz 18-esima de 6.0 es 1.1046650785974952
    la raiz 19-esima de 6.0 es 1.0988928027655247
    la raiz 20-esima de 6.0 es 1.0937235477264424
    la raiz 21-esima de 6.0 es 1.0890675587944523
    la raiz 22-esima de 6.0 es 1.0848520434800557
    la raiz 23-esima de 6.0 es 1.0810173469046067
    la raiz 24-esima de 6.0 es 1.0775141170184241
    la raiz 25-esima de 6.0 es 1.0743011732208552
    la raiz 26-esima de 6.0 es 1.0713438829035236
    la raiz 27-esima de 6.0 es 1.0686129101356392
    la raiz 28-esima de 6.0 es 1.0660832406569969
    la raiz 29-esima de 6.0 es 1.063733414541692
    la raiz 30-esima de 6.0 es 1.0615449167090512
    la raiz 31-esima de 6.0 es 1.0595016886637296
    la raiz 32-esima de 6.0 es 1.0575897342418854
    la raiz 33-esima de 6.0 es 1.0557967989083417
    la raiz 34-esima de 6.0 es 1.0541121070820896
    la raiz 35-esima de 6.0 es 1.0525261456012585
    la raiz 36-esima de 6.0 es 1.0510304841428222
    la raiz 37-esima de 6.0 es 1.0496176254437533
    la raiz 38-esima de 6.0 es 1.0482808797099776
    la raiz 39-esima de 6.0 es 1.0470142587761369
    la raiz 40-esima de 6.0 es 1.045812386485474
    la raiz 41-esima de 6.0 es 1.0446704224624213
    la raiz 42-esima de 6.0 es 1.0435839969999792
    la raiz 43-esima de 6.0 es 1.042549155216214
    la raiz 44-esima de 6.0 es 1.0415623089763069
    la raiz 45-esima de 6.0 es 1.0406201953489853
    la raiz 46-esima de 6.0 es 1.039719840584283
    la raiz 47-esima de 6.0 es 1.038858528775155
    la raiz 48-esima de 6.0 es 1.0380337745075658
    la raiz 49-esima de 6.0 es 1.0372432989191824
    la raiz 50-esima de 6.0 es 1.0364850086811943
    la raiz 51-esima de 6.0 es 1.0357569774952138
    la raiz 52-esima de 6.0 es 1.0350574297610367
    la raiz 53-esima de 6.0 es 1.0343847261238408
    la raiz 54-esima de 6.0 es 1.0337373506532688
    la raiz 55-esima de 6.0 es 1.0331138994434157
    la raiz 56-esima de 6.0 es 1.0325130704533463
    la raiz 57-esima de 6.0 es 1.0319336544334674
    la raiz 58-esima de 6.0 es 1.0313745268047354
    la raiz 59-esima de 6.0 es 1.0308346403759792
    la raiz 60-esima de 6.0 es 1.0303130188001368
    la raiz 61-esima de 6.0 es 1.0298087506834
    la raiz 62-esima de 6.0 es 1.0293209842725104
    la raiz 63-esima de 6.0 es 1.0288489226550819
    la raiz 64-esima de 6.0 es 1.0283918194160655
    la raiz 65-esima de 6.0 es 1.0279489747005777
    la raiz 66-esima de 6.0 es 1.027519731639418
    la raiz 67-esima de 6.0 es 1.0271034730988913
    la raiz 68-esima de 6.0 es 1.0266996187211181
    la raiz 69-esima de 6.0 es 1.0263076222249912
    la raiz 70-esima de 6.0 es 1.0259269689413855
    la raiz 71-esima de 6.0 es 1.0255571735592441
    la raiz 72-esima de 6.0 es 1.0251977780617856
    la raiz 73-esima de 6.0 es 1.0248483498343846
    la raiz 74-esima de 6.0 es 1.0245084799276936
    la raiz 75-esima de 6.0 es 1.0241777814613477
    la raiz 76-esima de 6.0 es 1.0238558881551532
    la raiz 77-esima de 6.0 es 1.0235424529760397
    la raiz 78-esima de 6.0 es 1.0232371468902683
    la raiz 79-esima de 6.0 es 1.0229396577114687
    la raiz 80-esima de 6.0 es 1.0226496890360228
    la raiz 81-esima de 6.0 es 1.0223669592581706
    la raiz 82-esima de 6.0 es 1.0220912006579554
    la raiz 83-esima de 6.0 es 1.021822158555803
    la raiz 84-esima de 6.0 es 1.0215595905281194
    la raiz 85-esima de 6.0 es 1.0213032656788383
    la raiz 86-esima de 6.0 es 1.0210529639623078
    la raiz 87-esima de 6.0 es 1.0208084755533517
    la raiz 88-esima de 6.0 es 1.0205696002607108
    la raiz 89-esima de 6.0 es 1.0203361469804202
    la raiz 90-esima de 6.0 es 1.0201079331859866
    la raiz 91-esima de 6.0 es 1.0198847844525065
    la raiz 92-esima de 6.0 es 1.0196665340121167
    la raiz 93-esima de 6.0 es 1.0194530223384006
    la raiz 94-esima de 6.0 es 1.0192440967575702
    la raiz 95-esima de 6.0 es 1.019039611084432
    la raiz 96-esima de 6.0 es 1.0188394252813178
    la raiz 97-esima de 6.0 es 1.0186434051383018
    la raiz 98-esima de 6.0 es 1.018451421973175
    la raiz 99-esima de 6.0 es 1.0182633523497657
    la raiz 100-esima de 6.0 es 1.0180790778133073



```python
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

```

    Ingrese su nombre:  paco


    Nombre Correcto
    Nombre Correcto
    Nombre Correcto
    Nombre Correcto


    Ingrese su apellido:  Torres


    Nombre Correcto
    Nombre Correcto
    Nombre Correcto
    Nombre Correcto
    Nombre Correcto
    Nombre Correcto



```python

```
