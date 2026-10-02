import os
#region Inicio, ingreso y validación de usuario
print()
print("Bienvenido")
 #iniciamos la variable de "bandera"
ingreso = "incorrecto"
 #Validamos "usuario"
while ingreso == "incorrecto":
    usuario = input("Ingrese usuario, sólo letras: ")
    if usuario.isalpha():
        ingreso = "correcto"
    else:
        print("Usuario incorrecto")
#endregion

#region Inicio de las variables de los turnos
turnoslibres =""
turno = ""
#Turnos de los Lunes(son 4)
L1 = ""
L2 = ""
L3 = ""
L4 = ""
#Turnos de los Martes(son 3)
M1 = ""
M2 = ""
M3 = ""
opcion = 0
#endregion

#region opciones
while opcion != 5:
    os.system('clear')
    print()
    print(f"Usuario: {usuario}")
    print()
    print ("1): Reservar turno")
    print ("2): Cancelar turno")
    print ("3): Ver agenda del día")
    print ("4): Ver resumen general")
    print ("5): Salir")
    print()
    opcion = input("Ingrese su opción (1 al 5): ")
  #region validacion ingreso opcion 
    if opcion.isdigit():
        opcion=int(opcion)
        if opcion in range(1,6):
          #region OPCIÓN 1            
            if opcion == 1:             
              #region inicializa variables del bucle
                dia = ""            # Inicializamos variable dia para reserva de turno
                continuar ="si"     # Bandera para continuar o cortar el bucle
              #endregion             
              #region menu para elegir día de reserva (o salir)
                os.system('clear')
                print()                
                while continuar == "si": 
                    os.system('clear')
                    print()
                    print(f"Usuario: {usuario}")
                    print()
                    print("Turno día Lunes, presione l: ")
                    print("Turno día Martes, presione m: ")
                    print("Para salir presione s: ")
                    print()
                    dia = input ("Ingrese su opción: ").lower()
                    #
                    # valida que el ingreso sea texto, y que sea "l", "m" o "s"
                    while not dia.isalpha() or (dia != "l" and dia != "m" and dia != "s"):                       
                        dia = input("Error. Ingrese sólo l, m o s; ")
                    #
              #endregion              
                  #region Proceso día Lunes
                    os.system('clear')
                    print()
                    if dia == "l":
                     #region Turno 1:
                       #region Verifica si el turno 1 del Lunes está libre
                        if L1 == "":
                            print ("Está libre el turno 1 del Lunes")
                            turnoslibres = "1"
                            L1 = input("Ingrese el nombre: ")
                            ok = "si" #Bandera para confirmar el turno                   
                          #region Comprueba que el turno no esté repetido
                            if L1 == L2:
                                print("Ya reservó el turno 2")
                                L1 = ""
                                ok ="no"
                            elif L1 == L3:
                                print("Ya reservó el turno 3")
                                L1 = ""
                                ok ="no"
                            elif L1 == L4:
                                print("Ya reservó el turno 4")
                                L1 = ""
                                ok ="no"
                            elif L1 == M1 or L1 == M2 or L1 == M3:
                                print("Ya tiene reservado un turno el día Martes")
                                L1 = ""
                                ok ="no"                                                                
                            if ok == "si":#Si todo está bien, confirma el turno
                                print(f"Queda reservado el turno 1 del Lunes para {L1}")
                          #endregion
                          #region Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                          #endregion
                       #endregion 
                     #endregion              
                     #region Turno 2:
                       #region Verifica si el turno 2 del Lunes está libre
                        elif L2 == "":
                            print ("Está libre el turno 2 del Lunes")
                            turnoslibres = turnoslibres + "2"
                            L2 = input("Ingrese el nombre: ")
                       #endregion    
                          #region Comprueba que el turno no esté repetido
                            if L2 == L1:
                                print("Ya reservó el turno 1")
                                L2 = ""
                            elif L2 == L3:
                                print("Ya reservó el turno 3")
                                L2 = ""
                            elif L2 == L4:
                                print("Ya reservó el turno 4")
                                L2 = ""
                            elif L2 == M1 or L2 == M2 or L2 == M3:
                                print("Ya tiene reservado un turno el día Martes")
                                L2 = ""
                                
                            #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 2 del Lunes para {L2}")
                          # endregion                            
                          # region Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                          # endregion
                     #endregion               
                     #region Turno 3:
                       #region Verifica si el turno 3 del Lunes está libre
                        elif L3 == "":
                            print ("Está libre el turno 3 del Lunes")
                            turnoslibres = turnoslibres + "3"
                            L3 = input("Ingrese el nombre: ")
                       #endregion
                          #region Comprueba que el turno no esté repetido
                            if L3 == L1:
                                print("Ya reservó el turno 1")
                                L3 = ""
                            elif L3 == L2:
                                print("Ya reservó el turno 2")
                                L3 = ""
                            elif L3 == L4:
                                print("Ya reservó el turno 4")
                                L3 = ""
                            elif L3 == M1 or L3 == M2 or L3 == M3:
                                print("Ya tiene reservado un turno el día Martes")
                                L3 = ""
                                    
                            #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 3 del Lunes para {L3}")
                          #endregion                            
                          #region Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                          #endregion
                     #endregion           
                     #region Turno 4:
                       #region Verifica si el turno 4 del Lunes está libre
                        elif L4 == "":
                            print ("Está libre el turno 4 del Lunes")
                            turnoslibres = turnoslibres + "4"
                            L4 = input("Ingrese el nombre: ")
                       #endregion                                                 
                          #Comprueba que el turno no esté repetido
                            if L4 == L1:
                                print("Ya reservó el turno 1")
                                L4 = ""
                            elif L4 == L2:
                                print("Ya reservó el turno 2")
                                L4 = ""
                            elif L4 == L3:
                                print("Ya reservó el turno 3")
                                L4 = ""
                            elif L4 == M1 or L4 == M2 or L4 == M3:
                                print("Ya tiene reservado un turno el día Martes")
                                L4 = ""                                            
                            #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 4 del Lunes para {L4}")
                          #endregion                                                     
                          #region Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                          #endregion                     
                     #endregion
                       #region Si no quedan turnos disponibles, se informa
                        else :
                            print("No quedan turnos disponibles el día Lunes")
                            #Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                       #endregion 
                  #endregion
                  #region Inicio proceso día Martes
                    elif dia == "m":
                        os.system('clear')
                        print()

                        #Verifica si el turno 1 del Martes está libre
                        if M1 == "":
                            print ("Está libre el turno 1 del Martes")
                            turnoslibres = "1"
                            M1 = input("Ingrese el nombre: ")

                            #Comprueba que el turno no esté repetido
                            if M1 == M2:
                                print("Ya reservó el turno 2")
                                M1 = ""
                            elif M1 == M3:
                                print("Ya reservó el turno 3")
                                M1 = ""
                            elif M1 == L1 or M1 == L2 or M1 == L3 or M1 == L4:
                                print("Ya tiene reservado un turno el día Lunes")
                                M1 = ""
                            
                            #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 1 del Martes para {M1}")
                            #Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"

                        #Verifica si el turno 2 del Martes está libre        
                        elif M2 == "":
                            print ("Está libre el turno 2 del Martes")
                            turnoslibres = turnoslibres + "2"
                            M2 = input("Ingrese el nombre: ")
                                
                            #Comprueba que el turno no esté repetido
                            if M2 == M1:
                                print("Ya reservó el turno 1")
                                M2 = ""
                            elif M2 == M3:
                                print("Ya reservó el turno 3")
                                M2 = ""
                            elif M2 == L1 or M2 == L2 or M2 == L3 or M2 == L4:
                                print("Ya tiene reservado un turno el día Lunes")
                                M2 = ""
                                
                                #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 2 del Martes para {M2}")
                            #Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"

                        #Verifica si el turno 3 del Martes está libre
                        elif M3 == "":
                            print ("Está libre el turno 3 del Martes")
                            turnoslibres = turnoslibres + " 3"
                            M3 = input("Ingrese el nombre: ")

                            #Comprueba que el turno no esté repetido
                            if M3 == M1:
                                print("Ya reservó el turno 1")
                                M3 = ""
                            elif M3 == M2:
                                print("Ya reservó el turno 2")
                                M3 = ""
                            elif M3 == L1 or M3 == L2 or M3 == L3 or M3 == L4:
                                print("Ya tiene reservado un turno el día Lunes")
                                M3 = ""
                                    
                            #Si todo está bien, asigna el turno
                            else:
                                print(f"Queda reservado el turno 3 del Martes para {M3}")
                            
                            #Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                        
                        #Si no quedan turnos disponibles, se informa
                        else: 
                            turnoslibres == ""
                            print("No quedan turnos disponibles el día Martes")
                            #Ofrece opción de continuar la carga de turnos
                            continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()
                            while continuar != "n" and continuar != "s": #Valida el ingreso
                                print("Ingrese sólo s/n ")
                                continuar = input ("¿Desea continuar la carga de turnos? (s/n)?: ").lower()

                            #continua la carga de turnos (continuar =si) o sale (continuar =no)    
                            if continuar == "s":
                                continuar = "si"
                            else:                                       
                                continuar = "no"
                  #endregion
                    else:
                        continuar = "no"
          #endregion
          #region OPCIÓN 2
            elif opcion == 2:                
                anuladia = ""
                turnoanular= ""          
                while anuladia != "s":
                    os.system('clear')
                    print()
                    print(f"Usuario: {usuario}")
                    print()
                    print("Anular turno del Lunes, ingrese l")
                    print("Anular turno del Martes, ingrese m")
                    print("Salir, ingrese s")
                    print()

                    correcto = "no"
                    while correcto =="no":
                        anuladia = input("Ingrese la opción deseada: ").lower()
                        if not anuladia.isalpha():
                            print("Ingreso incorrecto, sólo l, m o s")
                            input("Presione ENTER para continuar")
                            #Si no ingresa "l" o "m" o "s"
                        elif anuladia != "l" and anuladia != "m" and anuladia != "s":
                            print("Ingreso incorrecto, sólo l, m o s")
                            input("Presione ENTER para continuar")
                        else:
                            correcto = "si"
                    
                    #inicia proceso para nular un turno el Lunes
                    if anuladia == "l":
                        os.system('clear')
                        print()
                        
                        turnoanular = input("Ingrese el nombre: ") #solicita el nombre -turno- a anular
                        if turnoanular.isalpha(): #valida el ingreso
                            
                            #Busca el turno 
                            if turnoanular == L1:
                                L1 = ""
                                print ("Turno 1 del Lunes anulado")
                            elif turnoanular == L2:
                                L2 = ""
                                print ("Turno 2 del Lunes anulado")
                            elif turnoanular == L3:
                                L3 = ""
                                print ("Turno 3 del Lunes anulado")
                            elif turnoanular == L4:
                                L4 = ""
                                print ("Turno 4 del Lunes anulado")                                
                            #si no se encuentra el nombre (o turno)
                            else:
                                print ("No se encontró el turno")

                        #si no ingreso un nombre "solo texto"                    
                        else:
                            print("Ingreso incorrecto")
                        input("Presione ENTER para continuar")
                        
                    #Inicia proceso para anular un turno el Martes
                    elif anuladia == "m":
                        os.system('clear')
                        print()
                        turnoanular = input("Ingrese el nombre: ")

                        if turnoanular.isalpha():#valida el ingreso

                            #Busca el turno
                            if turnoanular == M1:
                                M1 = ""
                                print ("Turno 1 del Martes anulado")
                            elif turnoanular == M2:
                                M2 = ""
                                print ("Turno 2 del Martes anulado")
                            elif turnoanular == M3:
                                M3 = ""
                                print ("Turno 3 del Martes anulado")
                            
                            #si no encuentra el turno
                            else:
                                print ("Turno no encontrado")
                            
                        #si no ingreso un nombre "solo texto"                    
                        else:
                            print("Ingreso incorrecto")
                        input("Presione ENTER para continuar")                       
          #endregion
          #region OPCIÓN 3
            elif opcion == 3:
                os.system('clear') #limpia pantalla
                print()
                ver_agenda = "s"

                #solicita dia a ver de la agenda
                while ver_agenda == "s":
                    os.system('clear')
                    agendadia = "" #inicializa variable
                    while agendadia != "l" and agendadia != "m":
                        print (f"Usuario {usuario}")
                        print()
                        agendadia = input ("Ingrese el día que desea ver (L/M): ").lower()
                
                    #Procesa el Lunes
                    if agendadia == "l":
                        
                        print()
                        print (f"Turno 1 día Lunes: {L1}")
                        print (f"Turno 2 día Lunes: {L2}")
                        print (f"Turno 3 día Lunes: {L3}")
                        print (f"Turno 4 día Lunes: {L4}")
                        print()
                        ver_agenda = input("¿Desea ver otra agenda? s/n: ")
                        while ver_agenda != "s" and ver_agenda != "n":
                            ver_agenda = input("Error, ingrese sólo s ó n: ")

                    #Procesa el Martes
                    elif agendadia == "m":
                        #os.system('clear')
                        print()
                        print (f"Turno 1 día Martes: {M1}")
                        print (f"Turno 2 día Martes: {M2}")
                        print (f"Turno 3 día Martes: {M3}")
                        print()
                        ver_agenda = input("¿Desea ver otra agenda? s/n: ")
                        while ver_agenda != "s" and ver_agenda != "n":
                            ver_agenda = input("Error, ingrese sólo s ó n: ")
          #endregion
          #region OPCIÓN 4
            elif opcion == 4:

                os.system('clear')
                print()

                #Inicia las variables para dia Lunes
                ocupadosL = 0
                libresL = 0                
                
                #Inicia el conteo de los turnos del Lunes
                #coloco todo en la misma línea para priorizar limpieza visual del código
                if L1 == "": libresL += 1 
                else: ocupadosL += 1

                if L2 == "": libresL += 1
                else: ocupadosL += 1

                if L3 == "": libresL += 1
                else: ocupadosL += 1

                if L4 == "": libresL += 1
                else: ocupadosL += 1
                
                #Inicia las variables para dia Martes
                ocupadosM = 0
                libresM = 0
                
                #Inicia el conteo de los turnos del Martes
                if M1 == "": 
                    libresM += 1                    
                else:
                    ocupadosM += 1

                if M2 == "": 
                    libresM += 1
                else:
                    ocupadosM += 1

                if M3 == "": 
                    libresM += 1
                else: 
                    ocupadosM += 1
                print(f"Usuario: {usuario}")

                #Imprime resultados de Lunes                
                if libresL == 0: print("No quedan turnos libres el Lunes")
                else: print(f"Quedan {libresL} turnos libres el Lunes ")

                if ocupadosL == 0: print("Todos los turnos del Lunes están libres")
                else: print(f"Hay {ocupadosL} turnos ocupados el Lunes ")
                print()

                #Imprime resultados de Martes
                if libresM == 0: print("No quedan turnos libres el Martes")
                else: print(f"Quedan {libresM} turnos libres el Martes ")

                if ocupadosM == 0: print("Todos los turnos del Martes están libres")
                else: print(f"Hay {ocupadosM} turnos ocupados el Martes ")
                print()

                #Imprime comparativas
                if ocupadosL > ocupadosM: print(f"Mayor cantidad de turnos ocupados: Lunes ({ocupadosL})")

                elif ocupadosL < ocupadosM: print(f"Mayor cantidad de turnos ocupados: Martes ({ocupadosM})")
                              
                else :
                    if (ocupadosL != "" and ocupadosM != ""):
                        print(f"Igual cantidad de turnos ocupados: Lunes ({ocupadosL}) y Martes ({ocupadosM})")

                input("Presione ENTER para volver al menú principal...")
          #endregion
          #region OPCIÓN 5
            else: #Opción 5) salida del programa
                os.system('clear')
                print()
                print ("Salió correctamente del programa")
                print()
          #endregion
  #endregion        
#endregion