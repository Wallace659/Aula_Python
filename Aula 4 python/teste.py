def horario(horas):
    if horas >= 6 and horas <= 12:
        return "Bom dia!"
    elif horas > 12 and horas <= 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
hora = int(input("Digite que horas são:"))
print(horario(hora))

hr = int(input("Digite que horas são: "))
print(horario(hr))

xy = int(input("Digite outra hora: "))
print(horario(xy))

daqui_2_horas = int(input("Digite a hora: "))
print(horario(daqui_2_horas + 2))
