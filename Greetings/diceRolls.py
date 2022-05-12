import random

coin_flips = 100
number_of_simulations = 10000
number_of_streaks = 0
heads_tails = ('H', 'T')
heads_tails_list = []

for simulationNo in range(number_of_simulations):

        for i in range(coin_flips):
            heads_tails_list.append(random.choice(heads_tails))

        same_result = 0
        for index, item in enumerate(heads_tails_list):
         if(same_result == 6):
            number_of_streaks +=1

         if(index == 0):
            pass
         elif(item == heads_tails_list[index-1]):
                same_result+=1
         else:
                same_result = 0
        
        heads_tails_list = []


print('Chance of streak: %s%%' % (number_of_streaks / (coin_flips* number_of_simulations)))
