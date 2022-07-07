import random
import pyinputplus as pyin

names = pyin.inputFilename("Enter names seperated by commas: ")
name_list = names.split(', ')
for i in range (10):
    print(f"{name_list[random.randint(0,len(name_list)-1)]} will pay the bill today!")