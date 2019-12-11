
import random
#Nasumičnost broj
random.sample(range(52), 52)
#Nasumičnost znaka



def dek_karata():
    znak = ['MAK','SRCE','KARO','TREF']
    brojevi = [1,2,3,4,5,6,7,8,9,10,12,13,14]
    dek = []

    for num in brojevi:
        for mrk in znak:
            dek.append([(num,mrk)])

    return dek

print(dek_karata())