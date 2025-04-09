def ngg_2():
    # START
    print("Think about a number from 0 to 1000, and let me guess it!")
    min = 0
    max = 1000
    moves_10 = 0
    while moves_10 >= 10:
        guess = int((max - min) / 2) + min
        print("Guessing:", guess)
        read_answer = input("too low, too high, you guessed")
        moves_10 += 1
        if read_answer == "you guessed":
            print("I won!")
            break
            # STOP
        elif read_answer == "too high":
            max = guess
        elif read_answer == "too low":
            min = guess
        else:
            print("Dont cheat!")
            break
        if moves_10 >= 10:
            print("Game over...")
            break
    return 
    
ngg_2()
