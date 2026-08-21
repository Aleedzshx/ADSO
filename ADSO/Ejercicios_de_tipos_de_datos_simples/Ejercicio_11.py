
print("Bienvenido a tu cuenta de ahorros!")
print("Tenemos un interes amnua del 4%")

rate = 0.04
deposit = int(input("Cuanto dinero desea depositar:\n"))
time = 0

profit = deposit * (rate + 1) ** time

for i in range(0,2):
    time = +1 