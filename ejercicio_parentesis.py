# -*- coding: utf-8 -*-
from Pila import Pila
from Utilidades import SuppressPrint


def hay_balanceo_de_parentesis(texto = "" ) -> bool:
    # Creamos la pila de control de paréntesis: ( ; [ ; {
    pila_control = Pila()

    """
        Si encontramos un paréntesis de apertura, lo incorporamos a la pila mediante push()
        Si encontramos un paréntesis de cierre, iniciamos una extracción del último elemento de la pila mediante  pop(). 
            Comprobamos si el cierre se corresponde con la última apertura incorporada a la pila
                Si la correspondencia es correcta ==> el texto sigue balanceado
                Si no ==> el texto no está balanceado y dejamos de analizar
    """

    balanceado = True  # estado inicial del texto
    # contador_push = 0

    # literal constante para disponer de un código más legible
    ESTADO_PILA_MSJ = "\t" * 20 + "ESTADO DE LA PILA: "

    """
    Solución de correspondencia mediante listas paralelas
    aperturas = ['(', '[', '{' ]
    cierres =   [')', ']', '}'] 
    print(cierres.index(']'))
    """

    # Mejor solución, mediante diccionario (Clave:Valor)
    parejas = {"(": ")", "[": "]", "{": "}"}

    for letra_leida in texto:
        # Leemos letra a letra del texto y si la letra leída se corresponde con paréntesis de apertura, lo incorporamos a la pila
        if letra_leida in parejas.keys():
            pila_control.push(letra_leida)  # incorporamos a la pila
            print(f"\n{letra_leida} es de apertura ==> hacemos push")
            print(ESTADO_PILA_MSJ + str(pila_control))

        elif letra_leida in parejas.values():
            print(letra_leida + " es de cierre ==> hacemos pop y comprobamos ")
            letra_extraida = pila_control.pop() # extraemos el último elemento incorporado a la pila

            # en caso de que la pila no devuelva elementos por estar vacía cerramos el bucle
            if letra_extraida == None:
                balanceado = False
                break

            print("Letra extraida: " + letra_extraida + "  es igual a? " + letra_leida)
            print(ESTADO_PILA_MSJ + " después de pop: " + str(pila_control))

            # if(aperturas.index(letra_extraida) == cierres.index(letra) ):
            if parejas[letra_extraida] == letra_leida:
                print("\nDe momento está balanceado")
                balanceado = True
            else:
                print("De momento NO está balanceado")
                balanceado = False
                break
    return balanceado


def main(modo_verboso = True):
    # Textos para pruebas
    texto1 = "| Entrada | Salida |"
    texto2 = "| --- | --- |"
    texto3 = "| (Hola 1234 mundo) | La cadena está balanceada. |"
    texto4 = "| (a f 6)(s b 6)"
    texto5 = "| (()()) |"
    texto6 = "| ((()) | La cadena no está balanceada. |"
    texto7 = "| (a)b) | La cadena no está balanceada. |"
    texto8 = "| ((( | La cadena no está balanceada. |"
    texto9 = "| (((( | La cadena no está balanceada |"
    texto10 = "| {[()]} | "
    texto11 = "| {[(]} | La cadena no está balanceada. |"
    texto12 = "En la programación, es crucial que los paréntesis (corchetes y llaves también) estén balanceados para que el código se ejecute correctamente. Por ejemplo, una función que comienza con { pero nunca se cierra con } provocará un error. Lo mismo ocurre con los paréntesis en expresiones matemáticas: (3 + 2] es incorrecto y puede causar confusiones o errores en el procesamiento. Asegúrate de que cada símbolo de apertura tenga su correspondiente cierre y estén en el orden correcto, como en )a * (b + c)) donde todo está balanceado."

    # lista de textos para automatizar las pruebas
    textos = [ texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8, texto9, texto10, texto11, texto12 ]
    resultados = []
    i = 0
    for texto in textos:
        #separador = "\t" * 40
        separador = ''

        esta_balanceado = True
        if not modo_verboso: 
            with SuppressPrint():
                esta_balanceado = hay_balanceo_de_parentesis(texto)
        else: 
            esta_balanceado = hay_balanceo_de_parentesis(texto)
            print("\n" + "=" * 100 + "\n")

        resultados.append(f"{separador}El texto{i} está balanceado? {esta_balanceado} ")
        i += 1

    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    modo_verboso = True
    main(modo_verboso)