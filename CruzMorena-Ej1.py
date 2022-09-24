'''
Desarrollar una funciónrecursiva para duplicar los valores pares de una lista (NO crear una lista nueva).
Ejemplo:duplicar_pares([1,2,3,4,5,-8,10,0]) --> [1,4,3,8,5,-16,20,0].
'''
import random
#FUNCIONES
'''FUNCION PARA VALIDAR QUE UN NUMERO CUMPLA CON UNA CONDICION'''
def ValidarUnicaCondicion(Cond):
    '''
    pre: Se recibe una condicion minima (valor minimo que limita al valor recibido) y un valor.
    pos: Se devuelve el valor el cual se confirmo que es mayor a la condicion.
    '''
    iValor=int(input("Ingrese un valor:"))
    while iValor<Cond:
        iValor=int(input("Error- Se ingreso un numero invalido, vuelva a intentarlo:"))
    return iValor

'''FUNCION PARA CREAR UNA LISTA CON N NUMEROS AL AZAR DENTRO DE UN RANGO PREINGRESADO'''
def CrearListaAzar():
    '''
    pre: Se recibe un numero minimo para el rango de valores y un maximo.
    pos: Se devuelve una lista cargada de N cantidad de numeros al azar dentro del rango preestablecido.
    '''
    lNumerosAzar=[] #Creo la lista a llenar
    iMin= int(input("Cual es el numero minimo que desea que se genere dentro de la lista:"))
    print("Ahora necesito el numero maximo que desea que se genere")
    iMax= ValidarUnicaCondicion(iMin) #Establezco el numero minimo y el maximo que se generaran al azar.
    print("Ahora estableceremos la cantidad de numeros que contendra la lista")
    iCantidad=ValidarUnicaCondicion(0) #Aca le pregunta al usuario la cantidad de numeros que quiere que contenga.
    for i in range(iCantidad): #Agrega tantos numeros al azar, como indique N
        iAzar=random.randint (iMin,iMax)
        lNumerosAzar.append(iAzar)
    return lNumerosAzar #Devuelve la lista resultante

'''FUNCION PARA DUPLICAR VALORES PARES QUE APARECEN DENTRO DE UNA LISTA'''
def DuplicarPares (Lista,p=0):
    '''
    pre: Se recibe una lista de la cual se van a duplicar los valores pares y el numero de posicion de la cual vamos a ver si es par o no.
    pos: Se duplican los valores pares dentro de la misma lista. No se retorna nada ya que se trata de un parametro mutable.
    '''
    iTotalValores= len(Lista) #Vemos cuantos elementos se contienen en la lista para poder usar este numero para comparar.
    if iTotalValores==0: #Si la lista esta vacia, no es necesario duplicar ningun numero.
        print("Se ingreso una lista vacia, no tiene numeros para duplicar")
    elif iTotalValores!= p: #Si la posicion de la que estamos hablando es distinta del numero total de elementos (Cuando sea igual se dara el caso base).
        iValor=Lista[p]
        if (iValor%2)==0 and iValor!=0: #Revisamos si el numero es disible por 2 o no.
            Lista[p]=iValor*2 #Se duplica el numero si es par.
        NuevaPosicion=p+1 
        DuplicarPares(Lista,NuevaPosicion) #Caso recursivo.

#CODIGO PRINCIPAL
def main():
    pLista=CrearListaAzar()
    print()
    print("La lista creada al azar es:", pLista)
    print()
    DuplicarPares(pLista)
    print("La nueva lista duplicada es:", pLista)

if __name__=="__main__":
    main()
            

