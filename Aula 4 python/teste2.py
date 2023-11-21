def numeromaior(n1,n2,n3):
    if n1 > n2 and n3:
        return "O primeiro numero é maior"
    elif n2 > n1 and n3:
        return "O segundo numero é maior"
    else:
        return "O terceiro numero é maior"
    
print(numeromaior(2,3,8))