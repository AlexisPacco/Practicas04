```python
## Hacer un programa que ingrese por teclado un numero inicial y un numero final para generar un rango (una lista consecutiva de numeros que inicia y termina de acuerdo a los numeros ingresados

#funcion principal
def main():
    #solicitar que ingrese el numero inicial y final
    num_inicial = int(input("Ingrese el numero inicial: "))
    num_final = int(input("Ingrese el numero final: "))
    
    #funcion 'for'
    for num in range(num_inicial, num_final + 1):
        #llamamos a las funciones de verificacion y mostraremos el resultado
        if es_par(num):
            print(f"El numero {num} es par.")
        elif es_impar(num):
            print(f"El numero {num} es impar.")

#funcion para verificar si es un numero par
def es_par(numero):
    return numero % 2 == 0

#funcion para verificar si es un numero impar
def es_impar(numero):
    return numero % 2!= 0

#llamar a la funcion principal
main()

```

    Ingrese el numero inicial:  1
    Ingrese el numero final:  5


    El numero 1 es impar.
    El numero 2 es par.
    El numero 3 es impar.
    El numero 4 es par.
    El numero 5 es impar.



```python
## Hacer un Programa que imprima la tabla completa de multiplicar de un numero que se ingresa por teclado:

#funcion principal
def main():
    #funcion para solicitar un numero
    numero = int(input("Ingresa un numero: "))
    imprimir_tabla(numero)

#imprimir las tablas del 1 al 10
def imprimir_tabla(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#llamar a la funcion principal
main()

```

    Ingresa un numero:  5


    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50



```python
## Hacer un programa que solicite el ingreso de nombre y apellido

#funcion principal 'for'
def validar(nomap):
    for x in nomap:
        if x in num:
            print('Nombre o apellido no valido, contiene numeros')
            return False
        elif x in sim:
            print('Nombre o apellido no Valido, contiene simbolos extraños')
            return False
        else:
            print('Perfecto, ahora')
            return True
            
#verificar que el nombre o apellido no tenga numeros
num = ['1','2','3','4','5','6','7','8','9','0']

#verificar que el nombre o apellido no tenga simbolos extraños
sim = ['!','"','#','$','%','&','/','(',')',')','=','?','¡','°']

#funcion para solicitar un numero
def solicitar_nombre_apellido():
    while True:
        #Ingresar nombre
        nom = input('Ingrese su nombre: ')
        #llamar a la funcion
        if validar(nom):
            break
    while True:
        #Ingresar apellido
        apell = input('Ingrese su apellido: ')
        #llamar a la funcion
        if validar(apell):
            break

    print(f'Usted ingresó su nombre y apellido correctamente: {nom} {apell}')

#llamar a la funcion
solicitar_nombre_apellido()
```

    Ingrese su nombre:  Alexis


    Perfecto, ahora


    Ingrese su apellido:  Pacco


    Perfecto, ahora
    Usted ingresó su nombre y apellido correctamente: Alexis Pacco



```python
## Hacer un programa que verifique los comentarios de los alumnos EPIT:

#funcion para verificar el comentario
def verificar_comentario(com):
    #palabras negativas
    palabras_negativas = ['malo', 'pesimo', 'no', 'feo', 'horrible', 'terrible']
    #palabras positivas
    palabras_positivas = ['bueno', 'excelente', 'bien', 'fantastico', 'genial']
    com = com.lower()

    #funcion para verificar palabras
    for palabra in palabras_negativas:
        if palabra in com:
            print("Comentario NEGATIVO")
            return

    for palabra in palabras_positivas:
        if palabra in com:
            print("Comentario POSITIVO")
            return

    print("Comentario NEUTRO")

#solicitar el ingreso del comentario
com = input("Ingrese su comentario, alumno EPIT: ")
#llamar a la funcion
verificar_comentario(com)

```

    Ingrese su comentario, alumno EPIT:  Hola, jugaste bien


    Comentario POSITIVO



```python
## Hacer un programa que genere una lista aleatoria de hasta 60 numeros:

#funcion para generar lista aleatoria
def generar_lista(cantidad, limite_maximo):
    lista =[]
    for r in range(cantidad):
        num = (r * 9 + 7) % limite_maximo
        lista.append(num)
    return lista

#funcion para clasificar los numeros en listas
def clasificar_numeros(lista):
    multiplos_de_2 = []
    multiplos_de_3 = []
    multiplos_de_5 = []

    for numero in lista:
        if numero % 2 == 0:
            multiplos_de_2.append(numero)
        if numero % 3 == 0:
            multiplos_de_3.append(numero)
        if numero % 5 == 0:
            multiplos_de_5.append(numero)

    return multiplos_de_2, multiplos_de_3, multiplos_de_5

#solitar el numero de elementos para la lista
cantidad = int(input("Ingrese el numero de elementos (hasta 60): "))
limite_maximo = 100

#generar la lista aleatoria
lista_aleatoria = generar_lista(cantidad, limite_maximo)

#clasificar los numeros en las listas
multiplos_de_2, multiplos_de_3, multiplos_de_5 = clasificar_numeros(lista_aleatoria)

print("Lista aleatoria generada:", lista_aleatoria)
print("Multiplos de 2:", multiplos_de_2)
print("Multiplos de 3:", multiplos_de_3)
print("Multiplos de 5:", multiplos_de_5)

```

    Ingrese el numero de elementos (hasta 60):  15


    Lista aleatoria generada: [7, 16, 25, 34, 43, 52, 61, 70, 79, 88, 97, 6, 15, 24, 33]
    Multiplos de 2: [16, 34, 52, 70, 88, 6, 24]
    Multiplos de 3: [6, 15, 24, 33]
    Multiplos de 5: [25, 70, 15]



```python
## Hacer un programa que ingrese por teclado un numero inicial de 3 cifras y un numero final de 4 cifras para generar un rango:

#funcion para solicitar numeros de inicio y fin
numero_inicial = int(input("Ingrese un numero inicial de 3 cifras: "))
numero_final = int(input("Ingrese un numero final de 4 cifras: "))

#funcion para verificar si el numero es capicúa
def es_capicua(num):
    num_str = str(num)
    return num_str == num_str[::-1]

#verificar el numero inicial tiene 3 cifras y final 4 cifras
if 100 <= numero_inicial < 1000 and 1000 <= numero_final < 10000:
    for num in range(numero_inicial, numero_final + 1):
        if es_capicua(num):
            print(f"{num} es un numero capicua")
        else:
            print(f"{num} no es un numero capicua")

else:
    print("Por favor, ingrese un numero incial de 3 cifras y uno final de 4 cifras.")

```

    Ingrese un numero inicial de 3 cifras:  100
    Ingrese un numero final de 4 cifras:  1000


    100 no es un numero capicua
    101 es un numero capicua
    102 no es un numero capicua
    103 no es un numero capicua
    104 no es un numero capicua
    105 no es un numero capicua
    106 no es un numero capicua
    107 no es un numero capicua
    108 no es un numero capicua
    109 no es un numero capicua
    110 no es un numero capicua
    111 es un numero capicua
    112 no es un numero capicua
    113 no es un numero capicua
    114 no es un numero capicua
    115 no es un numero capicua
    116 no es un numero capicua
    117 no es un numero capicua
    118 no es un numero capicua
    119 no es un numero capicua
    120 no es un numero capicua
    121 es un numero capicua
    122 no es un numero capicua
    123 no es un numero capicua
    124 no es un numero capicua
    125 no es un numero capicua
    126 no es un numero capicua
    127 no es un numero capicua
    128 no es un numero capicua
    129 no es un numero capicua
    130 no es un numero capicua
    131 es un numero capicua
    132 no es un numero capicua
    133 no es un numero capicua
    134 no es un numero capicua
    135 no es un numero capicua
    136 no es un numero capicua
    137 no es un numero capicua
    138 no es un numero capicua
    139 no es un numero capicua
    140 no es un numero capicua
    141 es un numero capicua
    142 no es un numero capicua
    143 no es un numero capicua
    144 no es un numero capicua
    145 no es un numero capicua
    146 no es un numero capicua
    147 no es un numero capicua
    148 no es un numero capicua
    149 no es un numero capicua
    150 no es un numero capicua
    151 es un numero capicua
    152 no es un numero capicua
    153 no es un numero capicua
    154 no es un numero capicua
    155 no es un numero capicua
    156 no es un numero capicua
    157 no es un numero capicua
    158 no es un numero capicua
    159 no es un numero capicua
    160 no es un numero capicua
    161 es un numero capicua
    162 no es un numero capicua
    163 no es un numero capicua
    164 no es un numero capicua
    165 no es un numero capicua
    166 no es un numero capicua
    167 no es un numero capicua
    168 no es un numero capicua
    169 no es un numero capicua
    170 no es un numero capicua
    171 es un numero capicua
    172 no es un numero capicua
    173 no es un numero capicua
    174 no es un numero capicua
    175 no es un numero capicua
    176 no es un numero capicua
    177 no es un numero capicua
    178 no es un numero capicua
    179 no es un numero capicua
    180 no es un numero capicua
    181 es un numero capicua
    182 no es un numero capicua
    183 no es un numero capicua
    184 no es un numero capicua
    185 no es un numero capicua
    186 no es un numero capicua
    187 no es un numero capicua
    188 no es un numero capicua
    189 no es un numero capicua
    190 no es un numero capicua
    191 es un numero capicua
    192 no es un numero capicua
    193 no es un numero capicua
    194 no es un numero capicua
    195 no es un numero capicua
    196 no es un numero capicua
    197 no es un numero capicua
    198 no es un numero capicua
    199 no es un numero capicua
    200 no es un numero capicua
    201 no es un numero capicua
    202 es un numero capicua
    203 no es un numero capicua
    204 no es un numero capicua
    205 no es un numero capicua
    206 no es un numero capicua
    207 no es un numero capicua
    208 no es un numero capicua
    209 no es un numero capicua
    210 no es un numero capicua
    211 no es un numero capicua
    212 es un numero capicua
    213 no es un numero capicua
    214 no es un numero capicua
    215 no es un numero capicua
    216 no es un numero capicua
    217 no es un numero capicua
    218 no es un numero capicua
    219 no es un numero capicua
    220 no es un numero capicua
    221 no es un numero capicua
    222 es un numero capicua
    223 no es un numero capicua
    224 no es un numero capicua
    225 no es un numero capicua
    226 no es un numero capicua
    227 no es un numero capicua
    228 no es un numero capicua
    229 no es un numero capicua
    230 no es un numero capicua
    231 no es un numero capicua
    232 es un numero capicua
    233 no es un numero capicua
    234 no es un numero capicua
    235 no es un numero capicua
    236 no es un numero capicua
    237 no es un numero capicua
    238 no es un numero capicua
    239 no es un numero capicua
    240 no es un numero capicua
    241 no es un numero capicua
    242 es un numero capicua
    243 no es un numero capicua
    244 no es un numero capicua
    245 no es un numero capicua
    246 no es un numero capicua
    247 no es un numero capicua
    248 no es un numero capicua
    249 no es un numero capicua
    250 no es un numero capicua
    251 no es un numero capicua
    252 es un numero capicua
    253 no es un numero capicua
    254 no es un numero capicua
    255 no es un numero capicua
    256 no es un numero capicua
    257 no es un numero capicua
    258 no es un numero capicua
    259 no es un numero capicua
    260 no es un numero capicua
    261 no es un numero capicua
    262 es un numero capicua
    263 no es un numero capicua
    264 no es un numero capicua
    265 no es un numero capicua
    266 no es un numero capicua
    267 no es un numero capicua
    268 no es un numero capicua
    269 no es un numero capicua
    270 no es un numero capicua
    271 no es un numero capicua
    272 es un numero capicua
    273 no es un numero capicua
    274 no es un numero capicua
    275 no es un numero capicua
    276 no es un numero capicua
    277 no es un numero capicua
    278 no es un numero capicua
    279 no es un numero capicua
    280 no es un numero capicua
    281 no es un numero capicua
    282 es un numero capicua
    283 no es un numero capicua
    284 no es un numero capicua
    285 no es un numero capicua
    286 no es un numero capicua
    287 no es un numero capicua
    288 no es un numero capicua
    289 no es un numero capicua
    290 no es un numero capicua
    291 no es un numero capicua
    292 es un numero capicua
    293 no es un numero capicua
    294 no es un numero capicua
    295 no es un numero capicua
    296 no es un numero capicua
    297 no es un numero capicua
    298 no es un numero capicua
    299 no es un numero capicua
    300 no es un numero capicua
    301 no es un numero capicua
    302 no es un numero capicua
    303 es un numero capicua
    304 no es un numero capicua
    305 no es un numero capicua
    306 no es un numero capicua
    307 no es un numero capicua
    308 no es un numero capicua
    309 no es un numero capicua
    310 no es un numero capicua
    311 no es un numero capicua
    312 no es un numero capicua
    313 es un numero capicua
    314 no es un numero capicua
    315 no es un numero capicua
    316 no es un numero capicua
    317 no es un numero capicua
    318 no es un numero capicua
    319 no es un numero capicua
    320 no es un numero capicua
    321 no es un numero capicua
    322 no es un numero capicua
    323 es un numero capicua
    324 no es un numero capicua
    325 no es un numero capicua
    326 no es un numero capicua
    327 no es un numero capicua
    328 no es un numero capicua
    329 no es un numero capicua
    330 no es un numero capicua
    331 no es un numero capicua
    332 no es un numero capicua
    333 es un numero capicua
    334 no es un numero capicua
    335 no es un numero capicua
    336 no es un numero capicua
    337 no es un numero capicua
    338 no es un numero capicua
    339 no es un numero capicua
    340 no es un numero capicua
    341 no es un numero capicua
    342 no es un numero capicua
    343 es un numero capicua
    344 no es un numero capicua
    345 no es un numero capicua
    346 no es un numero capicua
    347 no es un numero capicua
    348 no es un numero capicua
    349 no es un numero capicua
    350 no es un numero capicua
    351 no es un numero capicua
    352 no es un numero capicua
    353 es un numero capicua
    354 no es un numero capicua
    355 no es un numero capicua
    356 no es un numero capicua
    357 no es un numero capicua
    358 no es un numero capicua
    359 no es un numero capicua
    360 no es un numero capicua
    361 no es un numero capicua
    362 no es un numero capicua
    363 es un numero capicua
    364 no es un numero capicua
    365 no es un numero capicua
    366 no es un numero capicua
    367 no es un numero capicua
    368 no es un numero capicua
    369 no es un numero capicua
    370 no es un numero capicua
    371 no es un numero capicua
    372 no es un numero capicua
    373 es un numero capicua
    374 no es un numero capicua
    375 no es un numero capicua
    376 no es un numero capicua
    377 no es un numero capicua
    378 no es un numero capicua
    379 no es un numero capicua
    380 no es un numero capicua
    381 no es un numero capicua
    382 no es un numero capicua
    383 es un numero capicua
    384 no es un numero capicua
    385 no es un numero capicua
    386 no es un numero capicua
    387 no es un numero capicua
    388 no es un numero capicua
    389 no es un numero capicua
    390 no es un numero capicua
    391 no es un numero capicua
    392 no es un numero capicua
    393 es un numero capicua
    394 no es un numero capicua
    395 no es un numero capicua
    396 no es un numero capicua
    397 no es un numero capicua
    398 no es un numero capicua
    399 no es un numero capicua
    400 no es un numero capicua
    401 no es un numero capicua
    402 no es un numero capicua
    403 no es un numero capicua
    404 es un numero capicua
    405 no es un numero capicua
    406 no es un numero capicua
    407 no es un numero capicua
    408 no es un numero capicua
    409 no es un numero capicua
    410 no es un numero capicua
    411 no es un numero capicua
    412 no es un numero capicua
    413 no es un numero capicua
    414 es un numero capicua
    415 no es un numero capicua
    416 no es un numero capicua
    417 no es un numero capicua
    418 no es un numero capicua
    419 no es un numero capicua
    420 no es un numero capicua
    421 no es un numero capicua
    422 no es un numero capicua
    423 no es un numero capicua
    424 es un numero capicua
    425 no es un numero capicua
    426 no es un numero capicua
    427 no es un numero capicua
    428 no es un numero capicua
    429 no es un numero capicua
    430 no es un numero capicua
    431 no es un numero capicua
    432 no es un numero capicua
    433 no es un numero capicua
    434 es un numero capicua
    435 no es un numero capicua
    436 no es un numero capicua
    437 no es un numero capicua
    438 no es un numero capicua
    439 no es un numero capicua
    440 no es un numero capicua
    441 no es un numero capicua
    442 no es un numero capicua
    443 no es un numero capicua
    444 es un numero capicua
    445 no es un numero capicua
    446 no es un numero capicua
    447 no es un numero capicua
    448 no es un numero capicua
    449 no es un numero capicua
    450 no es un numero capicua
    451 no es un numero capicua
    452 no es un numero capicua
    453 no es un numero capicua
    454 es un numero capicua
    455 no es un numero capicua
    456 no es un numero capicua
    457 no es un numero capicua
    458 no es un numero capicua
    459 no es un numero capicua
    460 no es un numero capicua
    461 no es un numero capicua
    462 no es un numero capicua
    463 no es un numero capicua
    464 es un numero capicua
    465 no es un numero capicua
    466 no es un numero capicua
    467 no es un numero capicua
    468 no es un numero capicua
    469 no es un numero capicua
    470 no es un numero capicua
    471 no es un numero capicua
    472 no es un numero capicua
    473 no es un numero capicua
    474 es un numero capicua
    475 no es un numero capicua
    476 no es un numero capicua
    477 no es un numero capicua
    478 no es un numero capicua
    479 no es un numero capicua
    480 no es un numero capicua
    481 no es un numero capicua
    482 no es un numero capicua
    483 no es un numero capicua
    484 es un numero capicua
    485 no es un numero capicua
    486 no es un numero capicua
    487 no es un numero capicua
    488 no es un numero capicua
    489 no es un numero capicua
    490 no es un numero capicua
    491 no es un numero capicua
    492 no es un numero capicua
    493 no es un numero capicua
    494 es un numero capicua
    495 no es un numero capicua
    496 no es un numero capicua
    497 no es un numero capicua
    498 no es un numero capicua
    499 no es un numero capicua
    500 no es un numero capicua
    501 no es un numero capicua
    502 no es un numero capicua
    503 no es un numero capicua
    504 no es un numero capicua
    505 es un numero capicua
    506 no es un numero capicua
    507 no es un numero capicua
    508 no es un numero capicua
    509 no es un numero capicua
    510 no es un numero capicua
    511 no es un numero capicua
    512 no es un numero capicua
    513 no es un numero capicua
    514 no es un numero capicua
    515 es un numero capicua
    516 no es un numero capicua
    517 no es un numero capicua
    518 no es un numero capicua
    519 no es un numero capicua
    520 no es un numero capicua
    521 no es un numero capicua
    522 no es un numero capicua
    523 no es un numero capicua
    524 no es un numero capicua
    525 es un numero capicua
    526 no es un numero capicua
    527 no es un numero capicua
    528 no es un numero capicua
    529 no es un numero capicua
    530 no es un numero capicua
    531 no es un numero capicua
    532 no es un numero capicua
    533 no es un numero capicua
    534 no es un numero capicua
    535 es un numero capicua
    536 no es un numero capicua
    537 no es un numero capicua
    538 no es un numero capicua
    539 no es un numero capicua
    540 no es un numero capicua
    541 no es un numero capicua
    542 no es un numero capicua
    543 no es un numero capicua
    544 no es un numero capicua
    545 es un numero capicua
    546 no es un numero capicua
    547 no es un numero capicua
    548 no es un numero capicua
    549 no es un numero capicua
    550 no es un numero capicua
    551 no es un numero capicua
    552 no es un numero capicua
    553 no es un numero capicua
    554 no es un numero capicua
    555 es un numero capicua
    556 no es un numero capicua
    557 no es un numero capicua
    558 no es un numero capicua
    559 no es un numero capicua
    560 no es un numero capicua
    561 no es un numero capicua
    562 no es un numero capicua
    563 no es un numero capicua
    564 no es un numero capicua
    565 es un numero capicua
    566 no es un numero capicua
    567 no es un numero capicua
    568 no es un numero capicua
    569 no es un numero capicua
    570 no es un numero capicua
    571 no es un numero capicua
    572 no es un numero capicua
    573 no es un numero capicua
    574 no es un numero capicua
    575 es un numero capicua
    576 no es un numero capicua
    577 no es un numero capicua
    578 no es un numero capicua
    579 no es un numero capicua
    580 no es un numero capicua
    581 no es un numero capicua
    582 no es un numero capicua
    583 no es un numero capicua
    584 no es un numero capicua
    585 es un numero capicua
    586 no es un numero capicua
    587 no es un numero capicua
    588 no es un numero capicua
    589 no es un numero capicua
    590 no es un numero capicua
    591 no es un numero capicua
    592 no es un numero capicua
    593 no es un numero capicua
    594 no es un numero capicua
    595 es un numero capicua
    596 no es un numero capicua
    597 no es un numero capicua
    598 no es un numero capicua
    599 no es un numero capicua
    600 no es un numero capicua
    601 no es un numero capicua
    602 no es un numero capicua
    603 no es un numero capicua
    604 no es un numero capicua
    605 no es un numero capicua
    606 es un numero capicua
    607 no es un numero capicua
    608 no es un numero capicua
    609 no es un numero capicua
    610 no es un numero capicua
    611 no es un numero capicua
    612 no es un numero capicua
    613 no es un numero capicua
    614 no es un numero capicua
    615 no es un numero capicua
    616 es un numero capicua
    617 no es un numero capicua
    618 no es un numero capicua
    619 no es un numero capicua
    620 no es un numero capicua
    621 no es un numero capicua
    622 no es un numero capicua
    623 no es un numero capicua
    624 no es un numero capicua
    625 no es un numero capicua
    626 es un numero capicua
    627 no es un numero capicua
    628 no es un numero capicua
    629 no es un numero capicua
    630 no es un numero capicua
    631 no es un numero capicua
    632 no es un numero capicua
    633 no es un numero capicua
    634 no es un numero capicua
    635 no es un numero capicua
    636 es un numero capicua
    637 no es un numero capicua
    638 no es un numero capicua
    639 no es un numero capicua
    640 no es un numero capicua
    641 no es un numero capicua
    642 no es un numero capicua
    643 no es un numero capicua
    644 no es un numero capicua
    645 no es un numero capicua
    646 es un numero capicua
    647 no es un numero capicua
    648 no es un numero capicua
    649 no es un numero capicua
    650 no es un numero capicua
    651 no es un numero capicua
    652 no es un numero capicua
    653 no es un numero capicua
    654 no es un numero capicua
    655 no es un numero capicua
    656 es un numero capicua
    657 no es un numero capicua
    658 no es un numero capicua
    659 no es un numero capicua
    660 no es un numero capicua
    661 no es un numero capicua
    662 no es un numero capicua
    663 no es un numero capicua
    664 no es un numero capicua
    665 no es un numero capicua
    666 es un numero capicua
    667 no es un numero capicua
    668 no es un numero capicua
    669 no es un numero capicua
    670 no es un numero capicua
    671 no es un numero capicua
    672 no es un numero capicua
    673 no es un numero capicua
    674 no es un numero capicua
    675 no es un numero capicua
    676 es un numero capicua
    677 no es un numero capicua
    678 no es un numero capicua
    679 no es un numero capicua
    680 no es un numero capicua
    681 no es un numero capicua
    682 no es un numero capicua
    683 no es un numero capicua
    684 no es un numero capicua
    685 no es un numero capicua
    686 es un numero capicua
    687 no es un numero capicua
    688 no es un numero capicua
    689 no es un numero capicua
    690 no es un numero capicua
    691 no es un numero capicua
    692 no es un numero capicua
    693 no es un numero capicua
    694 no es un numero capicua
    695 no es un numero capicua
    696 es un numero capicua
    697 no es un numero capicua
    698 no es un numero capicua
    699 no es un numero capicua
    700 no es un numero capicua
    701 no es un numero capicua
    702 no es un numero capicua
    703 no es un numero capicua
    704 no es un numero capicua
    705 no es un numero capicua
    706 no es un numero capicua
    707 es un numero capicua
    708 no es un numero capicua
    709 no es un numero capicua
    710 no es un numero capicua
    711 no es un numero capicua
    712 no es un numero capicua
    713 no es un numero capicua
    714 no es un numero capicua
    715 no es un numero capicua
    716 no es un numero capicua
    717 es un numero capicua
    718 no es un numero capicua
    719 no es un numero capicua
    720 no es un numero capicua
    721 no es un numero capicua
    722 no es un numero capicua
    723 no es un numero capicua
    724 no es un numero capicua
    725 no es un numero capicua
    726 no es un numero capicua
    727 es un numero capicua
    728 no es un numero capicua
    729 no es un numero capicua
    730 no es un numero capicua
    731 no es un numero capicua
    732 no es un numero capicua
    733 no es un numero capicua
    734 no es un numero capicua
    735 no es un numero capicua
    736 no es un numero capicua
    737 es un numero capicua
    738 no es un numero capicua
    739 no es un numero capicua
    740 no es un numero capicua
    741 no es un numero capicua
    742 no es un numero capicua
    743 no es un numero capicua
    744 no es un numero capicua
    745 no es un numero capicua
    746 no es un numero capicua
    747 es un numero capicua
    748 no es un numero capicua
    749 no es un numero capicua
    750 no es un numero capicua
    751 no es un numero capicua
    752 no es un numero capicua
    753 no es un numero capicua
    754 no es un numero capicua
    755 no es un numero capicua
    756 no es un numero capicua
    757 es un numero capicua
    758 no es un numero capicua
    759 no es un numero capicua
    760 no es un numero capicua
    761 no es un numero capicua
    762 no es un numero capicua
    763 no es un numero capicua
    764 no es un numero capicua
    765 no es un numero capicua
    766 no es un numero capicua
    767 es un numero capicua
    768 no es un numero capicua
    769 no es un numero capicua
    770 no es un numero capicua
    771 no es un numero capicua
    772 no es un numero capicua
    773 no es un numero capicua
    774 no es un numero capicua
    775 no es un numero capicua
    776 no es un numero capicua
    777 es un numero capicua
    778 no es un numero capicua
    779 no es un numero capicua
    780 no es un numero capicua
    781 no es un numero capicua
    782 no es un numero capicua
    783 no es un numero capicua
    784 no es un numero capicua
    785 no es un numero capicua
    786 no es un numero capicua
    787 es un numero capicua
    788 no es un numero capicua
    789 no es un numero capicua
    790 no es un numero capicua
    791 no es un numero capicua
    792 no es un numero capicua
    793 no es un numero capicua
    794 no es un numero capicua
    795 no es un numero capicua
    796 no es un numero capicua
    797 es un numero capicua
    798 no es un numero capicua
    799 no es un numero capicua
    800 no es un numero capicua
    801 no es un numero capicua
    802 no es un numero capicua
    803 no es un numero capicua
    804 no es un numero capicua
    805 no es un numero capicua
    806 no es un numero capicua
    807 no es un numero capicua
    808 es un numero capicua
    809 no es un numero capicua
    810 no es un numero capicua
    811 no es un numero capicua
    812 no es un numero capicua
    813 no es un numero capicua
    814 no es un numero capicua
    815 no es un numero capicua
    816 no es un numero capicua
    817 no es un numero capicua
    818 es un numero capicua
    819 no es un numero capicua
    820 no es un numero capicua
    821 no es un numero capicua
    822 no es un numero capicua
    823 no es un numero capicua
    824 no es un numero capicua
    825 no es un numero capicua
    826 no es un numero capicua
    827 no es un numero capicua
    828 es un numero capicua
    829 no es un numero capicua
    830 no es un numero capicua
    831 no es un numero capicua
    832 no es un numero capicua
    833 no es un numero capicua
    834 no es un numero capicua
    835 no es un numero capicua
    836 no es un numero capicua
    837 no es un numero capicua
    838 es un numero capicua
    839 no es un numero capicua
    840 no es un numero capicua
    841 no es un numero capicua
    842 no es un numero capicua
    843 no es un numero capicua
    844 no es un numero capicua
    845 no es un numero capicua
    846 no es un numero capicua
    847 no es un numero capicua
    848 es un numero capicua
    849 no es un numero capicua
    850 no es un numero capicua
    851 no es un numero capicua
    852 no es un numero capicua
    853 no es un numero capicua
    854 no es un numero capicua
    855 no es un numero capicua
    856 no es un numero capicua
    857 no es un numero capicua
    858 es un numero capicua
    859 no es un numero capicua
    860 no es un numero capicua
    861 no es un numero capicua
    862 no es un numero capicua
    863 no es un numero capicua
    864 no es un numero capicua
    865 no es un numero capicua
    866 no es un numero capicua
    867 no es un numero capicua
    868 es un numero capicua
    869 no es un numero capicua
    870 no es un numero capicua
    871 no es un numero capicua
    872 no es un numero capicua
    873 no es un numero capicua
    874 no es un numero capicua
    875 no es un numero capicua
    876 no es un numero capicua
    877 no es un numero capicua
    878 es un numero capicua
    879 no es un numero capicua
    880 no es un numero capicua
    881 no es un numero capicua
    882 no es un numero capicua
    883 no es un numero capicua
    884 no es un numero capicua
    885 no es un numero capicua
    886 no es un numero capicua
    887 no es un numero capicua
    888 es un numero capicua
    889 no es un numero capicua
    890 no es un numero capicua
    891 no es un numero capicua
    892 no es un numero capicua
    893 no es un numero capicua
    894 no es un numero capicua
    895 no es un numero capicua
    896 no es un numero capicua
    897 no es un numero capicua
    898 es un numero capicua
    899 no es un numero capicua
    900 no es un numero capicua
    901 no es un numero capicua
    902 no es un numero capicua
    903 no es un numero capicua
    904 no es un numero capicua
    905 no es un numero capicua
    906 no es un numero capicua
    907 no es un numero capicua
    908 no es un numero capicua
    909 es un numero capicua
    910 no es un numero capicua
    911 no es un numero capicua
    912 no es un numero capicua
    913 no es un numero capicua
    914 no es un numero capicua
    915 no es un numero capicua
    916 no es un numero capicua
    917 no es un numero capicua
    918 no es un numero capicua
    919 es un numero capicua
    920 no es un numero capicua
    921 no es un numero capicua
    922 no es un numero capicua
    923 no es un numero capicua
    924 no es un numero capicua
    925 no es un numero capicua
    926 no es un numero capicua
    927 no es un numero capicua
    928 no es un numero capicua
    929 es un numero capicua
    930 no es un numero capicua
    931 no es un numero capicua
    932 no es un numero capicua
    933 no es un numero capicua
    934 no es un numero capicua
    935 no es un numero capicua
    936 no es un numero capicua
    937 no es un numero capicua
    938 no es un numero capicua
    939 es un numero capicua
    940 no es un numero capicua
    941 no es un numero capicua
    942 no es un numero capicua
    943 no es un numero capicua
    944 no es un numero capicua
    945 no es un numero capicua
    946 no es un numero capicua
    947 no es un numero capicua
    948 no es un numero capicua
    949 es un numero capicua
    950 no es un numero capicua
    951 no es un numero capicua
    952 no es un numero capicua
    953 no es un numero capicua
    954 no es un numero capicua
    955 no es un numero capicua
    956 no es un numero capicua
    957 no es un numero capicua
    958 no es un numero capicua
    959 es un numero capicua
    960 no es un numero capicua
    961 no es un numero capicua
    962 no es un numero capicua
    963 no es un numero capicua
    964 no es un numero capicua
    965 no es un numero capicua
    966 no es un numero capicua
    967 no es un numero capicua
    968 no es un numero capicua
    969 es un numero capicua
    970 no es un numero capicua
    971 no es un numero capicua
    972 no es un numero capicua
    973 no es un numero capicua
    974 no es un numero capicua
    975 no es un numero capicua
    976 no es un numero capicua
    977 no es un numero capicua
    978 no es un numero capicua
    979 es un numero capicua
    980 no es un numero capicua
    981 no es un numero capicua
    982 no es un numero capicua
    983 no es un numero capicua
    984 no es un numero capicua
    985 no es un numero capicua
    986 no es un numero capicua
    987 no es un numero capicua
    988 no es un numero capicua
    989 es un numero capicua
    990 no es un numero capicua
    991 no es un numero capicua
    992 no es un numero capicua
    993 no es un numero capicua
    994 no es un numero capicua
    995 no es un numero capicua
    996 no es un numero capicua
    997 no es un numero capicua
    998 no es un numero capicua
    999 es un numero capicua
    1000 no es un numero capicua



```python
## Hacer un programa que solicite el ingreso del DNI de un ciudadano:

#funcion para solicitar y verificar el DNI
def solicitar_dni():
    while True:
        dni = input("Ingrese su DNI (8 digitos):")
        if dni_valido(dni):
            print("DNI ingresado valido.")
            break
        else:
            print("DNI invalido. Asegurese de ingresar 8 digitos numericos")

#funcion para verificar si el DNI es valido
def dni_valido(dni):
    if len(dni) != 8:
        return False
    #verificar que solo sean numeros
    for char in dni:
        if not char.isdigit():
            return False

    return True

#llamar a la funcion
solicitar_dni()

```

    Ingrese su DNI (8 digitos): kl


    DNI invalido. Asegurese de ingresar 8 digitos numericos


    Ingrese su DNI (8 digitos): 20240874


    DNI ingresado valido.



```python

```
