# ordenar.py · plantilla inicial
# Paso 1: comparar dos números y mostrarlos de menor a mayor
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c= int(input("Tercer número: "))

if a <= b:
    if b>= c and c>=a:
        print(a,c,b)
    elif b>=c and c<=a:
        print(c, a, b)
    else:
        print(a,b,c)
elif b <= a:
    if c>=b and c<=a:
        print(b,c,a)
    elif c>=b and a<=c:
        print(b,a,c)
    else:
        print(c,b,a)
else:
    print("compruebe su input")

# Paso 2 (con tu TL): pide un tercer número c y muestra los tres de menor a mayor.
# Solo con if, else y comparaciones: sin listas, ciclos ni sorted().