print("Enter your name")
name = input()
print("Repeat how many times?")
repeat = int(input())

for i in range(repeat):
    print("Your name is " + name +".This has repeated " + str(i) +" times.")

#for loops use range(x) and in for i in x 
