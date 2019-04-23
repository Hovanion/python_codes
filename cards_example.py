#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections, itertools, random
import time



SZIN = ("Kőr", "Pikk", "Káró", "Treff")
SOROZAT = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Bubi", "Dáma", "Király", "Ász")

class card:  #egy kártyalap
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit

    def __repr__(self):
        return self.suit + "-" + self.numeral

class pakli(set):
    def __init__(self):
        for numeral, suit in itertools.product(SOROZAT, SZIN):
            self.add(card(numeral, suit))

    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card

    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            '''
            in_hand=list[]
            for x in range(number_of_cards):
                in_hand.append(self.get_card())
            return in_hand
            '''
            return poker_hand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError


class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        short_desc = "Semmi."
        numeral_dict = collections.defaultdict(int) #default dict - 0
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        #print (numeral_dict, suit_dict)

        # Pár
        if len(numeral_dict) == 4: #csak 1 van a values-ekben
            short_desc = "Egy pár."

        # Két pár vagy drill
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Drill."
            else:
                short_desc ="Két pár."  #kétszer van benne a 2-es érték
        # Full house vagy poker

        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Full house."
            else:
                short_desc ="Póker."
        else:
            straight, flush = False, False

            if len(suit_dict) == 1:
                flush = True

            min_numeral = min([SOROZAT.index(x) for x in numeral_dict.keys()]) #min(float(i) for i in list)
            max_numeral = max([SOROZAT.index(x) for x in numeral_dict.keys()])

            if int(max_numeral) - int(min_numeral) == 4:
                straight = True

            low_straight = set(("Ász", "2", "3", "4", "5"))

            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True

            if straight and not flush:
                short_desc ="Sor."

            elif flush and not straight:
                short_desc ="Flush."

            elif flush and  straight:
                short_desc ="Royal flush."

        osztott_lap = " + ".join([str(x) for x in self.card_list])
        return f"{print_hand} ------> ({short_desc})"

##################
a=input("Hogy hívnak?\n")

print ("Üdv %s, most osztok neked lapokat és megmondom mi van benne:" % a)
for i in range(3):
    print (f"{i+1}")
    time.sleep(0.5)
print(pakli().get_hand())



#összehasonlítás két osztással


print ("Viszlát és kössz a halakat")
