# -*- coding: utf-8 -*-
import smtplib

import time
import yfinance as yf
""" Programa beriot iz config.ini informaciju pro tikeri (nazvanije i diapozon dopustimich znacenij)
, razberaet infu do nuznovo sostojanija i proveriaet cerez YFinance na birze sootvetstvije atributa
RegularMarketPrice k zadonomu cenovomu diapazonu v config.ini. Jesli jest nesootvetstvije v tecenii 15min
, visilaet pismo po zadannomu adresu s opovescejijem, cto tiker visiol iz diapozona. Vsia programa 
razmescena v zadavaemij dniami vremenoj cikl nabliudejija. 
"""
tiker_ = list()  # коментарий на кирилеце
dict_tiker = dict()
index = list()
outofrange = list()
n = float(input('Cколько дней хотите мониторить:'))
start_t = time.time()  # время старта
finish_t = time.time() + n * 86400  # Время окончания, дни n превращаем в секунды 1min=0.002
while time.time() <= finish_t:  # zapuskaem cikl intervala vremeni nabiudenij
    with open('config.ini', 'r') as f:  # citaem dannije iz faila config.ini
        tiker = f.read()
        tiker = tiker.split('}\n{')  # obrabotka scitanich danix-svod v nuznij format
    for i in range(len(tiker)):
        if i == 0:  # s 1 saga k sledujuscenu
            tiker[i] = tiker[i][1:]  # skinul s peredi {
        elif i == len(tiker) - 1:  # idem dalshe
            tiker[i] = tiker[i][:len(tiker[i]) - 1]  # skinuli s konca }
        tiker_ += tiker[i].split(':')  # imejem spisok tikerov (index-kliuc i znacenije)
    for i in range(0, len(tiker_), 2):
        dict_tiker[tiker_[i]] = tiker_[i + 1]  # polucili slovar kliuc-index i min/max znacenija
        index = list(dict_tiker)  # imeem spisok indeksov-kliuceij? mozet on i ne nuzen?
    for i in range(len(index)):  # razbiv znacenij min i max na cifru
        reiksmes = dict_tiker[index[i]][1:-1]
        reiksmes = reiksmes.split(",")
        minimum, maksimum = float(reiksmes[0]), float(
            reiksmes[1])  # nado polucit kotirovki po etim indeksam
        tickeris = yf.Ticker(index[i])  # delaem zapros v birzu pro tiker iz spiska
        x = tickeris.info['regularMarketPrice']  # X prisvaevaem znacenija tekusciai ceni tikera s birzi
        print(x, type(x), (minimum < x < maksimum))  # INFO TESTA dlai ocevidnosti
        if not (minimum < x < maksimum):  # proverka sootvetstvija ceni tikera s zadanimi znacenijami
            if index[i] in outofrange:  # proveriu nalicije Tikera v spiske tikerov OUTOFRANGE
                smtpObj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
                smtpObj.login('markus0013@mail.ru', 'QzK7xDaSdMAqXNL7BJtb')
                smtpObj.sendmail("markus0013@mail.ru", "markus0013@mail.ru",
                                 f'Tiker {index[i]} vne diapazona, znacenije = {x}')
                smtpObj.quit()

            else:
                outofrange += [index[i]]  # jesli ne nasiol tam tikera, to dabavliu
    print(f'Vremia pereriva {time.ctime()}', 'OUTOFRANGE', outofrange, type(outofrange))
    time.sleep(30)  # po scenariju mozno prervatsia na 15 min(15*60=900)
