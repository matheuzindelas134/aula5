def maior_dos_dois(x,y,z):
    if x > y and z :
        return f"o numero {x} e maiorque os numero {z} e {y}"
    elif y > x and z  :
        return f"o numero {y} é maior que os numero {x} e {z}"
    elif z > x and y :
        return f"o numero {z} é maior que os numero {x} e {y}"
    else:
        return f"os numeros sao iguais"

print(maior_dos_dois(5,8,9))