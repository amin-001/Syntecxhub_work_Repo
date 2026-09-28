import random

LEVELS = {
    "1": ("Easy", 1, 10),
    "2": ("Medium", 1, 50),
    "3": ("Hard", 1, 100),
    "4": ("Expert", 1, 500),
}

best_scores = {}


def pick_level():
    print("\nChoose a difficulty:")
    for key, (name, low, high) in LEVELS.items():
        print(f"  {key}) {name}  ({low} to {high})")

    while True:
        choice = input("Your choice: ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("Oops, please type 1, 2, 3 or 4.")


def play_round(low, high):
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}. Good luck!")
    print("(Type 'q' at any time to give up.)")

    while True:
        text = input(f"Guess #{attempts + 1}: ").strip().lower()

        if text == "q":
            print(f"No worries! The number was {secret}.")
            return None

        try:
            guess = int(text)
        except ValueError:
            print("Hmm, that's not a whole number. Try again.")
            continue

        if guess < low or guess > high:
            print(f"Please stay between {low} and {high}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try a bigger number.")
        elif guess > secret:
            print("Too high! Try a smaller number.")
        else:
            if attempts == 1:
                print("WOW, you got it on the first try!")
            else:
                print(f"You got it! It took you {attempts} guesses.")
            return attempts


def record_score(level_name, attempts):
    old_best = best_scores.get(level_name)

    if old_best is None:
        best_scores[level_name] = attempts
        print(f"First score on {level_name}, nice start!")
    elif attempts < old_best:
        best_scores[level_name] = attempts
        print(f"New record! You beat your old best of {old_best}.")
    else:
        print(f"Your best on {level_name} is still {old_best}. Can you beat it?")


def show_best_scores():
    print("\n\tBest scores (fewest guesses)")
    for name, low, high in LEVELS.values():
        if name in best_scores:
            print(f"  {name}: {best_scores[name]}")
        else:
            print(f"  {name}: no score yet")


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print("\tNumber Guessing Game")

    playing = True
    while playing:
        name, low, high = pick_level()
        attempts = play_round(low, high)

        if attempts is not None:
            record_score(name, attempts)

        show_best_scores()
        playing = ask_play_again()

    print("\nThanks for playing! See you next time.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame ended. Bye!")