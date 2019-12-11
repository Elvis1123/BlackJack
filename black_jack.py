'''
21 BLACKJACK GAME
'''

import random
import sys 


class Player:
    def __init__(self,name,novac):
        self.novac = novac
        self.name = name
    
    def place_a_bet(self,bet):
        self.novac -=bet
        print(f'Stanje vaseg racuna je: {self.novac} \nPolozena opklada iznosi {bet} [KM]')

    def win(self,bet):
        self.novac += 2 * bet

    def __str__(self):
        return (f'Stanje vaseg racuna je {self.novac}')


def dek_karata():
    znak = ['MAK','SRCE','KARO','TREF']
    brojevi = [1,2,3,4,5,6,7,8,9,10,12,13,14]
    dek = []

    for num in brojevi:
        for mrk in znak:
            dek.append([(num,mrk)])

    return dek


def shuffled_deck(dek = []):
    shuffle = random.sample(range(52), 52)
    mixed_deck = []
    for num in shuffle:
        i = 0
        try:
            mixed_deck.append(dek[num])
            i+=1
        except:
            print(f'nesto se uzjebalo {i}  {len(shuffle)}')
    return mixed_deck


def black_jack_value(i = 0 ,lista = [0]):
    if(lista[i][0][0]>=10):
        print(f'Potez {i}! Izvukli ste {lista[i]}, to racunamo 10 \n')
        return 10
    elif(lista[i][0][0]==1):
        print(f'Potez {i}! Izvukli ste {lista[i]}\n')
        unos=0
        while(unos!=1 and unos!=11):
            unos=int(input('Izaberite 1 ili 11 !'))
        else:
            print(f'Potez {i}! Izabrali ste {unos}\n')
            return unos
    else:
        print(f'Potez {i}! Izvukli ste {i}. kartu  {izmjesani_dek[i]}\n')
        return lista[i][0][0]

def izvlačenje_karte(redni_br, dek = []):
    return dek[redni_br]
suma_player = 0

if __name__ == "__main__":
    i = 4
    dek = dek_karata()
    izmjesani_dek = shuffled_deck(dek)
    neotkrivena_karta = izmjesani_dek[0]
    karta1_comp = izmjesani_dek[1]  
    karta1_player = izmjesani_dek[2] 
    karta2_player = izmjesani_dek[3]
    suma_player = 0
    suma_computer = karta1_comp + neotkrivena_karta

    ime = input('Vaše ime?')
    novac = int(input('Koliko novca zelite staviti na vas racun?'))

    player1 = Player(ime,novac)

    polog = int(input('Na koliko novca se kladite?'))
    while(polog > novac):
        print('Nemate dovoljno novca na računu')
        potvrda = input('Nemate dovoljno novca za zeljeni ulog. Prihvate li ALL IIN [Y/N]')
        if(potvrda.lower()=='y'):
            polog = player1.novac
        else:
            print('Drugi put')
            exit()
        
      
    player1.place_a_bet(polog)
    print(f'Otkrivena karta Dealera je {karta1_comp}')
    print(f'Vaše otkrivene karte su {karta1_player},{karta2_player}')
    suma_player = black_jack_value(2,izmjesani_dek) + black_jack_value(3,izmjesani_dek)
    print(f'Ukupna vrijednost')
    suma_computer=black_jack_value(0,izmjesani_dek) + black_jack_value(1,izmjesani_dek)



    while (suma_player<=21 and suma_computer<=21):
        potez = input('HIT or STAY [H/S]')
        if(potez.lower()=='h'):
            suma_player  += black_jack_value(i,izmjesani_dek)
        elif(potez.lower()=='s'):
            if suma_player > suma_computer:
                print(f'Pobjednik je KOMPJUTER, sa osvojenih {suma_computer} bodova')
                exit()
            else:
                print(f'Pobjednik je IGRAČ, sa osvojenih {suma_player} bodova')
                exit()
        else:
            print('Unijeli ste pogresno slovo')

    else:
        if suma_player > suma_computer:
            print(f'Pobjednik je KOMPJUTER, sa osvojenih {suma_computer} bodova')
        else:
            print(f'Pobjednik je IGRAČ, sa osvojenih {suma_player} bodova')






