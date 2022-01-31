import os
import time

print(os.getcwd())

wr_ip_adres = []
ok_wr = []

n = float(input('Cколько дней хотите мониторить:'))      # 1 мин примерно 0,0007 дня(это для проверки)
start_t = time.time()                                    # время старта
finish_t = time.time() + n*86400                         # Время окончания, дни n превращаем в секунды
with open('config.ini', 'r') as f:
    ip_adres = f.read()
    ip_adres = ip_adres.split(',')
while time.time() <= finish_t:                            # проверяем савпадения времяни с временем окончания
    for i in range(len(ip_adres)):
        if not os.system("ping -n 1 " + ip_adres[i]) == 0:  # делаем пинг, если нет ответ, то пишем в ping_log.ini
            with open('ping_log.ini', 'a') as f:
                f.write(f'{ip_adres[i]} Не отвечает. Время сбоя: {time.ctime()}\n')
            if not ip_adres[i] in wr_ip_adres:
                wr_ip_adres += [ip_adres[i]]
    for j in range(len(wr_ip_adres)):
        if os.system("ping -n 1 " + wr_ip_adres[j]) == 0:  # делаем пинг, если есть ответ, пишем в ping_log.ini
            with open('ping_log.ini', 'a') as f:
                f.write(f'{wr_ip_adres[j]} Отозвался. Время отклика: {time.ctime()}\n')
            ok_wr += [wr_ip_adres[j]]
    ip_adres = [i for i in ip_adres if i not in wr_ip_adres]
    ip_adres += ok_wr
    wr_ip_adres = [i for i in wr_ip_adres if i not in ok_wr]
    ok_wr = []
print('Отчет можно посмотреть в файле ping_log.ini')
print('IP которые, на момент завершения, отзывались', ip_adres)
print('IP которые, на момент завершения, НЕ отзывались', wr_ip_adres)
