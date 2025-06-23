"""definire una lista e trovare la posizione (indice) del numero più alto nella lista
chiedere all'utente di inserire dei voti (float) terminato l'inserimento visualizzare il voto e quello più
basso"""
numeri=[10,8,34,54,68,199,2,169,4]
max_num=0
position=0

for num in numeri:
    if max_num <num:
        max_num = num
        position=numeri.index(max_num)
print(f"il numero più alto è {max_num} in posizione {position} ")

#utilizzo un ciclo  while per iterare l'utilizzo di .append
voti=[]
while True:
    voto=(input("voto: "))
    if voto== "fine":
        break
    else:
        voti.append(float(voto)) #converto qui perchè, se forzassi un float in input, non potrei leggere la stringa fine

print(voti)
max_voti=0
min_voti=10
position_max=0
position_min=0
for vot in voti:
    if max_voti < vot:
        max_voti=vot
        position_max=voti.index(max_voti)
    elif min_voti > vot:
        min_voti= vot
        position_min=voti.index(min_voti)
print(f"il voto più alto è {max_voti}in posizione {position_max}")
print(f"il voto più basso è {min_voti}in posizione {position_min}")