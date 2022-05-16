import pprint


def countCharacter(message):
    count = {}

    for character in message: #Iterates over the sentence
      count.setdefault(character, 0) #Creates a new key with a default value of 0 for each character
      count[character] = count[character] + 1 #Increments the key value when the key is the same

    return count


message = 'The quick brown fox jumps over the lazy dog'

pprint.pprint(countCharacter(message)) #Prints out how often an ascii character occured

print("Please enter a new sentence")
message = input()

print(pprint.pformat(countCharacter(message)))


#Set default can be used to create a key value only once
