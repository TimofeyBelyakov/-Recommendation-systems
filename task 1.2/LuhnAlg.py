import re

def LuhnAlg(card):
    answer = False
    cardSub = str(card).replace(' ', '')
    #if(re.match(r'\d+', cardSub)):
    sum = 0
    for i in range(0, len(cardSub), 2):
        sum = sum + int(cardSub[i])
    for i in range(1, len(cardSub), 2):
        if ((int(cardSub[i]) * 2) > 9):
            sum = sum + (int(cardSub[i]) * 2 - 9)
        else:
            sum = sum + int(cardSub[i]) * 2
    answer = bool(sum % 10 == 0)
    return answer

print(LuhnAlg('79927398716'))


