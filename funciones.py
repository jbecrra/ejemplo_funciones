def sumar_2_numeros():
    num1=validar_numero()
    num2=validar_numero()
    total=num1+num2
    print("FUNCION: El total de la suma es:",total)

def restar_2_numeros(p_num1:float,p_num2:float=0):
    total=p_num1-p_num2
    print("FUNCION: El total de la resta es:",total)

def multiplicar_2_numeros():
    num1=validar_numero()
    num2=validar_numero()
    total=num1*num2
    return total
        
def dividir_2_numeros(p_num1:int,p_num2:int):
    total=p_num1/p_num2
    return total

def validar_numero():
    while True:
        try:
            num=float(input("Ingrese número: "))
            break
        except:
            print("ERROR! debe ingresar un número entero")
    return num

def menu():
    print("MENU")
    print("1. sumar 2 numeros")
    print("2. restar 2 numeros")
    print("3. multiplicar 2 numeros")
    print("4. dividir 2 numeros")  

def validar_opciones(opciones):
    while True:
        try:
            opc=int(input("ingrese opcion: "))
            if opc in opciones:
                break
            else:
                print("ERROR! opcion incorrecta")
        except:
            print("ERROR! debe ingresar un número entero")
    return opc