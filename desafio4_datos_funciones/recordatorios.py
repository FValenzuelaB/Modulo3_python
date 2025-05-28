
recordatorios=[
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],  #Lista de recordatorios originales
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
    ]
recordatorios.insert(1,['2021-01-02','06:00','Empezar el año']) # Se crea recordatorio, el desafio dice que sea el 2 de febrero pero en el output esperado dice el 2 de enero, dado que es empezar el año, tiene mas sentido que sea en enero, se deja en enero.
recordatorios[3][0]='2021-07-16' #se corrige fecha del feriado 15 de julio a 16 de julio
del recordatorios[2] #Se borra recordatorio de no trabajar, Tu tiene que tlabajal, mucho tlabajo
recordatorios.insert(4,['2021-12-24', '22:00', 'Cena de Navidad']) # Se agrega recordatorio cena de navidad
recordatorios.insert(6,['2021-12-31', '22:00', 'Cena de Año Nuevo']) # Se agrega recordatiro de Cena de año nuevo



for i in recordatorios:
    print(i) #Formato levemente distinto al pedido por el desafío, pero me parece un poco mas ordenado.
