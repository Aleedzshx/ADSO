
#meat = input("Escribe cualquier palabra que se te ocurra =")

a = int(input("Enter ax2: "))
b = int(input("Enter bx: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)