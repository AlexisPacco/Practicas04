```python
num=[6, 23, 89, 120]
for n in num:
    print(n)
```

    6
    23
    89
    120



```python
nom= "Maximiliano"
for letra in nom:
    print(letra)
```

    M
    a
    x
    i
    m
    i
    l
    i
    a
    n
    o



```python
for nombre in ['milita' , 'Luisito' , 'Pablito' , 'Alexandito']:
    print('Hola{0}, la longitud de tu nombre es de: {1} caracteres. '.format(nombre,len(nombre)))
```

    Holamilita, la longitud de tu nombre es de: 6 caracteres. 
    HolaLuisito, la longitud de tu nombre es de: 7 caracteres. 
    HolaPablito, la longitud de tu nombre es de: 7 caracteres. 
    HolaAlexandito, la longitud de tu nombre es de: 10 caracteres. 



```python
colo =["amarillo" ,"rojo" , "verde" ,"azul" , "purpura","blanco","negro","limon"]
colo_con_r=[]

for m in colo:
    if 'r'in m:
        colo_con_r.append(m)
print(colo_con_r)

```

    ['amarillo', 'rojo', 'verde', 'purpura', 'negro']



```python
for i in range(12):
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11



```python
for i in range(10):
    print(i+1, "",end="")
```

    1 2 3 4 5 6 7 8 9 10 


```python
for i in range(1,11):
    print(i, "",end="")
```

    1 2 3 4 5 6 7 8 9 10 


```python
for i in range(2,12,2):
    print(i, "",end="")
```

    2 4 6 8 10 


```python
for i in range(20,0,-2):
    print(i, "",end="")
```

    20 18 16 14 12 10 8 6 4 2 


```python
for i in range(40,-5,-5):
    print(i, "",end="")
```

    40 35 30 25 20 15 10 5 0 


```python
for i in range(50,-1,-5):
    print(i, "",end="")
```

    50 45 40 35 30 25 20 15 10 5 0 


```python
lista=[2,4,5,7,8,9,3,4]
cont=-1

for m in lista:
    cont += 1
    if m == 9:
        break
print(cont)
```

    5



```python
contador = 1
contador /= 5
print(contador)
```

    0.2



```python
lista=[2,4,5,7,8,19,3,4]
cont=-1

for m in lista:
    cont= cont + 1
    if m == 9:
        break
else:
    cont= -1
    print("No se encontro el numero 9")
if cont >= 0:
    print(cont)
```

    No se encontro el numero 9



```python
num=[12,14,15,27,108,90,33,49,200]

for p in num:
    if p % 2 !=0:
        continue
    print(p)

```

    12
    14
    108
    90
    200



```python
for num in range (0,11,2):
    print(num)
```

    0
    2
    4
    6
    8
    10



```python
nombres =[]
def ingreso (ele):
    for i in range (0,ele):
        m=input("Ingresar Nombre de la posicion {0} :".format(i))
        nombres.append(m)
l=int(input("De cuantos elementos crearemos la lista de nombres : "))

ingreso(l)
print("\n la lista completa de nombres es :\n",nombres)
```

    De cuantos elementos crearemos la lista de nombres :  3
    Ingresar Nombre de la posicion 0 : Juancito
    Ingresar Nombre de la posicion 1 : Luisito
    Ingresar Nombre de la posicion 2 : Marianita


    
     la lista completa de nombres es :
     ['Juancito', 'Luisito', 'Marianita']



```python
lista = [2,4,5,7,8,19,3,4]
for i,m in enumerate(lista):
    if m==9:
        break
else:
    i = -1
    print('No se encontro el numero 9')
if i >=0:
    print (i)
```

    No se encontro el numero 9



```python
obras_mv11=["La ciudad y los perros","La casa verde","Pantaleon y las visitadoras"]
orden=["primer","segundo","tercer"]
for i, libro in enumerate (obras_mv11):
    print("\nEl " + orden [i] + " libro de mario Vargas Llosa es :" + libro)
```

    
    El primer libro de mario Vargas Llosa es :La ciudad y los perros
    
    El segundo libro de mario Vargas Llosa es :La casa verde
    
    El tercer libro de mario Vargas Llosa es :Pantaleon y las visitadoras



```python
for f in ["Joel","Nati","Jehu","Angeles","Maryori","Lucila","Mirella","Cesar"]:
    invitation = "Hola " + f + ".  !Por favor , ven a mi fiesta el sabado!"
    print(invitation)
```

    Hola Joel.  !Por favor , ven a mi fiesta el sabado!
    Hola Nati.  !Por favor , ven a mi fiesta el sabado!
    Hola Jehu.  !Por favor , ven a mi fiesta el sabado!
    Hola Angeles.  !Por favor , ven a mi fiesta el sabado!
    Hola Maryori.  !Por favor , ven a mi fiesta el sabado!
    Hola Lucila.  !Por favor , ven a mi fiesta el sabado!
    Hola Mirella.  !Por favor , ven a mi fiesta el sabado!
    Hola Cesar.  !Por favor , ven a mi fiesta el sabado!



```python
def mysum(xs):
    """Suma los numeros de la lista xs, y devuelve el total."""
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total
print(mysum([1,2,3,4]))
print(mysum([1.25,2.5,1.75]))
print(mysum([1,-2,3]))
print(mysum([1,2,3,4]))
print(mysum(range(11)))
print(mysum([]))
```

    10
    5.5
    2
    10
    55
    0



```python
m = [1,2,3,4]
sum(m)
```




    10




```python
def multiplos (n):
    for i in range (1,10):
        print(n * i, end="  ")
    print()
m = int (input("ingrese un numero:"))
print("\nLos multiplos de ",m,"son:")
multiplos(m)
```

    ingrese un numero: 3


    
    Los multiplos de  3 son:
    3  6  9  12  15  18  21  24  27  



```python
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,2):
            print(i,j,k)
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
numero = float(input("Ingrese un numero: " ))

for n in range(2, 101):
    print("La raiz {0}-esima de {1} es {2}".format(n,numero,numero**(1/n)))
```

    Ingrese un numero:  6


    La raiz 2-esima de 6.0 es 2.449489742783178
    La raiz 3-esima de 6.0 es 1.8171205928321397
    La raiz 4-esima de 6.0 es 1.5650845800732873
    La raiz 5-esima de 6.0 es 1.4309690811052556
    La raiz 6-esima de 6.0 es 1.3480061545972777
    La raiz 7-esima de 6.0 es 1.2917083420907467
    La raiz 8-esima de 6.0 es 1.2510334048590739
    La raiz 9-esima de 6.0 es 1.2202849358728105
    La raiz 10-esima de 6.0 es 1.1962311988513155
    La raiz 11-esima de 6.0 es 1.1769039562428527
    La raiz 12-esima de 6.0 es 1.1610366723739942
    La raiz 13-esima de 6.0 es 1.1477777154347986
    La raiz 14-esima de 6.0 es 1.1365334760097243
    La raiz 15-esima de 6.0 es 1.1268776101908264
    La raiz 16-esima de 6.0 es 1.1184960459738218
    La raiz 17-esima de 6.0 es 1.1111523342970424
    La raiz 18-esima de 6.0 es 1.1046650785974952
    La raiz 19-esima de 6.0 es 1.0988928027655247
    La raiz 20-esima de 6.0 es 1.0937235477264424
    La raiz 21-esima de 6.0 es 1.0890675587944523
    La raiz 22-esima de 6.0 es 1.0848520434800557
    La raiz 23-esima de 6.0 es 1.0810173469046067
    La raiz 24-esima de 6.0 es 1.0775141170184241
    La raiz 25-esima de 6.0 es 1.0743011732208552
    La raiz 26-esima de 6.0 es 1.0713438829035236
    La raiz 27-esima de 6.0 es 1.0686129101356392
    La raiz 28-esima de 6.0 es 1.0660832406569969
    La raiz 29-esima de 6.0 es 1.063733414541692
    La raiz 30-esima de 6.0 es 1.0615449167090512
    La raiz 31-esima de 6.0 es 1.0595016886637296
    La raiz 32-esima de 6.0 es 1.0575897342418854
    La raiz 33-esima de 6.0 es 1.0557967989083417
    La raiz 34-esima de 6.0 es 1.0541121070820896
    La raiz 35-esima de 6.0 es 1.0525261456012585
    La raiz 36-esima de 6.0 es 1.0510304841428222
    La raiz 37-esima de 6.0 es 1.0496176254437533
    La raiz 38-esima de 6.0 es 1.0482808797099776
    La raiz 39-esima de 6.0 es 1.0470142587761369
    La raiz 40-esima de 6.0 es 1.045812386485474
    La raiz 41-esima de 6.0 es 1.0446704224624213
    La raiz 42-esima de 6.0 es 1.0435839969999792
    La raiz 43-esima de 6.0 es 1.042549155216214
    La raiz 44-esima de 6.0 es 1.0415623089763069
    La raiz 45-esima de 6.0 es 1.0406201953489853
    La raiz 46-esima de 6.0 es 1.039719840584283
    La raiz 47-esima de 6.0 es 1.038858528775155
    La raiz 48-esima de 6.0 es 1.0380337745075658
    La raiz 49-esima de 6.0 es 1.0372432989191824
    La raiz 50-esima de 6.0 es 1.0364850086811943
    La raiz 51-esima de 6.0 es 1.0357569774952138
    La raiz 52-esima de 6.0 es 1.0350574297610367
    La raiz 53-esima de 6.0 es 1.0343847261238408
    La raiz 54-esima de 6.0 es 1.0337373506532688
    La raiz 55-esima de 6.0 es 1.0331138994434157
    La raiz 56-esima de 6.0 es 1.0325130704533463
    La raiz 57-esima de 6.0 es 1.0319336544334674
    La raiz 58-esima de 6.0 es 1.0313745268047354
    La raiz 59-esima de 6.0 es 1.0308346403759792
    La raiz 60-esima de 6.0 es 1.0303130188001368
    La raiz 61-esima de 6.0 es 1.0298087506834
    La raiz 62-esima de 6.0 es 1.0293209842725104
    La raiz 63-esima de 6.0 es 1.0288489226550819
    La raiz 64-esima de 6.0 es 1.0283918194160655
    La raiz 65-esima de 6.0 es 1.0279489747005777
    La raiz 66-esima de 6.0 es 1.027519731639418
    La raiz 67-esima de 6.0 es 1.0271034730988913
    La raiz 68-esima de 6.0 es 1.0266996187211181
    La raiz 69-esima de 6.0 es 1.0263076222249912
    La raiz 70-esima de 6.0 es 1.0259269689413855
    La raiz 71-esima de 6.0 es 1.0255571735592441
    La raiz 72-esima de 6.0 es 1.0251977780617856
    La raiz 73-esima de 6.0 es 1.0248483498343846
    La raiz 74-esima de 6.0 es 1.0245084799276936
    La raiz 75-esima de 6.0 es 1.0241777814613477
    La raiz 76-esima de 6.0 es 1.0238558881551532
    La raiz 77-esima de 6.0 es 1.0235424529760397
    La raiz 78-esima de 6.0 es 1.0232371468902683
    La raiz 79-esima de 6.0 es 1.0229396577114687
    La raiz 80-esima de 6.0 es 1.0226496890360228
    La raiz 81-esima de 6.0 es 1.0223669592581706
    La raiz 82-esima de 6.0 es 1.0220912006579554
    La raiz 83-esima de 6.0 es 1.021822158555803
    La raiz 84-esima de 6.0 es 1.0215595905281194
    La raiz 85-esima de 6.0 es 1.0213032656788383
    La raiz 86-esima de 6.0 es 1.0210529639623078
    La raiz 87-esima de 6.0 es 1.0208084755533517
    La raiz 88-esima de 6.0 es 1.0205696002607108
    La raiz 89-esima de 6.0 es 1.0203361469804202
    La raiz 90-esima de 6.0 es 1.0201079331859866
    La raiz 91-esima de 6.0 es 1.0198847844525065
    La raiz 92-esima de 6.0 es 1.0196665340121167
    La raiz 93-esima de 6.0 es 1.0194530223384006
    La raiz 94-esima de 6.0 es 1.0192440967575702
    La raiz 95-esima de 6.0 es 1.019039611084432
    La raiz 96-esima de 6.0 es 1.0188394252813178
    La raiz 97-esima de 6.0 es 1.0186434051383018
    La raiz 98-esima de 6.0 es 1.018451421973175
    La raiz 99-esima de 6.0 es 1.0182633523497657
    La raiz 100-esima de 6.0 es 1.0180790778133073



```python
num = ['1','2','3','4','5','6','7','8','9','0']
sim = ['?','!','$''%','&','/','ª','º']
def validar(nomap):
    for x in nomap:
        if x in num:
            print('Nombre no valido!!!')
        elif x in sim:
            print('Nombre no valido')
        else:
            print('Nombre Correcto')
            
nom = input('Ingrese su nombre:')
validar(nom) 
apell = input('Ingrese su apellido: ')
validar(apell)
       

```

    Ingrese su nombre: Paco


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
