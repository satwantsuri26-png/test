secret = 2
print ("You have 💗💗💗💗💗 lives.")
guess1 = int(input("What is your first guess for the number?"))
if guess1 >= 5 and <= 12:
    print ("🌡️")
if guess1 <5:
    print ("🔥")
if guess1 >=20 and <=30:
    print ("🥶")
if guess1 <=50 and >=30:
    print ("🧊")
if guess1 != 2:
    print ("You have 💗💗💗💗 lives left!")
if guess1 == 2:
    print ("You have guessed the number!")

guess2 = int(input("What is your second guess for the number?"))
if guess2 >= 5 and <= 12:
    print ("🌡️")
if guess2 <5:
    print ("🔥")
if guess2 >=20 and <=30:
    print ("🥶")
if guess2 <=50 and >=30:
    print ("🧊")
if guess2 != 2:
    print ("You have 💗💗💗 lives left!")
if guess2 == 2:
    print ("You have guessed the number!")

guess3 = int(input("What is your third guess for the number?"))
if guess3 >= 5 and guess3 <= 12:
    print ("🌡️")
if guess3 <5:
    print ("🔥")
if guess3 >=20 and guess3 <=30:
    print ("🥶")
if guess3 <=50 and guess3 >=30:
    print ("🧊")
if guess3 != 2:
    print ("You have 💗💗 lives left!")
if guess3 == 2:
    print ("You have guessed the number!")

guess4 = int(input("What is your fourth guess for the number?"))
if guess4 >= 5 and <= 12:
    print ("🌡️")
if guess4 <5:
    print ("🔥")
if guess4 >=20 and <=30:
    print ("🥶")
if guess4 <=50 and >=30:
    print ("🧊")
if guess4 != 2:
    print ("You have 💗 lives left!")
if guess4 == 2:
    print ("You have guessed the number!")

guess5 = int(input("What is your final guess for the number?"))
if guess5 >= 5 and <= 12:
    print ("🌡️")
if guess5 <5:
    print ("🔥")
if guess5 >=20 and <=30:
    print ("🥶")
if guess5 <=50 and >=30:
    print ("🧊")
if guess5 != 2:
    print ("You have 0 lives left! You have failed to guess the number! The number was '2' ")
if guess5 == 2:
    print ("You have guessed the number!")