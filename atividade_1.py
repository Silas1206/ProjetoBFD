notas = [8,7.5,-1,10,11,6,0,9,None,5]
notas_invalidas=0
nota_maior= notas[0]
nota_menor=notas[0]
total=0
notas_validas=0
for x in notas:
    if  x is not None and x >=0 and x <=10:  
        total += x 
        notas_validas = notas_validas +  1
        if x > nota_maior:
            nota_maior =x 
        if x <nota_menor:
            nota_menor=x
    else:
        notas_invalidas = notas_invalidas +1 
media= total/notas_validas 
print(f"media é {media}\n nota maior {nota_maior}\n nota menor{nota_menor}\n notas inválias {notas_invalidas}"
      )