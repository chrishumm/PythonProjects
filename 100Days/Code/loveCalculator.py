import pyinputplus as pyin

print("Welcome to the love calculator!")
name1 = pyin.inputStr("Write the first name here: ")
name2 = pyin.inputStr("Write the second name here: ")

def calculateLoveScore(alphabet_list):
    sum = alphabet_list['t'] + alphabet_list['r'] + alphabet_list['u'] + alphabet_list['e'] + alphabet_list['l'] + alphabet_list['o'] + alphabet_list['v'] + alphabet_list['e']
    return sum

def countCharacters(name):
    alphabet_list = {'a' : 0 ,'b' : 0,'c' :0 ,'d' : 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    for indices, value in enumerate(name):
        if(value in alphabet_list):
            alphabet_list[value] += 1

    return alphabet_list


list_1 = countCharacters(name1.lower())
list_2 = countCharacters(name2.lower())

loveScore = int(str(calculateLoveScore(list_1)) + str(calculateLoveScore(list_2)))

if loveScore < 10 or loveScore > 90:
    print(f'Your love score is {loveScore}, you go together like mentos and coke.')
elif loveScore >= 40 and loveScore <= 50:
    print(f'Your love score is {loveScore}, you go well together')
else:
    print(f'Your love score is {loveScore}')