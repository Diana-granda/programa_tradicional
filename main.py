# Programación Tradicional

def ingresar_lluvia_diaria():
    lluvias = []
    for i in range(7):
        lluvia = float(input(f"Ingrese la cantidad de lluvia para el día {i + 1} (en mm): "))
        lluvias.append(lluvia)
    return lluvias

def calcular_promedio_semanal(lluvias):
    promedio = sum(lluvias) / len(lluvias)
    return promedio

def main():
    lluvias_diarias = ingresar_lluvia_diaria()
    promedio_semanal = calcular_promedio_semanal(lluvias_diarias)
    print(f"El promedio semanal de cantidad de lluvia es: {promedio_semanal:.2f} mm")

if __name__ == "__main__":
    main()
