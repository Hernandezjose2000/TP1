from random import randint,uniform, shuffle

def fichas_juegos() -> list:
    
    #PRE: No recibe nada esta funcion
    #POST: Se encarga de retornar todas las fichas totales

    fichas  = [["violin","viola","cello","contrabajo","oboe","corno ingles","flauta","flauta picolo","faggote","clarinete","trompeta","trombon"],

    ["tuba","bateria","redoblantes","congas","timpani","piano","organo","xilofono","marimba","guitarra","cuatro","bajo electrico"],

    ["acordeon","ukelele","mandolina","mandola","arpa llanera","maracas","clave","gurrufio","flauta dulce","oboe de amor","contrafaggote","clarinete picolo"],

    ["clarinete bajo","trombon bajo","trombon picolo","tubas wagnerianas","triangulo","bon","clave","laud","lira","saxofon","clavecin","caja"],

    ["saxofon baritono","timbales","charango","pandereta","armonica","bongo","bombo","cortina","castanuelas","gong","cabasa","platos"],

    ["gaitas","tambor","cambus","guacharaca","platillos","timbales","arpa clasica","matraca","campanas","litofono","guitarron argentino","cacalatchtli"],

    ["violin","viola","cello","contrabajo","oboe","corno ingles","flauta","flauta picolo","faggote","clarinete","trompeta","trombon"],
    
    ["tuba","bateria","redoblantes","congas","timpani","piano","organo","xilofono","marimba","guitarra","cuatro","bajo electrico"],
    
    ["acordeon","ukelele","mandolina","mandola","arpa llanera","maracas","clave","gurrufio","flauta dulce","oboe de amor","contrafaggote","clarinete picolo"],
    
    ["clarinete bajo","trombon bajo","trombon picolo","tubas wagnerianas","triangulo","bon","clave","laud","lira","saxofon","clavecin","caja"],
    
    ["saxofon baritono","timbales","charango","pandereta","armonica","bongo","bombo","cortina","castanuelas","gong","cabasa","platos"],
    
    ["gaitas","tambor","cambus","guacharaca","platillos","timbales","arpa clasica","matraca","campanas","litofono","guitarron argentino","cacalatchtli"]]

    return fichas


def duracion_juego() -> int:
    
    #PRE: No recibe argumentos, solicita al usuario la duracion de la partida. 
    #POST: Retornara un entero el cual esta asociado a la duracion.

    contador = 0
    while contador < 3:
        print("\n\n\nDURACION DEl JUEGO: \n\n Corto: 4x4\n\n Medio: 8x8\n\n Largo: 12x12")
        duracion_de_juego = input("\n\nDe cuanta duracion deseas que sea tu juego? ej(4x4) ")
        validacion = validacion_duracion_juego(duracion_de_juego.upper())

        if (validacion == 4) or (validacion == 8) or (validacion == 12):
            contador = 4
            
        else:
            contador+=1
            if contador < 3:
                print("INTENTA NUEVAMENTE")
            else:
                print("OK, EMPEZAREMOS LA PARTIDA DE MODALIDAD CORTA, ES DECIR, 4X4")
                contador = 4
                validacion = 4 
    return validacion


def validacion_duracion_juego(duracion:str) -> int:

    #PRE: Esta funcion recibe como argumento un int que representa la duracion de la partida.
    #POST: Retorna un entero representando la duracion de la partida misma y cero si no corresponde.

    if (duracion == "4X4"):
        return 4

    elif (duracion == "8X8"):
        return 8

    elif (duracion == "12X12"):
        return 12

    elif duracion.isnumeric():
        print("INTRODUCISTE SOLO NUMEROS, NO ES VALIDO!!!!!!!")
        return 0
    
    else:
        print("INTRODUCISTE SOLO LETRAS, NO ES VALIDO!!!!!")
        return 0


def armando_tableros(duracion:int) -> list:
    
    #PRE: Esta funcion recibe la duracion de la partida.
    #POST: En base a esa duracion armara los tableros y los retorna como listas de listas para cada user.

    j = 0
    tablero_users = []
    for i in range(duracion):
        tablero_users.append([])
        for k in range(duracion):
            j+=1
            tablero_users[i].append(j)
    alterando_piezas(tablero_users)
    return tablero_users


def alterando_piezas(fichas_reales:list):

    #PRE: Procedimiento que altera la lista recibida.

    shuffle(fichas_reales)
    for i in fichas_reales:
        shuffle(i)
    print("alteramos tableros, muajaja!")


def armando_fichas_reales(duracion:int) -> list:

    #PRE: Esta funcion recibe un entero para poder armar las fichas detras de los tableros.
    #POST: Retorna esas fichas que se esconderan detras de los tableros como una lista.

    fichas_reales = fichas_juegos()
    fichas_reales_users = []
    for i in range(int(duracion/2)):
        for j in range(2):
            fichas_reales_users.append(fichas_reales[i][0:duracion])
    alterando_piezas(fichas_reales_users)
    return fichas_reales_users


def seleccionando_fichas(fichas_rales:list, tablero_user:list, duracion:int) -> bool:

    #PRE: Recibimos los tableros y fichas reales para enviarlos a comparar(listas).
    #POST: Una vez recibidas las coordenadas se envian a comparar y retornara un True o False.

    repetidor = 5
    while repetidor != 4:
        fila_1 = int(input("\n\nPor favor selecciona el numero de la fila a seleccionar.(Ej: 2): "))
        par_1 = int(input("Por favor selecciona la posicion de la ficha en la fila seleccionada.(Ej: 12): "))
        par_1 = par_1 - 1
        fila_1 = fila_1 - 1

        fila_2 = int(input("Por favor ingresa la otra fila a seleccionar: "))
        par_2 = int(input("Por favor ingresa la posicion de la segunda ficha en la segunda fila seleccionada: "))
        par_2 = par_2 - 1
        fila_2 = fila_2 - 1

        #Se resta una unidad a cada valor por como enumeran elementos en las lista.

        validar_coordenadas = validando_coordenadas(fila_1, par_1, fila_2, par_2, duracion)
        if validar_coordenadas == True:
            print("HAZ INTRODUCIDO UNA COORDENADA INCORRECTA")
        else:
            repetidor = 4
            print("\nVALIDAREMOS TUS FICHAS!")
    validacion_fichas = adivinando_fichas(fila_1, fila_2, par_1, par_2, fichas_rales, tablero_user)
    return validacion_fichas


def validando_repeticion(ficha1:str, ficha2:str) -> str:
    
    #PRE: Recibiremos como str los valores de cda ficha que quiere adivinar el user.
    #POST: Retornamos un str en el caso correspondiente.

    if ficha1 == "!" and ficha2 =="!":
        return "repetidas"

    else:
        return "no repetidas"


def validando_coordenadas(fila_1:int, par_1:int, fila_2:int, par_2:int, duracion:int) -> bool:

    #PRE: Recibimos como int los valores de las filas y columnas de las fichas a acertar.
    #POST: Se valida que dichos valores no sean superiores a los elementos de cada lista(tableros y fichas reales).

    if (fila_1 == fila_2) and (par_1 == par_2):
        return True

    elif (fila_1 >= duracion) or (par_1 >= duracion) or (fila_2 >= duracion) or (par_2 >= duracion):
        return True

    else:
        return False


def adivinando_fichas(fila_1:int, fila_2: int, par_1:int, par_2:int, 
                        lista_real:list, tablero:list) -> bool:
    
    #PRE: Recibira las coordenadas de las fichas y vera que coincidan su valores en fichas.
    #POST: Retorna un booleano en los casos de acertar o no y si acierta cambia el numero del tablero por el simbolo"!".

    ficha1 = lista_real[fila_1][par_1]
    ficha2 = lista_real[fila_2][par_2]
    repeticion = validando_repeticion(ficha1, ficha2)

    if repeticion =="repetidas":
        return False
    else:
        print(f"\nficha {tablero[fila_1][par_1]} = {ficha1}\nficha {tablero[fila_2][par_2]} = {ficha2}\n")
        if lista_real[fila_1][par_1] == lista_real[fila_2][par_2]:
            lista_real[fila_1][par_1] = "!"
            lista_real[fila_2][par_2] = "!"
            tablero[fila_1][par_1] = "!"
            tablero[fila_2][par_2] = "!"
            return True
        else:
            return False


def aplicando_layaut_tableros(tableros_propios:list, tipo:str, duracion:int): 
    
    #PRE: Recibimos los tableros como lista a ser afectados por la carta layaut e imprimimos el tipo de tablero.
    
    for i in range(len(tableros_propios[0])-1):
        for j in range(len(tableros_propios)-1):
            tableros_propios[i].append(tableros_propios[j][i])
    for a in range(duracion -1):
        for b in range(duracion -1):
            tableros_propios[b].pop(0) 
    tableros_propios.reverse()
    print(f"APLICADO --- {tipo}")


def aplicando_layaut_fichas_reales(acumuladores_cartas:list, 
                    fichas_propias:list, tableros_propios:list, duracion:int) -> str: 

    #PRE: Recibimos las fichas,tableros y acumuladores a ser afectados por la carta layaut.
    #POST: Retornamos un str si el usuario decide o no aplicar la carta.

    decision = int(input(
        "DESEAS USAR LAS CARTAS LAYAUTS OBTENIDAS?\n1)SI LA QUIERES USAR AHORA\n2)SI DESEAS ACUMULARLA "
    ))

    if decision == 1:
        if acumuladores_cartas.count("layaut") == 0:
            print("NO POSEES ESTE TIPO DE CARTA")
            return "no aplicado"
        else:
            acumuladores_cartas.remove("layaut")
            aplicando_layaut_tableros(fichas_propias, "fichas", duracion)
            aplicando_layaut_tableros(tableros_propios, "tableros", duracion)
            return "aplicado"
    else:
        print("Se acumulo tu carta")
        return "no aplicado"


def aplicando_replay(acumuladores_cartas: list) -> str:

    #PRE: Se reciben los acumuladores de cartas como listas y las acumula o resta.
    #POST: Retornamos un str en caso de aplicar o no la carta.

    decision = int(input(
        "DESEAS USAR LAS CARTAS REPLAIES OBTENIDAS?\n1)SI LA QUIERES USAR AHORA\n2)SI DESEAS ACUMULARLA "
    ))

    if decision == 1:
        if acumuladores_cartas.count("replay") == 0:
            print("NO POSEE ESTE TIPO DE CARTA")
            return "no aplicado"
        else:
            acumuladores_cartas.remove("replay")
            print("\nSE APLICARA TU REPLAY EN CASO DE FALLAR")
            return "aplicar replay"

    else:
        print("se ha acumulado tu carta")
        return "no aplicar replay"


def trasponiendo_fichas(fichas_propias:list, duracion:int, tipo:str):

    #PRE: Procedimiento que recibe listas(tableros), int(duracion) y str(tipo de ficha[tablero u oculta]) y traspone.

    for i in range(len(fichas_propias[0])):
        for j in range(len(fichas_propias)):
            fichas_propias[i].append(fichas_propias[j][i])
    for a in range(duracion):
        for b in range(duracion):
            fichas_propias[a].pop(0)                                        
    print(f"CAMBIO APLICADO AL {tipo}")


def decidiendo_trasponer(acumuladores_cartas:list, fichas_propias:list, 
                            tableros_propios:list, duracion:int) -> str:

    #PRE: Recibimos los tableros a trasponer como listas ademas de otras listas.
    #POST: Retornamos un str informando la aplicacion o no.
    
    decision = int(input(
        "DESEAS USAR LAS CARTAS FATALITIES OBTENIDAS?\n1)SI LA QUIERES USAR AHORA\n2)SI DESEAS ACUMULARLA "))
                                                                                                        
    if decision == 1:
        if acumuladores_cartas.count("fatality") == 0:
            print("NO POSEE ESTE TIPO DE CARTA")
            return "no aplicado"
        
        else:
            acumuladores_cartas.remove("fatality")
            trasponiendo_fichas(tableros_propios, duracion, "tablero")
            trasponiendo_fichas(fichas_propias, duracion, "fichas ocultas")
            return "aplicado"

    else:
        print("CARTA ACUMULADA")
        return "no aplicado"


def espejando_fichas_horizontalmente(fichas_propias:list, tipo:str):

    #PRE: Procedimiento que espeja e imprime el tipo de lista(tablero o ficha)

    for i in fichas_propias:
        i.reverse()
    print(f"CAMBIO APLICADO --- {tipo}")


def decidiendo_espejar_fichas(fichas_propias:list, tableros_propios:list, 
                                     acumuladores_cartas:list, duracion:int) -> str:

    #PRE: Recibimos distintas listas para que seana fectadas y la duracion(int).
    #POST: Retornamos el string correspondiente en caso de que se aplique o no la carta.

    decision = int(input(
        "DESEAS USAR LAS CARTAS TOTIES OBTENIDAS?\n1)SI LA QUIERES USAR AHORA\n2)SI DESEAS ACUMULARLA "
    ))

    if decision == 1:
        forma = int(input("Como deseas espejarla?\n1)Verticalmente\n2)Horizontalmente "))

        if forma == 1:
            if acumuladores_cartas.count("toti") == 0:
                print("NO POSEES CARTA DE ESTE TIPO")
                return "no aplicado"
            else:
                acumuladores_cartas.remove("toti")
                espejar_fichas_verticalmente(tableros_propios,duracion,"tablero")
                espejar_fichas_verticalmente(fichas_propias,duracion, "ficha")
                return "aplicado"

        else:
            if acumuladores_cartas.count("toti") == 0:
                print("NO POSEES CARTA DE ESTE TIPO")
                return "no aplicado"
            else:
                acumuladores_cartas.remove("toti")
                espejando_fichas_horizontalmente(fichas_propias,"fichas")
                espejando_fichas_horizontalmente(tableros_propios,"tablero")
                return "aplicado"

    else:
        print("CARTA ACUMULADA")
        return "no aplicado"


def espejar_fichas_verticalmente(fichas_propias:list, duracion:int, tipo:str):

    #PRE: lista(tableros o fichas), duracion(int) y el tipo(tablero o fichas) para espejar.

    contador = 0
    for i in range(int(duracion / 2)):
        contador = contador -1
        guardando_elemento = fichas_propias[i]
        fichas_propias[i] = fichas_propias[contador]
        fichas_propias.insert(contador, guardando_elemento)
        fichas_propias.pop(contador)
    print(f"CAMBIO APLICADO --- {tipo}")


def validando_decision_cartas(cantidad_replay:int,cantidad_layaut:int, 
                                cantidad_toti:int, cantidad_fatality:int ) -> int:

    #PRE: Recibimos como enteros las cantidades acumuladas de cada carta por usuario
    #POST: Se retorna un int que representa la carta elejida a usar por el usuario.

    decision = int(input(
    f'''\tCARTAS ACUMULADAS:
        0)Si no tienes
        1)Raplay:{cantidad_replay}
        2)Layaut:{cantidad_layaut}
        3)Toti:{cantidad_toti}
        4)Fatality:{cantidad_fatality}
        selecciona cual quieres usar '''))

    contador = 5
    while contador != 6:
        if decision < 0 or decision > 4 :
            decision = int(input(
        f'''\n\tVALOR INVALIDO:
        0)Si no tienes
        1)Raplay:{cantidad_replay}
        2)Layaut:{cantidad_layaut}
        3)Toti:{cantidad_toti}
        4)Fatality:{cantidad_fatality}
        selecciona cual quieres usar '''
        ))

        else:
            contador = 6

    return decision        


def decidiendo_cartas(acumuladores_cartas:list, fichas_propias:list,
                     tableros_propios:list, duracion:int) -> str:

    #PRE: Recibiremos las listas para ser afectadas, acumulador de cartas y la duracion para operar las fichas.
    #POST: Retornamos un str el cual idicara la aplicacion o no de cada carta.

    cantidad_replay = acumuladores_cartas.count("replay")
    cantidad_layaut = acumuladores_cartas.count("layaut")
    cantidad_toti = acumuladores_cartas.count("toti")
    cantidad_fatality = acumuladores_cartas.count("fatality")
    carta_usar = validando_decision_cartas(cantidad_replay, cantidad_layaut, cantidad_toti, cantidad_fatality)
    
    if carta_usar == 0:
        decision = "no aplicado"

    elif carta_usar == 1:
        decision = aplicando_replay(acumuladores_cartas)

    elif carta_usar == 2:
        decision = aplicando_layaut_fichas_reales(acumuladores_cartas, fichas_propias, tableros_propios, duracion)

    elif carta_usar == 3:
        decision = decidiendo_espejar_fichas(fichas_propias, tableros_propios, acumuladores_cartas, duracion)

    else:
        decision =  decidiendo_trasponer(acumuladores_cartas, fichas_propias, tableros_propios, duracion)
    
    return decision


def validando_probabilidad(numero_random:float, acumuladores_cartas:list, fichas_propias:list,
                                tableros_propios:list, duracion:int, prob:list) -> str:

    #PRE: Recibimos una cantidad distinta de datos para ir operando sobre ellos.
    #POST: Retornamos un str en base a las operaciones que realicen las demas funciones.

    if (numero_random > 0) and (numero_random <= prob[0]):
        print("HAS OBTENIDO LA CARTA REPLAY!")
        acumuladores_cartas.append("replay")
    
    elif (numero_random > prob[0]) and (numero_random <= prob[1] + prob[0]):
        print("HAS OBTENIDO LA CARTA LAYAUT!")                  
        acumuladores_cartas.append("layaut")

    elif (numero_random > prob[1] + prob[0]) and (numero_random <= prob[2] + prob[1] + prob[0]):
        print("HAS OBTENIDO LA CARTA TOTI!")
        acumuladores_cartas.append("toti")
    
    elif (numero_random > prob[2] + prob[1] + prob[0]) and (numero_random <= prob[3] + prob[2] + prob[1] + prob[0]):
        print("HAS OBTENIDO LA CARTA FATALITY")
        acumuladores_cartas.append("fatality")

    else:
        print("NO HAS OBTENIDO NINGUNA CARTA, QUE MAL DADO EH!!")

    decision = decidiendo_cartas(acumuladores_cartas, fichas_propias, tableros_propios, duracion)
    return decision


def calculando_probabilidad() -> float:

    #PRE: No recbimos nada
    #POST: Calculamos la probabilidad y retornamos y float.

    carta_probable = uniform(0,100)
    return carta_probable


def jugando_users(fichas_reales_oponente:list, tablero_users_oponente:list,
        fichas_propias:list, tableros_propios:list, duracion:int, participante_adivinador:str, 
        participante_advinado:str, acumuladores_cartas:list, probabilidades:list) -> bool:

    #PRE: recibimos fichas y tableros del oponente(lista), nombres de participantes(str) y duracion del juego(int)
    #POST: Se retorna un booleano en caso de acabar o no el juego.

    validando_fichas = True
    while validando_fichas == True:
        print(f"\t\t\t\n\n turno para: {participante_adivinador} \n tablero de {participante_advinado}\n\n")

        for i in range(len(tablero_users_oponente)):
            for k in range(len(tablero_users_oponente)):
                print(f"\t{tablero_users_oponente[i][k]}", end="")   
            print("\n")
        probabilidad = calculando_probabilidad()
        print(probabilidad)        
        carta_comodin = validando_probabilidad(probabilidad, acumuladores_cartas, fichas_propias, tableros_propios, duracion,
                                                probabilidades)
        validando_fichas = seleccionando_fichas(fichas_reales_oponente, tablero_users_oponente, duracion)
        if validando_fichas == True:
            finalizacion = validando_finalizacion_juego(duracion, fichas_reales_oponente)
            if finalizacion == True:
                validando_fichas = False
                finalizacion = True
            else:
                print("VAMOS NUEVAMENTE, ACERTASTE")
        else:
            if carta_comodin == "aplicar replay":
                validando_fichas = True
                print(f"HAS FALLADO PERO VAMOS DE NUEVO {participante_adivinador}")
                
            elif carta_comodin == "no aplicar replay":
                print("HAS FALLADO Y DECIDISTE NO USAR LA CARTA REPLAY")
                finalizacion = False

            else:
                print(f"HA FALLADO {participante_adivinador} A CONTINUACION {participante_advinado}")
                finalizacion = False

    return finalizacion


def validando_finalizacion_juego(duracion_juego:int, fichas_reales_users:list) -> bool:

    #PRE:Esta funcion recibira la duracion y fichas reales.
    #POST: Retorna un booleano si todos los elementos coinciden con "!" y en ese caso termina el juego.

    if fichas_reales_users == [["!"]*duracion_juego]*duracion_juego:
        return True

    else:
        return False


def validando_existencia_ganador(lista_ganadores:list, participantes:str) -> int:

    #PRE: Recibimos una lista y nombres de los participantes ganadores.
    #POST: En caso de de existir o no retorna un entero.
    
    if participantes in lista_ganadores:
        cantidad_existencia = lista_ganadores.count(participantes)
        return cantidad_existencia
    else:
        return 0


def decidiendo_juagar() ->str:

    #PRE: No recibimos ningun argumento, solicitamos si se quiere jugar una partida.
    #POST: Retornamos el valor str introduciodo por el user, si o no.

    validador = 4
    while validador != 2:
        decision = input("Desean jugar? (si o no) ").lower()
        if decision == "no":
            validador = 2
            
        elif decision =="si":
            validador = 2

        else:
            print("HAS INTRODUCIDO UN VALOR NO VALIDO")

    return decision


def agregando_ganadores(ganadores_totales:list, ganadores_repetidos:list, participante:str, partidas_totales:int) -> str:

    #PRE:Recibimos las listas de ganadores, sus nombres y la cantidad de partidas como un int.
    #POS: retornamos el participante ganador como str.

    existecia_ganador = validando_existencia_ganador(ganadores_repetidos, participante)
    if existecia_ganador == 0:
        ganadores_totales.append([participante, existecia_ganador+1, partidas_totales])
        ganadores_repetidos.append(participante)

    else:
        ganadores_repetidos.append(participante)
        ganadores_totales.append([participante,existecia_ganador + 1, partidas_totales])

    return participante


def intercambio_turnos(cartas_acumuladas1:list, cartas_acumuladas2:list, ganadores_totales:list, ganadores_repetidos:list, 
                        participante1:str, participante2:str,nivel_duracion:int, tablero_1:list, tablero_2:list, 
                                fichas_1:list, fichas_2:list, partidas_totales:int,probabilidades:list) -> str:

    jugando_user1 = True
    while jugando_user1 == True:
        jugando_user1 = jugando_users(fichas_2, tablero_2, fichas_1,tablero_1,
                            nivel_duracion, participante1, participante2, cartas_acumuladas1, probabilidades)

        if jugando_user1 == False:
            jugando_user2 = jugando_users(fichas_1, tablero_1, fichas_2,tablero_2,
                            nivel_duracion, participante2, participante1, cartas_acumuladas2,probabilidades)
            
            if jugando_user2 == False:
                jugando_user1 = True
            else:
                ganador = agregando_ganadores(ganadores_totales,ganadores_repetidos, participante2, partidas_totales)
        else:
            jugando_user1 = False
            ganador = agregando_ganadores(ganadores_totales,ganadores_repetidos, participante1, partidas_totales)

    return ganador


def mostrando_score(ganadores_totales:list, ganadores_repetidos:list, contador_partidas:int):

    #PRE: Procedimiento, recibe las listas de los ganadores y los id's de partidas.

    print(
            f"\t\t\t\t\t\tBIENVENIDOS A NUESTRO MENU \n\nLos ganadores de las ultimas {contador_partidas} partidas son:"
        )

    if (len(ganadores_totales) == 4) and (len(ganadores_repetidos) == 4):
        contador_partidas = 4
        for i, j,k in ganadores_totales:
            print(f"participantes:{i} cantidad de partidas ganadas:{j} id de partida ganda: {k}")
        ganadores_totales.pop(0)
        ganadores_repetidos.pop(0)
    else:
        for i, j, k in ganadores_totales:
            print(f"participantes: {i}  partidas ganadas:  {j} id de partida ganda: {k}")


def cambiar_probabilidad() ->list:

    #PRE: No recibimos ningun valor.
    #POS: Se solicitan las probabilidades de las cartas a los usuarios y se retorna una lista con ellas.

    print(
     """\nTIENES 5 CARTAS:
        1)Replay:Puedes repetir un turno
        2)Layaut:Alteras tu tablero aleatoriamente
        3)Toti: Espejas tu tablero
        4)Fatality: Traspones tu tablero
        5)Carta nula: No obtienes ninguna carta(coloca todo en cero o solo pon 100 a esta carta""")

    cambio = input(
        "\nTODAS LAS CARTAS TIENEN UNA PROBABIlIDAD DEL 20%, DESEAN CAMBIARLA? LA SUMATORIA DEBE DAR 100%. responde con si o no ")
    
    probabilidades = []
    cartas = ["replay","layaut","toti","fatality","nula"]
    if cambio == "si":
        for i in cartas:
            porcentaje = int(input(f"De cuanto deseas la carta {i} "))
            probabilidades.append(porcentaje)
    else:
        probabilidades = [20,20,20,20,20]
    
    return probabilidades


def main():

    contador_partidas_totales = 0
    contador_partidas = 0
    lista_ganadores_repetidos = []
    lista_ganadores_totales = []

    decision = "si"
    while decision =="si":
        mostrando_score(lista_ganadores_totales, lista_ganadores_repetidos, 
                            contador_partidas_totales)
        cartas_acumuladas1 = []
        cartas_acumuladas2 = []
            
        decision = decidiendo_juagar()
        if decision =="no":
            print("OK, CHAOOO")
        else:
            if contador_partidas == 4:
                contador_partidas = 4
            else:
                contador_partidas+=1

            lista_probabilidades = cambiar_probabilidad()
            contador_partidas_totales+=1
            participante1 = input("Ingresa el nombre participante 1 ")
            participante2 = input("Ingresa el nombre participante 2 ")
            nivel_duracion = duracion_juego()
            tablero_1 = armando_tableros(nivel_duracion)
            tablero_2 = armando_tableros(nivel_duracion)
            fichas_1 = armando_fichas_reales(nivel_duracion)
            fichas_2 = armando_fichas_reales(nivel_duracion)
            ganador = intercambio_turnos(cartas_acumuladas1, cartas_acumuladas2, lista_ganadores_totales, lista_ganadores_repetidos, 
                                        participante1, participante2,nivel_duracion, tablero_1, tablero_2, fichas_1, fichas_2, 
                                        contador_partidas_totales, lista_probabilidades)

            print(f"EL GANADOR ES {ganador}")


main()
