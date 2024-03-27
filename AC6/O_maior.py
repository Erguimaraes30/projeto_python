a = int(input(""))
b = int(input(""))
c = int(input(""))


maiorab = (a + b + abs(a - b)) / 2


maior = (maiorab + c + abs(maiorab - c)) / 2


print(f" {a}, {b}, {c}") 
print(f"{maior} eh o maior")