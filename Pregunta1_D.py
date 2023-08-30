fusionOro = 1064
fusionHierro = 1538
fusionPlata = 962
fusionZinc = 420
fusionTungsteno = 3422
tempMetales = [fusionPlata, fusionHierro, fusionOro, fusionTungsteno, fusionZinc]
metales = ["Plata", "Hierro", "Oro", "Tungsteno", "Zinc"]
def celsiusKelvin():
    i = 0
    while i < len(tempMetales):
        tempKelvin = tempMetales[i] + 273
        print("La temperatura de fusión del " + metales[i] + " es de " + str(tempKelvin) + " K")
        i = i + 1;

celsiusKelvin()