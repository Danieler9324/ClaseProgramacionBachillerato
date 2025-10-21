print("Dame la edad del primer amigo")
edad1=int(input())
print("Dame la edad del sengundo amigo")
edad2=int(input())
print("Dame la edad del tercer amigo")
edad3=int(input())
print("Dame la edad del cuarto amigo")
edad4=int(input())
print("Dame la edad del quinto amigo")
edad5=int(input())
mayor=edad1
if (edad2>mayor):
    mayor=edad2
if (edad3>mayor):
    mayor=edad3
if (edad4>mayor):
    mayor=edad4
if (edad5>mayor):
    mayor=edad5
print("El mayor de las amigos tiene ", mayor)