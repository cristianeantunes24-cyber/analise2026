anon= float(input(" digite o ano de nascimento "))
anoat= float(input(" digite o ano de atual ")) 
idade = anoat - anon

if idade>=18:
    print(f"você é maior de idade {idade}")

else:
    print(f"você é menor de idade {idade}")