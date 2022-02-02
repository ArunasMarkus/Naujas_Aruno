tiker_=list()
dict_tiker=dict()
index=list()
reiksmes=''
minimum=int()
maksimum=int()
with open('config.ini', 'r') as f:
    tiker = f.read()
    tiker = tiker.split('}\n{')
    for i in range(len(tiker)):
        if i==0 :
            tiker[i] = tiker[i][1:]
        elif i == len(tiker)-1:
            tiker[i] = tiker[i][:len(tiker[i])-1]
        tiker_ += tiker[i].split(':')
    for i in range(0,len(tiker_),2):
        dict_tiker[tiker_[i]] = tiker_[i+1]
    index=list(dict_tiker)                                  # имеим список индексов
                                                            # надо получить котировки по этим индексам
                                                            # и их сравнить с мин и мах

    reiksmes=dict_tiker[index[0]][1:-1]                     # получаем значения мин и мах для конкт.индекса
    reiksmes=reiksmes.split(",")                            # это надо зациклить
    minimum, maksimum =int(reiksmes[0]), int(reiksmes[1])
    print(minimum<maksimum)