import random
import os
os.system("cls")
def sorting(acak):
    if len(acak) <= 1:
        return acak
    else:
        patokan = acak[0]
        cilik = []
        gedi = []
        sama = []
        for i in acak:
            if i < patokan:
                cilik.append(i)
            elif i == patokan:
                sama.append(i)
            else:
                gedi.append(i)
        return sorting(cilik) + sama + sorting(gedi)
acak = [random.randint(0, 14) for i in range(10)]
print("Angka Acak : ", acak)
sorted_acak = sorting(acak)
print("Angka Terurut : ", sorted_acak)