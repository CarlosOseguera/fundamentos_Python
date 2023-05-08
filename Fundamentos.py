def nuevotema(tema):
    print("\n---------", tema,"---------\n")

if __name__ == "__main__":

    #Operadores aritméticos
    nuevotema("Operadores aritmeticos")
    print("Operador suma, 5 + 3 =",5+3)
    print("Operador resta 10 - 2 =", 10-2)
    print("Operador multiplicación 3 * 3 =", 3*3)
    print("Operador división 20 / 3", 20/3)
    print("Operador división entera 20 // 3 =", 20//3)
    print("Operador módulo 20 % 3 =", 20%3)
    #Operadores Logicos
    nuevotema("Operadores Logicos")
    print("True and True", True and True)
    print("True and False", True and False)
    print("False and True", False and True)
    print("False and Flase", False and False)
    print("not True", not True)
    print("not False", not False)
    print("True or True", True or True)
    print("True or False", True or False)
    print("False or True", False or True)
    print("False or False", False or False)
    #Ejercicios de comparacion
    nuevotema("Ejercicios de comparación")
    print("1==2", 1==2)
    print("1¡=2", 1!=2)
    print ("1>2", 1>2)
    print ("1>=2", 1>=2)
    print ("1<2", 1<2)
    print ("1<=2", 1<=2)
    #Variables
    nuevotema("Variables")
    Variable1= 10
    _Variable2= 6.2547
    Variable3= "pepe"
    print(Variable1,_Variable2,Variable3)
    a, b, c = 5, 10.8, "Hola"
    print (a)
    print (b)
    print (c)
    #Enteros
    nuevotema("Enteros")
    w, x, y, z, h = 105, 78658965235632, -256, 0b00110011, 0xff
    print (w, type (w))
    print (x,type (x))
    print (y,type (y))
    print (z,type (z))
    print (h,type (z))
    #Flotantes
    nuevotema ("Flotantes")
    x= 1234.56
    print (x, type (x))
    y= 9874.56
    print (y, type(y))
    #Números complejos
    nuevotema("Numeros complejos")
    x, y, z = -46j, 12+45j, 2j
    print (x, type(x))
    print (y, type(y))
    print (z, type(z))
    #Booleanos
    nuevotema("Booleanos")
    lis = (5)
    print(lis, "is", bool(lis))
    #Listas
    nuevotema("Listas")
    a = [10, 20, 5, "Python List"]
    print(a)
    print(a[1])
    a[1] = "Hola"
    print(a)
    #Tuplas
    nuevotema("Tuplas")
    t = (25, "Tupla", 1 + 10j)
    print (t)
    print (t[1])
    #t[1] = "Hola" Operacion no valida en tuplas.
    #prin(t)
    #Cadenas
    nuevotema("Cadenas")
    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto también es una cadena'
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena1[5])
    #Cadena multilinea
    nuevotema("Cadena Multilinea")
    cadenaMultilinea = '''Esto es una cadena
    de varias lineas    con         tabulares 
    saltos
    de
    linea'''
    print(cadenaMultilinea, type(cadenaMultilinea))
    cadena3 = "Hola" * 5
    print(cadena3)
    #Conjuntos
    nuevotema ("Conjuntos")
    Conjunto = {10, 20, 30, 40, 10, 50}
    print(Conjunto)
    #Diccionarios
    nuevotema("Diccionarios")
    diccionario = {"Nombre": "Conrado",
                   "Edad":38,
                   "Tel" : 3356454888}
    print(diccionario)
    print(diccionario["Nombre"])

