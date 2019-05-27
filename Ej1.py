matriz=[
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]

n=0
while n<len(matriz):
    matriz[n][-1]=sum(matriz[n][:-1])
    n=n+1

print(matriz)

cadena="Hola"
print(cadena[::-1])