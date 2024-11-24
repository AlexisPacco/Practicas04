```python
# Estructura Iterativa - Bucle "for"
for <var> in <iterable>:
    <codigo>
    <codigo>
    .....................
```


      Cell In[1], line 2
        for <var> in <iterable>:
            ^
    SyntaxError: invalid syntax




```python
# 'for' iterando una lista
num = [6, 23, 89, 120]
for n in num:
    print(n)

```

    6
    23
    89
    120



```python
# 'for' iterando un string
nom = "Maximiliano"
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
# 'for' hallando la longitud de los elementos de una lista
for nombre in ['Milita', 'Luisito', 'Pablito', 'Alexandito']:
    print('Hola {0}, la longitud de tu nombre es de: {1} caracteres. '.format(nombre,len(nombre)))

```

    Hola Milita, la longitud de tu nombre es de: 6 caracteres. 
    Hola Luisito, la longitud de tu nombre es de: 7 caracteres. 
    Hola Pablito, la longitud de tu nombre es de: 7 caracteres. 
    Hola Alexandito, la longitud de tu nombre es de: 10 caracteres. 



```python
# lista de colores
colo = ["amarillo", "rojo", "verde", "azul", "purpura", "blanco", "negro", "limon"]
# nueva lista
color_con_r = []

for n in colo:
    if 'r' in n:
        color_con_r.append(n)

print(color_con_r)

```

    ['amarillo', 'rojo', 'verde', 'purpura', 'negro']



```python
# Funcion range()

# 'for' utilizando la funcion 'range' con 1 parametro
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
# Podemos usar un argumento
# añadir el parametro end="" para que por defecto no genere una nueva linea

for i in range(10):
    print(i + 1, "", end="")

```

    1 2 3 4 5 6 7 8 9 10 


```python
# Podemos usar dos valores para definir el inicio y el final

for i in range(1, 11):
    print(i, "", end="")

```

    1 2 3 4 5 6 7 8 9 10 


```python
# Podemos usar 3 para definir un inicio, un final y una longitud de paso(en este caso 2)

for i in range(2, 12, 2):
    print(i, "", end="")

```

    2 4 6 8 10 


```python
# inicio=20, un final=0 y una longitud de paso -2
for i in range(20, 0, -2):
    print(i, "", end="")
```

    20 18 16 14 12 10 8 6 4 2 


```python
# inicio=40, un final=-5 y una longitud de paso -5
for i in range(40, -5, -5):
    print(i, "",end="")
```

    40 35 30 25 20 15 10 5 0 


```python
# inicio=50, un final=-1 y una longitud de paso 5
for i in range(50,-1,5):
    print(i, "", end="")

```


```python
# Modificando la  iteracion del bucle for: break y contuniue

#lista de numero
lista = [2, 4, 5, 7, 8, 9, 3, 4]

# utilizaremos un contador iniciamos en 0 o en -1??
cont = -1

for m in lista:
    cont = cont + 1
    if m == 9:
        break

print(cont)

```

    5



```python
contador = 1
# contador = contador + 1
contador /= 5                # Hay abreviaturas similares para -=, *=, /=, //= y %=:
c=1
c+=1
print(c)

```

    2



```python
# lista de numeros sin el numero '9'
lista = [2, 4, 5, 7, 8, 19, 3, 4]

# utilizamos un contador reducido
cont = -1

for m in lista:
    cont += 1
    if m == 9:
        break
else:
## Usamos 'for' conjuntamente con 'else'
    cont = -1
    print("No se encontro el numero 9")

if cont >= 0:
    print(cont)


## Usamos 'for' conjuntamente con 'else'

```

    No se encontro el numero 9



```python
## Hacer un programa de una lista de numeros imprima solo numeros pares:

# lista de numeros
num = [12, 14, 15, 27, 108, 90, 33, 49, 200]

for p in num:
    if p % 2 != 0:
        continue
    print(p)

```

    12
    14
    108
    90
    200



```python

```
