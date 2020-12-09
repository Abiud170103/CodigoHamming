prueba = [0,1,0]
posError = ""

for bucle in prueba:
    posError += str(bucle)

posError = int(str(posError), 2) #Se lo cambia a formato decimal

print(f"El error se encuentra en el bit ({posError})")

