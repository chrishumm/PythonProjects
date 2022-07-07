import pyinputplus as pyin

height = pyin.inputFloat("What's your height?")

weight = pyin.inputFloat("What's your weight?")


bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, you have a healthy weight.")
elif bmi > 25 and bmi < 30:
        print(f"Your bmi is {bmi}, you are overweight.")
elif bmi > 30:
        print(f"Your bmi is {bmi}, you are obese.")
else:
        print("You are weightless, woohoo!")
