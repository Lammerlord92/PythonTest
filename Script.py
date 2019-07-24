import sys
print("Mi primer script")
if len(sys.argv)==2:
    texto=sys.argv[1]
    rep=int(sys.argv[2])
    for n in range(rep):
        print(texto)
    print(sys.argv)
else:
    print("Introduce los argumentos correctos (texto numero)")