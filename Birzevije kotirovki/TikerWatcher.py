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
    index=list(dict_tiker)                                  # ����� ������ ��������
                                                            # ���� �������� ��������� �� ���� ��������
                                                            # � �� �������� � ��� � ���

    reiksmes=dict_tiker[index[0]][1:-1]                     # �������� �������� ��� � ��� ��� �����.�������
    reiksmes=reiksmes.split(",")                            # ��� ���� ���������
    minimum, maksimum =int(reiksmes[0]), int(reiksmes[1])
    print(minimum<maksimum)