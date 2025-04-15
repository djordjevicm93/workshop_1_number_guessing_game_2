def ngg2():
    """
    Number guessing game 2

    Computer is guessing your number 1 to 1000.
    You answer: too high, too low, you win.
    Try it.
    """
    print("Think about a number from 1 to 1000, and let me guess it!")
    min = 1
    max = 1000
    moves = 0
    max_moves = 10
    while moves < max_moves:
        guess = (max - min) // 2 + min
        print(f"Guessing: {guess}")
        answers = input("Enter your response ('Too low', 'Too high', 'You win'): ").strip().lower()
        if answers == "you win":
            print("I won!")
            return
        elif answers == "too high":
            max = guess
        elif answers == "too low":
            min = guess
        else:
            print("Don't cheat!")
            return
        moves += 1
    print("Hmm... something's wrong. Are you sure you're not cheating?")

ngg2()
