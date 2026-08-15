


print('"Bank Colombia"')
print('"Tenemos un interes anual del 12,0%"')

Invest = int(input("Cuanto dinero deseas invertir:\n"))

time = float(input("Por cuanto años desea mantener su inversion?:\n"))

tasa= 0,12

final_amount = Invest * (1 + tasa) ** time


# Fórmula de interés compuesto: Monto = Capital * (1 + tasa) ^ tiempo
print(f"Tu ganancia seria de , {final_amount}")