operacion1 = 1.321*(10**(-4)) + 8.5*(10**(-2))
operacion2 = 1.71*(10**(3)) - 2.01*(10**(2))
operacion3 = (7.34*(10**3)) * (7.2*(10**4))
operacion4 = (7.34*(10**3)) / (7.2*(10**4))

def notacionCientifica(numero):
    valorRedondeado = "{: .3e}".format(numero)
    if "e+" in valorRedondeado:
        valorCientifico = valorRedondeado.replace("e+","x10^")
    if "e-" in valorRedondeado:
        valorCientifico = valorRedondeado.replace("e-","x10^-")
    return valorCientifico
    
print(notacionCientifica(operacion1))
print(notacionCientifica(operacion2))
print(notacionCientifica(operacion3))
print(notacionCientifica(operacion4))