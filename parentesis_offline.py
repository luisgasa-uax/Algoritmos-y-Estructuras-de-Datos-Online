from Pila import Pila

#texto = 'hd(asdf(dfga)adf(adfad)daff)afd'
texto = 'asdf(asdfasd(gjdfth)sfg sd fg( adfga dfg adfg) adf gdafg  adfa dsg )'

'''
aperturas = '([{'
cierres =   ')]}'
'''

parentesis = { ')':'(' ,']':'[', '}':'{' }


pila = Pila()
for letra in texto:
    if letra in parentesis.values():
        pila.push(letra)
    if letra in parentesis.keys():
        extraida = pila.pop()
        if extraida :
            #if aperturas.index(extraida) == cierres.index(letra):
            if parentesis[letra] == extraida:
                print( 'de momento vamos bien')
            else: 
                print('La cadena NOOO está balanceada')
        else: 
            print('¡Qué barbaridad!!!')

if not pila.is_empty():
    print("No está balanceado")
else:
    print('La cadena SIIIIUUU está balanceada')
