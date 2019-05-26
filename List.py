numeros=[1,2,3,4]
print(numeros)
datos=[4,"cadena",-15,3.14]
print(datos)
numerosExp=numeros+[5,6,7,8]
print(numerosExp)
numerosExp[3]=20
print(numerosExp)
numerosExp.append(12)
print(numerosExp)

r=[numeros,datos,numerosExp]
print(r)
print(r[1])
print(r[0][0])