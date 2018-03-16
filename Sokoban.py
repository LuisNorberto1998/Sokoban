# -*- coding: cp1252 -*-
print " 0 -> Muneco   1 -> Caja          2 -> Meta   3 -> Pared \n 4 -> Camino   5 -> Caja en meta  6 -> Muñeco en meta \n " #Simbologia
print " a = Izquierda d = Derecha \n w = Arriba    s = Abajo \n"

Matriz = [[3,3,3,3,3,3,3,3,3],
          [3,4,2,1,4,4,4,4,3],
          [3,4,0,4,4,4,4,4,3],
          [3,1,4,4,1,4,4,2,3],
          [3,2,4,4,4,4,4,4,3],
          [3,4,4,4,2,1,4,4,3],
          [3,3,3,3,3,3,3,3,3]]

posicionx = 2
posiciony = 2


while True: #Inicia el ciclo
    for matrizx in Matriz:
        for matrizy in matrizx:
            print matrizy,
        print
        
    Mov = raw_input("¿Hacia donde te quieres mover? \n ") #Pregunta hacia donde se desea mover el usuario
    #MOVIMIENTO A LA DERECHA
    if Mov == "d":
        #Movimiento a la derecha si hay camino "044"
        if Matriz[posicionx][posiciony + 1] == 4 and Matriz[posicionx][posiciony] == 0: 
            Matriz[posicionx][posiciony] = 4
            posiciony+= 1
            Matriz[posicionx][posiciony] = 0
        
        elif Matriz[posicionx][posiciony + 1] == 1 and Matriz[posicionx][posiciony] == 0:
            #Movimiento a la derecha si hay caja y camino "014"
            if Matriz[posicionx][posiciony + 2] == 4:
                Matriz[posicionx][posiciony] = 4
                posiciony+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony + 1] = 1
            #Movimiento a la derecha si hay caja y meta "012"
            elif Matriz[posicionx][posiciony + 2] == 2:
                Matriz[posicionx][posiciony] = 4
                posiciony+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony + 1] = 5
                
        #Si la posicion es igual a 6 y adelante hay una caja en meta
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony + 1] == 5:
            #muñeco en meta, caja en meta y meta "652"
            if Matriz[posicionx][posiciony + 2] == 2:
                Matriz[posicionx][posiciony] = 2
                posiciony+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony + 1] = 5
            #muñeco en meta, caja en meta y camino "654"
            elif Matriz[posicionx][posiciony + 2] == 4:
                Matriz[posicionx][posiciony] = 2
                posiciony+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony + 1] = 1
            
        #Movimiento a la derecha si hay caja en meta y camino
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx][posiciony + 1] == 5: 
            #054
            if Matriz[posicionx][posiciony + 2] == 4:
                Matriz[posicionx][posiciony] = 4
                posiciony+= 1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony + 1] = 1
            #052
            elif Matriz[posicionx][posiciony + 2] == 2:
                Matriz[posicionx][posiciony] = 4
                posiciony+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony + 1] = 5
                
        #Metas y muñeco consecutivo "622"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony + 1] == 2:
            Matriz[posicionx][posiciony] = 2
            posiciony+= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento a la derecha si el muñeco esta sobre la meta "024"
        elif Matriz[posicionx][posiciony + 1] == 2 and Matriz[posicionx][posiciony + 2] == 4 : 
            Matriz[posicionx][posiciony] = 4
            posiciony+= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento a la derecha si hay muñeco en meta y adelante un camino "644"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony + 1] == 4:
            Matriz[posicionx][posiciony] = 2
            posiciony+= 1
            Matriz[posicionx][posiciony] = 0
            
        #Muñeco en camino y si adelante hay meyta "402"
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx][posiciony + 1] == 2: 
            Matriz[posicionx][posiciony] = 4
            posiciony+=1
            Matriz[posicionx][posiciony] = 6
            
        #Muñeco en meta, adelante hay caja y adelante de la caja hay una meta o camino
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony + 1] == 1:
            if Matriz[posicionx][posiciony + 2] == 2: #612
                Matriz[posicionx][posiciony] = 2
                posiciony+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony + 1] = 5
            elif Matriz[posicionx][posiciony + 2] == 4:#614
                Matriz[posicionx][posiciony] = 2
                posiciony+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony + 1] = 1

    #MOVIMIENTO A LA IZQUIERDA
    elif Mov == "a":
        #Movimiento a la izquierda si hay camino "044"
        if Matriz[posicionx][posiciony - 1] == 4 and Matriz[posicionx][posiciony] == 0: 
            Matriz[posicionx][posiciony] = 4
            posiciony-= 1
            Matriz[posicionx][posiciony] = 0
        
        elif Matriz[posicionx][posiciony - 1] == 1 and Matriz[posicionx][posiciony] == 0:
            #Movimiento a la izquierda si hay caja y camino "014"
            if Matriz[posicionx][posiciony - 2] == 4:
                Matriz[posicionx][posiciony] = 4
                posiciony-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony - 1] = 1
            #Movimiento a la izquierda si hay caja y meta "012"
            elif Matriz[posicionx][posiciony - 2] == 2:
                Matriz[posicionx][posiciony] = 4
                posiciony-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony - 1] = 5
                
        #Si la posicion es igual a 6 y adelante hay una caja en meta
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony - 1] == 5:
            #muñeco en meta, caja en meta y meta "652"
            if Matriz[posicionx][posiciony - 2] == 2:
                Matriz[posicionx][posiciony] = 2
                posiciony-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony - 1] = 5
            #muñeco en meta, caja en meta y camino "654"
            elif Matriz[posicionx][posiciony - 2] == 4:
                Matriz[posicionx][posiciony] = 2
                posiciony-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony - 1] = 1
            
        #Movimiento a la derecha si hay caja en meta y camino
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx][posiciony - 1] == 5: 
            #054
            if Matriz[posicionx][posiciony - 2] == 4:
                Matriz[posicionx][posiciony] = 4
                posiciony-= 1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony - 1] = 1
            #052
            elif Matriz[posicionx][posiciony - 2] == 2:
                Matriz[posicionx][posiciony] = 4
                posiciony-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx][posiciony - 1] = 5
                
        #Metas y muñeco consecutivo "622"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony - 1] == 2:
            Matriz[posicionx][posiciony] = 2
            posiciony-= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento a la derecha si el muñeco esta sobre la meta "024"
        elif Matriz[posicionx][posiciony - 1] == 2 and Matriz[posicionx][posiciony - 2] == 4 : 
            Matriz[posicionx][posiciony] = 4
            posiciony-= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento a la derecha si hay muñeco en meta y adelante un camino "644"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony - 1] == 4:
            Matriz[posicionx][posiciony] = 2
            posiciony-= 1
            Matriz[posicionx][posiciony] = 0
            
        #Muñeco en camino y si adelante hay meyta "402"
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx][posiciony - 1] == 2: 
            Matriz[posicionx][posiciony] = 4
            posiciony-=1
            Matriz[posicionx][posiciony] = 6
            
        #Muñeco en meta, adelante hay caja y adelante de la caja hay una meta o camino
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx][posiciony - 1] == 1:
            if Matriz[posicionx][posiciony - 2] == 2: #612
                Matriz[posicionx][posiciony] = 2
                posiciony-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony - 1] = 5
            elif Matriz[posicionx][posiciony - 2] == 4:#614
                Matriz[posicionx][posiciony] = 2
                posiciony-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony - 1] = 1
                
    #MOVIMIENTO HACIA ARRIBA
    elif Mov == "w":
        #Movimiento hacia arriba si hay camino "044"
        if Matriz[posicionx - 1][posiciony] == 4 and Matriz[posicionx][posiciony] == 0: 
            Matriz[posicionx][posiciony] = 4
            posicionx-= 1
            Matriz[posicionx][posiciony] = 0
        
        elif Matriz[posicionx - 1][posiciony] == 1 and Matriz[posicionx][posiciony] == 0:
            #Movimiento arriba si hay caja y camino "014"
            if Matriz[posicionx - 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 4
                posicionx-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony - 1] = 1
            #Movimiento hacia arriba si hay caja y meta "012"
            elif Matriz[posicionx - 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 4
                posicionx-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx - 1][posiciony] = 5
                
        #Si la posicion es igual a 6 y adelante hay una caja en meta
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx - 1][posiciony] == 5:
            #muñeco en meta, caja en meta y meta "652"
            if Matriz[posicionx - 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 2
                posicionx-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx - 1][posiciony] = 5
            #muñeco en meta, caja en meta y camino "654"
            elif Matriz[posicionx - 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 2
                posicionx-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx - 1][posiciony] = 1
            
        #Movimiento hacia arriba si hay caja en meta y camino
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx - 1][posiciony] == 5: 
            #054
            if Matriz[posicionx - 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 4
                posicionx-= 1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx - 1][posiciony] = 1
            #052
            elif Matriz[posicionx - 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 4
                posicionx-=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx - 1][posiciony] = 5
                
        #Metas y muñeco consecutivo "622"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx - 1][posiciony] == 2:
            Matriz[posicionx][posiciony] = 2
            posicionx-= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento hacia arriba si el muñeco esta sobre la meta "024"
        elif Matriz[posicionx - 1][posiciony] == 2 and Matriz[posicionx - 2][posiciony] == 4 : 
            Matriz[posicionx][posiciony] = 4
            posicionx-= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento hacia arriba si hay muñeco en meta y adelante un camino "644"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx - 1][posiciony] == 4:
            Matriz[posicionx][posiciony] = 2
            posicionx-= 1
            Matriz[posicionx][posiciony] = 0
            
        #Muñeco en camino y si adelante hay meta "402"
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx - 1][posiciony] == 2: 
            Matriz[posicionx][posiciony] = 4
            posicionx-=1
            Matriz[posicionx][posiciony] = 6
            
        #Muñeco en meta, adelante hay caja y adelante de la caja hay una meta o camino
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx - 1][posiciony] == 1:
            if Matriz[posicionx - 2][posiciony] == 2: #612
                Matriz[posicionx][posiciony] = 2
                posicionx-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx - 1][posiciony] = 5
            elif Matriz[posicionx - 2][posiciony] == 4:#614
                Matriz[posicionx][posiciony] = 2
                posicionx-= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx - 1][posiciony] = 1

    #MOVIMIENTO HACIA ABAJO
    elif Mov == "s":
        #Movimiento abajo si hay camino "044"
        if Matriz[posicionx + 1][posiciony] == 4 and Matriz[posicionx][posiciony] == 0: 
            Matriz[posicionx][posiciony] = 4
            posicionx+= 1
            Matriz[posicionx][posiciony] = 0
        
        elif Matriz[posicionx + 1][posiciony] == 1 and Matriz[posicionx][posiciony] == 0:
            #Movimiento hacia abajo si hay caja y camino "014"
            if Matriz[posicionx + 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 4
                posicionx+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx][posiciony + 1] = 1
            #Movimiento hacia abajo si hay caja y meta "012"
            elif Matriz[posicionx + 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 4
                posicionx+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx + 1][posiciony] = 5
                
        #Si la posicion es igual a 6 y adelante hay una caja en meta
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx + 1][posiciony] == 5:
            #muñeco en meta, caja en meta y meta "652"
            if Matriz[posicionx + 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 2
                posicionx+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx + 1][posiciony] = 5
            #muñeco en meta, caja en meta y camino "654"
            elif Matriz[posicionx + 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 2
                posicionx+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx + 1][posiciony] = 1
            
        #Movimiento hacia abajo si hay caja en meta y camino
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx + 1][posiciony] == 5: 
            #054
            if Matriz[posicionx + 2][posiciony] == 4:
                Matriz[posicionx][posiciony] = 4
                posicionx+= 1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx + 1][posiciony] = 1
            #052
            elif Matriz[posicionx + 2][posiciony] == 2:
                Matriz[posicionx][posiciony] = 4
                posicionx+=1
                Matriz[posicionx][posiciony] = 6
                Matriz[posicionx + 1][posiciony] = 5
                
        #Metas y muñeco consecutivo "622"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx + 1][posiciony] == 2:
            Matriz[posicionx][posiciony] = 2
            posicionx+= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento hacia abajo si el muñeco esta sobre la meta "024"
        elif Matriz[posicionx + 1][posiciony] == 2 and Matriz[posicionx + 2][posiciony] == 4 : 
            Matriz[posicionx][posiciony] = 4
            posicionx+= 1
            Matriz[posicionx][posiciony] = 6
            
        #Movimiento hacia abajo si hay muñeco en meta y adelante un camino "644"
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx + 1][posiciony] == 4:
            Matriz[posicionx][posiciony] = 2
            posicionx+= 1
            Matriz[posicionx][posiciony] = 0
            
        #Muñeco en camino y si adelante hay meyta "402"
        elif Matriz[posicionx][posiciony] == 0 and Matriz[posicionx + 1][posiciony] == 2: 
            Matriz[posicionx][posiciony] = 4
            posicionx+=1
            Matriz[posicionx][posiciony] = 6
            
        #Muñeco en meta, adelante hay caja y adelante de la caja hay una meta o camino
        elif Matriz[posicionx][posiciony] == 6 and Matriz[posicionx + 1][posiciony] == 1:
            if Matriz[posicionx + 2][posiciony] == 2: #612
                Matriz[posicionx][posiciony] = 2
                posicionx+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx + 1][posiciony] = 5
            elif Matriz[posicionx + 2][posiciony] == 4:#614
                Matriz[posicionx][posiciony] = 2
                posicionx+= 1
                Matriz[posicionx][posiciony] = 0
                Matriz[posicionx + 1][posiciony] = 1
    else:
        print "Movimiento erroneo, por favor eliga una funcion correcta"
                
    cadena =((posicionx,posiciony)for posiciony,  row in enumerate(Matriz)for posicionx,  elemento in enumerate(row) if elemento == 0)
    for e in cadena:
        print "Posicion = ", e
        
    ele =((cajax,cajay)for cajay,  row in enumerate(Matriz) for cajax,  elemento in enumerate(row) if elemento == 2)

    suma = 0            
    for meta in ele:
        suma+=1
        
    if suma <= 0:
        print "Nivel completado"
        break
    
for matrizx in Matriz:
        for matrizy in matrizx:
            print matrizy,
        print


    
                    
