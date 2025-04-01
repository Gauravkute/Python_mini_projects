from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:  # Compare characters at the same index
                error += 1  # Increment error count if characters don't match
        except IndexError:
            error += 1  # Handle case where usertest is shorter than partest
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(userinput) / time_roundoff
    return round(speed, 2)

while True:
    ck = input("Ready to test : yes/no\n")
    if ck=="yes":
        test = [
        "Lorem, ipsum dolor sit amet consectetur adipisicing elit. "
        "Quasi, aliquid obcaecati eligendi, expedita eos ex provident eum veniam a facere quae "
        "earum facilis labore incidunt error. Illum minus mollitia fuga."
    ]
        test1 = r.choice(test)
        print("***** Typing Speed tester *****")
        print(test1)
        print()

        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print('Speed: ', speed_time(time_1, time_2, testinput), 'w/sec')
        print("Error: ", mistake(test1, testinput))
    elif ck == "no":
        print("thank you")
        break

    else:
        print("Wrong input")
