temperatura = float(input("Digite a temperatura: "))

if temperatura < 18:
    print("Frio")

elif temperatura >= 18 and temperatura <= 30:
    print("Agradável")

else:
    print("Calor")

print(f"A temperatura informada foi {temperatura}°C")