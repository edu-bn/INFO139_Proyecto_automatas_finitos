class AFD:
    def __init__(self, estados, alfabeto,transiciones, estado_inicial, estados_finales):
        self.estados = estados #set
        self.alfabeto = alfabeto #set
        self.transiciones = transiciones #diccionario {(estado_actual,transicion): estado a ir}
        self.estado_inicial = estado_inicial #variable
        self.estados_finales = estados_finales #set

    def validar_palabra(self, palabra):
        estado_actual = self.estado_inicial
        for simbolo in palabra: #iterar palabra
            if (estado_actual, simbolo) in self.transiciones: #si existe la transicion leyendo el simbolo
                estado_actual = self.transiciones[(estado_actual, simbolo)] # estado actual = valor en (estado_actual, simbolo)
            else:
                return False
        return estado_actual in self.estados_finales

    
def pedir_datos():
    # Solicitar al usuario los estados y el alfabeto
    estados = set(input("Ingrese los estados separados por comas: ").strip().split(','))
    while ( "" in estados):
        estados = set(input("ERROR, no ingrese elementos vacios(',,' o terminado en coma): ").strip().split(','))
    alfabeto = set(input("Ingrese el alfabeto separado por comas: ").strip().split(','))
    while ( "" in alfabeto):
        estados = set(input("ERROR, no ingrese elementos vacios(',,' o terminado en coma): ").strip().split(','))
    # Solicitar al usuario las transiciones
    transiciones = {}
    while True:
        lista = input("Ingrese una transición en el formato 'estado, símbolo, nuevo estado' (o 'fin' para terminar): ")
        if lista.lower() == 'fin':
            break
        lista = lista.strip().split(',')
        if len(lista) != 3:
            print("Formato no válido")
            continue
        estado = lista[0]
        simbolo = lista[1]
        nuevo_estado = lista[2]
        if simbolo not in alfabeto or estado not in estados or nuevo_estado not in estados:
            print("Transición no válida")
        elif (estado, simbolo) in transiciones:
            print(f"Simbolo ya utilizado en el estado: {estado}")
        else:
            transiciones[(estado, simbolo)] = nuevo_estado

    # Solicitar al usuario el estado inicial y los estados finales
    estado_inicial = input("Ingrese el estado inicial: ")
    while(estado_inicial not in estados):
        print("estado inicial no valido")
        estado_inicial = input("Ingrese el estado inicial: ")
        
    estados_finales = set(input("Ingrese los estados finales separados por comas: ").strip().split(','))
    while not estados_finales.issubset(estados):
        print("estado final no valido")
        estados_finales = set(input("Ingrese los estados finales separados por comas: ").strip().split(','))

    # Crear el AFD
    mi_AFD = AFD(estados, alfabeto, transiciones, estado_inicial, estados_finales)
    return mi_AFD
    
    
if __name__ == '__main__':
    #TKinter
    mi_AFD = pedir_datos()

    while True:
        palabra = input("Ingrese una palabra para validar (o 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break
        print("¿La palabra '{}' es aceptada? {}".format(palabra, mi_AFD.validar_palabra(palabra)))
