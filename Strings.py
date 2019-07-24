print("C:\nombre\directorio")
print(r"C:\nombre\directorio")
s="Una cadena " " compuesta de dos cadenas"
print(s)
diez_espacios=" "*10
print(diez_espacios+"diezEspaciosPuestos")

palabra="Python"
print(palabra[0])
print(palabra[3])
print(palabra[-1])
print(palabra[-2])
print(palabra[0:2])
print(palabra[2:-1])
print(palabra[2:])
print(palabra[:-1])
#print(palabra[99])
print(palabra[:99])
longit=len(palabra)
print(longit)
print(palabra.upper())
print(palabra.lower())

print(palabra[2:-1].capitalize())

hM="heLlo worLd"


print(hM.upper())
print(hM.lower())
print(hM.capitalize())
print(hM.title())
print(hM.count("o"))
print(hM.find("worLd"))


hM="heLlo worLd worLd worLd"
print(hM.rfind("worLd")) #reverse find

c="100"
print(c)
print(c.isdigit())

c2="agsahdj897616"
print(c2)
print(c2.isalnum())
print(c2.isalpha())



lS=hM.split()
print(lS[-1])

s="Hola,mundo,mundo"
s.split(',')

print(",".join(hM))

s="         ashdjsadk  ".strip()
print(s)
s="-----------ashdjsadk----------".strip("-")
print(s)

