texto = input("\n ingrese un texto cualquiera: ")
texto_m = texto.lower()

letra1 = input("\nIngrese una letra: ")
letra2 = input("Ingrese una letra: ")
letra3 = input("Ingrese una letra: ")

letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

letras =[letra1,letra2,letra3]

print(f"\nla cantidad de veces que {letra1} aparece en {texto} es {texto.count(letra1)}")
print(f"la cantidad de veces que {letra2} aparece en {texto} es {texto.count(letra2)}")
print(f"la cantidad de veces que {letra3} aparece en {texto} es {texto.count(letra3)}")