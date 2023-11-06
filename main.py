from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("CalculadoraPOO")
num = ""
operation = ""

indice = 0

#Funciones
def getNumero(n):
    global indice
    pantalla.insert(indice,n)
    indice += 1
    
def getOperacion(operator):
    global indice, operation
    operation = operator
    pantalla.insert(indice,operator)
    indice+= 1

def calcular():
    global operation
    estado = True
    num1 = ""
    num2 = ""
    estado = pantalla.get()
    pantalla.delete(0, "end")
    for i in estado:
        if(i != operation and estado):
            num1 += i
        elif(i==operation):
            estado = False
        else:
            num2 += i
    
    if(num1 == ""):
        return
    if(num2 == ""):
        return
    if(num1 != "" and num2 != ""):
        for s in num1:
            if(s == "."):
                num1 = float(num1)
                break
        for l in num2:
            if(l == "."):
                num2 = float(num2)
                break
        
        if(type(num1) == str): 
            num1 = int(num1)
            
        if(type(num2) == str): 
            num2 = int(num2)
    
    resultado = 0
    if(operation == "+"):
        resultado = num1 + num2
    elif(operation == "-"):
        resultado = num1 - num2
    elif(operation=="*"):
        resultado = num1 * num2
    elif(operation == "/"):
        resultado = num1 / num2
    
    pantalla.insert(0,resultado)
                
#root.resizable(0,0)
root.geometry("400x270")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"),textvariable=num)
pantalla.grid(row=0, column=0, columnspan=8, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", command=lambda:getNumero(1), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1,sticky="WE")
boton_2 = Button(root, text="2", command=lambda:getNumero(2), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1,sticky="WE")
boton_3 = Button(root, text="3", command=lambda:getNumero(3), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1,sticky="WE")
boton_4 = Button(root, text="4", command=lambda:getNumero(4), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1,sticky="WE")
boton_5 = Button(root, text="5", command=lambda:getNumero(5), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1,sticky="WE")
boton_6 = Button(root, text="6", command=lambda:getNumero(6), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1,sticky="WE")
boton_7 = Button(root, text="7", command=lambda:getNumero(7), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1,sticky="WE")
boton_8 = Button(root, text="8", command=lambda:getNumero(8), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1,sticky="WE")
boton_9 = Button(root, text="9", command=lambda:getNumero(9), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1,sticky="WE")
boton_igual = Button(root, text="=", command=lambda:calcular(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky="WE")
boton_punto = Button(root, text=".", command=lambda:getNumero("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1,sticky="WE")
boton_mas = Button(root, text="+", command=lambda:getOperacion("+"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1,sticky="WE")
boton_menos = Button(root, text="-", command=lambda:getOperacion("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1,sticky="WE")
boton_multiplicacion = Button(root, text="*", command=lambda:getOperacion("*"),  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1,sticky="WE")
boton_division = Button(root, text="/", command=lambda:getOperacion("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1,sticky="WE")

root.mainloop()