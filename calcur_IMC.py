def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):

    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

if __name__ == "__main__":
    # Entrada de usuario
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))

    # Calcular el IMC
    imc = calcular_imc(peso, altura)

    # Interpretar el IMC
    descripcion = interpretar_imc(imc)

    # Mostrar resultados
    print(f"Tu IMC es {imc:.2f}")
    print(f"Interpretación: {descripcion}")
