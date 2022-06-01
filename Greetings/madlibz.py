#! python3
#  madlibz.py - creates interesting sentences!

import random, re
import pyinputplus as pyip

def randomAdj():
    adjectives = ['happy', 'sad', 'angry', 'confused', 'bored']
    adj = adjectives[random.randint(0, len(adjectives)-1)]
    return adj

def randomNoun():
    noun = ['man', 'woman', 'dog', 'cat', 'giraffe']
    n = noun[random.randint(0, len(noun)-1)]
    return n
def randomVerb():
    verb = ['run', 'swim', 'jump', 'fly', 'sing']
    v = verb[random.randint(0, len(verb)-1)]
    return v

with open('madlibz.txt', 'r') as mad_lib_file:

    result = pyip.inputMenu(['Manual Mode', 'Random Mode'],prompt ='Choose a mode!\n', numbered=True)
    sentence = mad_lib_file.read()
    adj_re = re.compile(r'ADJECTIVE')
    verb_re = re.compile(r'VERB')
    noun_re = re.compile(r'NOUN?')
    if(result == 'Random Mode'):
        while adj_re.search(sentence) != None:
            sentence = adj_re.sub(randomAdj(), sentence,1)

        while verb_re.search(sentence) != None:
            sentence = verb_re.sub(randomVerb(), sentence,1)

        while noun_re.search(sentence) != None:
            sentence = noun_re.sub(randomNoun(), sentence,1)
    else:
        while adj_re.search(sentence) != None:
            result = pyip.inputStr('Please enter an adjective ')
            sentence = adj_re.sub(result, sentence,1)

        while verb_re.search(sentence) != None:
            result = pyip.inputStr('Please enter a verb ')
            sentence = verb_re.sub(result, sentence,1)

        while noun_re.search(sentence) != None:
            result = pyip.inputStr('Please enter a noun ')
            sentence = noun_re.sub(result, sentence,1)
    print(sentence)
    with open('mad_libz_result.txt', 'w') as new_file:
        new_file.write(sentence)
    new_file.close()

mad_lib_file.close()