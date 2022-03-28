productos=["A","B","C"]
valores=[270,340,390]
cuantas=int(input("Cuantas monedas va a ingresar: "))
pro=input("Elija producto: ") #"A"
pos=productos.index(pro)  # 0
costo=Valores[pos]  # 270
monedas=float(input("Ingrese monedas: ").split(","))  # [100.10,50,100,100 = 360]
entregado=0
for moneda in monedas:
    entregado+= int(moneda)
vuelto=entregado - costo
listaVuelto=[] # 50 10 10 10 10
if vuelto >0:

    while( vuelto!=0 ): # 0
        if (vuelto >=100):
           vuelto-=100
           listaVuelto.append("100")
        elif(vuelto >=50):
           vuelto-=50
           listaVuelto.append("50")
        else:
           vuelto-=10
           listaVuelto.append("10")
        print("Su vuelto: ",vuelto)
        unido=",".join(listaVuelto)
        print(unido)



else:
    print("Compra Realizada")